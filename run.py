import time
import tqdm
import numpy as np
import os
import argparse
import csv
from functools import partial

import datasets
from models import gcld3, langid, langdetect, pycld2, fasttext
from analysis import get_iso_alpha3


BENCHMARKS = {
  'fasttext': {
    'run': partial(fasttext.run, model_path=fasttext.MODEL_BIN),
    'supported_languages': [get_iso_alpha3(lang) for lang in fasttext.SUPPORTED_LANGUAGES],
  },
  'fasttext-compressed': {
    'run': partial(fasttext.run, model_path=fasttext.MODEL_COMPRESSED),
    'supported_languages': [get_iso_alpha3(lang) for lang in fasttext.SUPPORTED_LANGUAGES],
  },
  'gcld3': {
    'run': gcld3.run,
    'supported_languages': [get_iso_alpha3(lang) for lang in gcld3.SUPPORTED_LANGUAGES],
  },
  'langdetect': {
    'run': langdetect.run,
    'supported_languages': [get_iso_alpha3(lang) for lang in langdetect.SUPPORTED_LANGUAGES],
  },
  'langid': {
    'run': langid.run,
    'supported_languages': [get_iso_alpha3(lang) for lang in langid.SUPPORTED_LANGUAGES],
  },
  'pycld2': {
    'run': pycld2.run,
    'supported_languages': [get_iso_alpha3(lang) for lang in pycld2.SUPPORTED_LANGUAGES],
  },
}


def report_basic_timings(elapsed_in_fn, total_elapsed):
  spent_in_fn = np.sum(elapsed_in_fn)
  overhead = total_elapsed - spent_in_fn
  overhead_pct = overhead / spent_in_fn * 100
  avg = np.mean(elapsed_in_fn)
  std = np.std(elapsed_in_fn)
  throughput = 1/avg * 10**9
  print(f"In fn: total_time={spent_in_fn/10**9}s avg={avg}ns stddev={std}ns throughput={throughput}/s")
  print(f"Benchmark: total_time={total_elapsed/10**9} overhead: {overhead_pct}%")


def save_predictions(dst, results, original_dataset=None):
  with open(dst, mode='w') as fd:
    writer = csv.writer(fd, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for idx, lang, prob in zip(original_dataset.index, results['lang'], results['prob']):
      writer.writerow([idx, lang.decode('utf-8'), prob])


if __name__ == "__main__":
  # os.chdir(os.path.dirname(__file__))

  parser = argparse.ArgumentParser(description='Run benchmark for given model.')
  parser.add_argument('benchmarks', nargs='+')
  parser.add_argument('--examples-lo', '-lo', type=int)
  parser.add_argument('--examples-hi', '-hi', type=int)
  args = parser.parse_args()

  print('Loading big dataset...')
  dataset = datasets.tatoeba_2021_06_05()
  dataset_name = "tatoeba-sentences-2021-06-05"

  for benchmark_name in args.benchmarks:
    benchmark = BENCHMARKS[benchmark_name]
    print(f'Loaded benchmark {benchmark_name}')

    lo = args.examples_lo or 0
    hi = args.examples_hi or len(dataset)
    supported_dataset = datasets.get_supported_dataset_subset(dataset, benchmark['supported_languages'])
    print(f'Benchmark supports {len(supported_dataset)}/{len(dataset)} ({100*len(supported_dataset)/len(dataset)}%) items')
    benchmark_dataset = supported_dataset[lo:hi]
    print(f'Getting the chosen slice of the dataset (lo={lo} hi={hi}). Size={len(benchmark_dataset)}')

    print(f'Running {benchmark_name}...')
    total_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    elapsed = np.zeros((hi-lo,))
    predictions = benchmark['run'](tqdm.tqdm(benchmark_dataset.text), elapsed)

    os.makedirs(f'results/{dataset_name}/{benchmark_name}/', exist_ok=True)

    total_elapsed = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - total_start_time
    report_basic_timings(elapsed_in_fn=elapsed, total_elapsed=total_elapsed)
    np.save(f'results/{dataset_name}/{benchmark_name}/times.npy', elapsed)

    save_predictions(f'results/{dataset_name}/{benchmark_name}/results.csv', predictions, original_dataset=benchmark_dataset)
