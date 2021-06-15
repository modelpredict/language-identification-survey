import pandas as pd
import time
import tqdm
import numpy as np
import os
import argparse
from models import gcld3, langid


DATASET_PATH = 'datasets/tatoeba-sentences-2021-06-05/sentences.csv'
BENCHMARKS = {
  'langid': langid.run,
  'gcld3': gcld3.run,
}


def load_dataset(path=DATASET_PATH):
  return pd.read_csv(path, sep='\t', index_col=0, names=['language', 'text'])


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
    lang=[r.language for r in results]
    prob=[r.probability for r in results]
    result_df = pd.DataFrame(index=dataset.index[:n],data=dict(lang=lang, prob=prob))
    result_df.to_csv(dst, header=None)


if __name__ == "__main__":
  os.chdir(os.path.dirname(__file__))

  parser = argparse.ArgumentParser(description='Run benchmark for given model.')
  parser.add_argument('benchmarks', nargs='+')
  parser.add_argument('--examples-count', '-n', type=int)
  args = parser.parse_args()

  print('Loading dataset...')
  dataset = load_dataset()

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
