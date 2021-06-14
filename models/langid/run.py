import langid
import pandas as pd
import time
import tqdm
import numpy as np
import os

os.chdir(os.path.dirname(__file__))

# setup
dataset = pd.read_csv('data/sentences.csv', sep='\t', index_col=0, names=['language', 'text'])

# benchmark
total_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
results = []
n = len(dataset)
elapsed = np.zeros((n,))
for i, text in enumerate(tqdm.tqdm(dataset.text[:n])):
  iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
  result = langid.classify(text)
  elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time

  results.append(result)

# reporting
total_elapsed = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - total_start_time
spent_in_fn = np.sum(elapsed)
overhead = total_elapsed - spent_in_fn
overhead_pct = overhead / spent_in_fn * 100
avg = np.mean(elapsed)
std = np.std(elapsed)
throughput = 1/avg * 10**9
print(f"In fn: total_time={spent_in_fn/10**9}s avg={avg}ns stddev={std}ns throughput={throughput}/s")
print(f"Benchmark: total_time={total_elapsed/10**9} overhead: {overhead_pct}%")

# saving results
lang=[r.language for r in results]
prob=[r.probability for r in results]
result_df = pd.DataFrame(index=dataset.index[:n],data=dict(lang=lang, prob=prob))
result_df.to_csv('results.csv', header=None)
np.save('times.npy', elapsed)
