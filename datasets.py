from argparse import ArgumentError
import pandas as pd


def get(name):
  if name.replace('-', '_') == 'tatoeba_sentences_2021_06_05':
    return tatoeba_2021_06_05()
  raise ArgumentError(f"Unkown dataset {name}")


def tatoeba_2021_06_05():
  dataset_path = 'datasets/tatoeba-sentences-2021-06-05/sentences.csv'
  return pd.read_csv(dataset_path, sep='\t', index_col=0, names=['language', 'text'])


def get_supported_dataset_subset(dataset, supported_languages):
  return dataset[dataset['language'].isin(supported_languages)]
