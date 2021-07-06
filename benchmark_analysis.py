import os
import argparse
import pandas as pd
import numpy as np

from jinja2 import Environment, select_autoescape, FileSystemLoader

import datasets
import dataset_analysis
from benchmarks import BENCHMARKS
from langtools import get_iso_alpha3


def read_results(dataset_name, benchmark_name='fasttext'):
  results_path = os.path.join('results', dataset_name, benchmark_name, 'results.csv')
  results = pd.read_csv(results_path, sep=',', index_col=0, names=['detected_lang', 'detected_prob'])
  results['iso_lang_code'] = results['detected_lang'].apply(lambda x: get_iso_alpha3(x.replace('__label__', '')))
  return results


def join_results(dataset, results):
  joined = dataset.join(results)
  joined['correct'] = (joined['language'] == joined['iso_lang_code']).astype(int)
  joined['incorrect'] = 1 - joined['correct']
  return joined


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Write aggregated results files.')
  parser.add_argument('benchmarks', nargs='+')
  parser.add_argument('--dataset_name', type=str, default='tatoeba-sentences-2021-06-05')

  args = parser.parse_args()

  jinja_env = Environment(loader=FileSystemLoader("./templates"), autoescape=select_autoescape())

  dataset_name = args.dataset_name
  for benchmark_name in args.benchmarks:
    print(f"Analyzing {benchmark_name} results on {dataset_name}")
    dataset = datasets.get(dataset_name)
    results = read_results(dataset_name, benchmark_name)
    supported_langs = BENCHMARKS[benchmark_name]['supported_languages']
    dataset_subset = datasets.get_supported_dataset_subset(dataset, supported_languages=supported_langs)

    dataset_stats = dataset_analysis.get_stats_table(dataset_subset)

    joined_results = join_results(dataset_subset, results)

    accuracy = joined_results['correct'].mean()

    accuracy_per_language = joined_results.groupby('language').agg({'correct': [np.mean, 'count']})
    accuracy_per_language.columns = ['accuracy', 'datapoints']
    accuracy_per_language['datapoints'] = accuracy_per_language['datapoints'].astype(int)
    accuracy_per_language = accuracy_per_language.sort_values(['accuracy'], ascending=False)

    tmpl = jinja_env.get_template('model_results.md')
    rendered = tmpl.render(
      benchmark_name=benchmark_name,
      dataset_name=dataset_name,
      dataset_stats=dataset_stats.to_markdown(),
      accuracy=accuracy,
      stats_per_language=accuracy_per_language.to_markdown(floatfmt=".3f"),
    )
    results_path = os.path.join('results', dataset_name, benchmark_name, 'results.md')
    with open(results_path, 'w') as fd:
      fd.write(rendered)

    # TODO
    # confusion_matrix = pd.pivot_table(joined_results, values='incorrect', index=['language', 'iso_lang_code'], aggfunc=np.sum)

    # confusion_matrix['incorrect'].quantile([i/100 for i in itertools.chain(range(0, 90, 10), range(90, 100))])
    # confusion_matrix[confusion_matrix['incorrect'] > 600]
    # fasttext_dataset['language'] == 'hrv'
    # (fasttext_dataset['language'] == 'hrv').value_counts()
