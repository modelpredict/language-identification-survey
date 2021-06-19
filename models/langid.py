import langid
import time
from collections import namedtuple

Result = namedtuple('res', ['language', 'probability'])


def run(dataset, elapsed):
  results = []

  for i, text in enumerate(dataset):
    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = langid.classify(text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time
    results.append(result)

  return convert_results(results)


def convert_results(results):
  converted = []
  for r in results:
    converted.append(Result(r[0], r[1]))
  return converted
