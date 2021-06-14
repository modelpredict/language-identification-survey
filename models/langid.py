import langid
import time

detector = None

def run(dataset, elapsed):
  results = []

  for i, text in enumerate(dataset):
    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = langid.classify(text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time
    results.append(result)

  return results
