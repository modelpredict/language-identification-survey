import pandas as pd


def tatoeba_2021_06_05():
  dataset_path = 'datasets/tatoeba-sentences-2021-06-05/sentences.csv'
  return pd.read_csv(dataset_path, sep='\t', index_col=0, names=['language', 'text'])
