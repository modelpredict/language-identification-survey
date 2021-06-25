import pandas as pd
import time
import tqdm
import numpy as np
import os
import argparse
import csv
from functools import partial

import datasets
from models import gcld3, langid, langdetect, pycld2, fasttext


BENCHMARKS = {
  'langid': langid.run,
  'gcld3': gcld3.run,
  'pycld2': pycld2.run,
  'langdetect': langdetect.run,
  'fasttext': partial(fasttext.run, model_path=fasttext.MODEL_BIN),
  'fasttext-compressed': partial(fasttext.run, model_path=fasttext.MODEL_COMPRESSED),
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


def save_predictions(dst, results):
  with open(dst, mode='w') as fd:
    writer = csv.writer(fd, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for idx, lang, prob in zip(dataset.index[:n], results['lang'], results['prob']):
      writer.writerow([idx, lang.decode('utf-8'), prob])


if __name__ == "__main__":
  os.chdir(os.path.dirname(__file__))

  parser = argparse.ArgumentParser(description='Run benchmark for given model.')
  parser.add_argument('benchmarks', nargs='+')
  parser.add_argument('--examples-count', '-n', type=int)
  args = parser.parse_args()

  print('Loading dataset...')
  dataset = datasets.tatoeba_2021_06_05()

  for benchmark_name in args.benchmarks:
    benchmark = BENCHMARKS[benchmark_name]
    print(f'Loaded benchmark {benchmark_name}')

    print(f'Running {benchmark_name}...')
    total_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    n = args.examples_count or len(dataset)
    elapsed = np.zeros((n,))
    predictions = benchmark(tqdm.tqdm(dataset.text[:n]), elapsed)

    os.makedirs(f'results/{benchmark_name}/', exist_ok=True)

    total_elapsed = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - total_start_time
    report_basic_timings(elapsed_in_fn=elapsed, total_elapsed=total_elapsed)
    np.save(f'results/{benchmark_name}/times.npy', elapsed)

    save_predictions(f'results/{benchmark_name}/results.csv', predictions)
