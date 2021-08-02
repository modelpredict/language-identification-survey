from argparse import ArgumentError
from langcodes import Language
import pandas as pd


def get_alpha3(lang):
  l = Language.get(lang)
  try:
    return l.to_alpha3()
  except:
    return None


def get(name):
  if name.replace('-', '_') == 'tatoeba_sentences_2021_06_05':
    return tatoeba_sentences_2021_06_05()
  if name.replace('-', '_') == 'tatoeba_sentences_2021_06_05_common_48':
    return tatoeba_sentences_2021_06_05_common_48()
  raise ArgumentError(f"Unkown dataset {name}")


def tatoeba_sentences_2021_06_05():
  dataset_path = 'datasets/tatoeba-sentences-2021-06-05/sentences.csv'
  ds = pd.read_csv(dataset_path, sep='\t', index_col=0, names=['language', 'text'], dtype={'language': 'category'})
  ds['alpha3'] = ds['language'].apply(get_alpha3).astype("category")
  return ds


def tatoeba_sentences_2021_06_05_common_48():
  dataset_path = 'datasets/tatoeba-sentences-2021-06-05-common-48/sentences.csv'
  ds =  pd.read_csv(dataset_path, index_col=0, names=['language', 'text'], dtype={'language': 'category'})
  ds['alpha3'] = ds['language'].apply(get_alpha3).astype("category")
  return ds


def get_supported_dataset_subset(dataset, supported_languages):
  return dataset[dataset['alpha3'].isin(supported_languages)]
