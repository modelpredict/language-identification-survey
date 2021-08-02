import os
import pathlib
import argparse
import pandas as pd
import numpy as np

from jinja2 import Environment, select_autoescape, FileSystemLoader
from langcodes import Language

import datasets
import dataset_analysis
from benchmarks import BENCHMARKS
from langcodes import Language


def get_alpha3(l):
  try:
    return Language.get(l).to_alpha3()
  except:
    return 'unk'


def read_results(dataset_name, benchmark_name='fasttext', lang_dtype='str'):
  results_path = os.path.join('results', dataset_name, benchmark_name, 'results.csv')
  results = pd.read_csv(results_path, sep=',', index_col=0, names=['detected_lang', 'detected_prob'])
  # langdetect/pycld2 returns nan for small number of rows. We'll just convert them to strings
  results['detected_lang'] = results['detected_lang'].astype(str)
  results['detected_lang_alpha3'] = results['detected_lang'].apply(lambda x: get_alpha3(x.replace('__label__', ''))).astype(lang_dtype)
  return results


def accuracy(results_df):
  correct = (results_df['alpha3'] == results_df['detected_lang_alpha3']).astype(int)
  return correct.mean()


def get_stats_per_language(results):
  langs = results['alpha3'].unique().tolist()
  class_metrics = {}
  for lang in langs:
    tp = (results['alpha3'] == lang) & (results['detected_lang_alpha3'] == lang)
    fp = (results['alpha3'] != lang) & (results['detected_lang_alpha3'] == lang)
    tn = (results['alpha3'] != lang) & (results['detected_lang_alpha3'] != lang)
    fn = (results['alpha3'] == lang) & (results['detected_lang_alpha3'] != lang)
    precision = tp.sum() / (tp.sum() + fp.sum())
    recall = tp.sum() / (tp.sum() + fn.sum())
    class_metrics[lang] = dict(
      sentences_count=tp.sum()+fn.sum(),
      precision=precision,
      recall=recall,
      tp=tp.sum(),
      fp=fp.sum(),
      tn=tn.sum(),
      fn=fn.sum(),
    )

  stats_per_language = pd.DataFrame.from_records(data=list(class_metrics.values()), index=list(class_metrics.keys()))
  stats_per_language.index.name = 'language_alpha3'
  stats_per_language = stats_per_language.reset_index()

  # assign the language
  stats_per_language['language'] = stats_per_language['language_alpha3'].apply(dataset_analysis.get_language_name)

  # sort by sentences count and set the index to be row number
  stats_per_language.sort_values(['sentences_count'], ascending=False, inplace=True)
  stats_per_language = stats_per_language.reset_index()
  stats_per_language.index += 1

  return stats_per_language[['language_alpha3', 'language', 'sentences_count', 'precision', 'recall', 'tp', 'fp', 'tn', 'fn']]


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Write aggregated results files.')
  parser.add_argument('--dataset', '-d', type=str, default='tatoeba-sentences-2021-06-05')
  parser.add_argument('--timings_prefix', '-t', type=str, default='', help='Prefix of the times.npy file')
  parser.add_argument("--timings", type=bool, nargs='?', const=True, default=False, help='Analyze timings')
  parser.add_argument("--correctness", type=bool, nargs='?', const=True, default=False, help='Analyze correctness')
  args = parser.parse_args()

  jinja_env = Environment(loader=FileSystemLoader("./templates"), autoescape=select_autoescape())

  dataset_name = args.dataset
  timings_prefix = args.timings_prefix
  dataset = datasets.get(dataset_name)

  for benchmark_name in BENCHMARKS.keys():
    benchmark_results_path = pathlib.Path('results') / dataset_name / benchmark_name
    print()
    if not benchmark_results_path.exists():
      print(f"Skipping {benchmark_name}. Results files not found on {benchmark_results_path}")
      continue

    if args.correctness:
      print(f"Analyzing {benchmark_name} results on {dataset_name}...")

      supported_languages = BENCHMARKS[benchmark_name]['supported_languages']
      supported_languages_list_str = ", ".join(f"{lang.to_alpha3()} ({lang.display_name()})" for lang in supported_languages)

      results = read_results(dataset_name, benchmark_name, lang_dtype=dataset.dtypes['alpha3'])
      supported_langs = BENCHMARKS[benchmark_name]['supported_languages']
      dataset_subset = datasets.get_supported_dataset_subset(dataset, supported_languages=supported_langs)
      joined_results = dataset_subset.join(results)

      aggregated_accuracy = accuracy(joined_results)
      stats_per_language = get_stats_per_language(joined_results)

      # assemble the md file and write it
      tmpl = jinja_env.get_template('classification_performance.md')
      rendered = tmpl.render(
        benchmark_name=benchmark_name,
        dataset_name=dataset_name,
        dataset_len=len(dataset_subset),
        dataset_supported_pct="{:.2f}%".format(100. * len(dataset_subset) / len(dataset)),
        supported_languages_count=len(supported_languages),
        supported_languages_list_str=supported_languages_list_str,
        accuracy=aggregated_accuracy,
        stats_per_language=stats_per_language.to_markdown(floatfmt=".3f"),
      )
      results_path = os.path.join('results', dataset_name, benchmark_name, 'classification_performance.md')
      print(f"Dumping classification performance analysis to {results_path}")
      with open(results_path, 'w') as fd:
        fd.write(rendered)

    if args.timings:
      times = np.load(os.path.join('results', dataset_name, benchmark_name, f'{timings_prefix}times.npy'))
      tmpl = jinja_env.get_template('speed_performance.md')
      rendered = tmpl.render(
        benchmark_name=benchmark_name,
        dataset_name=dataset_name,
        latency_avg=np.mean(times) / 10**6,
        latency_std=np.std(times) / 10**6,
        latency_p50=np.quantile(times, [0.5])[0] / 10**6,
        latency_p90=np.quantile(times, [0.9])[0] / 10**6,
        latency_p95=np.quantile(times, [0.95])[0] / 10**6,
        latency_p99=np.quantile(times, [0.99])[0] / 10**6,
        throughput=10**9/np.mean(times),
      )
      results_path = os.path.join('results', dataset_name, benchmark_name, f'{timings_prefix}speed_performance.md')
      print(f"Dumping latency/throughput analysis to {results_path}")
      with open(results_path, 'w') as fd:
        fd.write(rendered)
