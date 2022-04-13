import re
from argparse import ArgumentError
from glob import glob

import pandas as pd
from langcodes import Language


__DATASETS = {}


def get_alpha3(lang):
    l = Language.get(lang)
    try:
        return l.to_alpha3()
    except:
        return None


def dataset(load_fn):
    __DATASETS[load_fn.__name__] = load_fn
    return load_fn


def get(name):
    name = name.replace("-", "_")
    if name in __DATASETS:
        return __DATASETS[name]()
    raise ArgumentError(f"Unkown dataset {name}")


def names():
    return [name.replace("_", "-") for name in __DATASETS.keys()]


@dataset
def tatoeba_sentences_2021_06_05():
    dataset_path = "datasets/tatoeba-sentences-2021-06-05/sentences.csv"
    ds = pd.read_csv(
        dataset_path,
        sep="\t",
        index_col=0,
        names=["language", "text"],
        dtype={"language": "category"},
    )
    ds["alpha3"] = ds["language"].apply(get_alpha3).astype("category")
    return ds


@dataset
def tatoeba_sentences_2021_06_05_common_48():
    dataset_path = "datasets/tatoeba-sentences-2021-06-05-common-48/sentences.csv"
    ds = pd.read_csv(
        dataset_path,
        index_col=0,
        names=["language", "text"],
        dtype={"language": "category"},
    )
    ds["alpha3"] = ds["language"].apply(get_alpha3).astype("category")
    return ds


@dataset
def WiLI_2018():
    dataset_text = open("datasets/WiLI-2018/x_train.txt").read().split("\n")[:-1]
    dataset_label = open("datasets/WiLI-2018/y_train.txt").read().split("\n")[:-1]

    ds = pd.DataFrame({"language": dataset_label, "text": dataset_text})
    ds["alpha3"] = ds["language"].apply(get_alpha3).astype("category")

    return ds


@dataset
def open_subtitles_v2018_100k_per_lang():
    dataset_files = "datasets/open-subtitles-v2018-100k-per-lang/*.txt"
    dfs = []
    for f in glob(dataset_files):
        sentences = open(f, encoding="utf-8").readlines()
        language = re.split("[\./]", f)[-2]
        data = dict(
            text=sentences,
            language=language,
        )
        dfs.append(pd.DataFrame(data=data))

    big_df = pd.concat(dfs).reset_index().drop("index", axis=1)
    big_df["language"] = big_df["language"].astype("category")
    big_df["alpha3"] = big_df["language"].apply(get_alpha3).astype("category")
    return big_df


def get_supported_dataset_subset(dataset, supported_languages):
    return dataset[dataset["alpha3"].isin(supported_languages)]
