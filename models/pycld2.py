import pycld2
import time
from collections import namedtuple

Result = namedtuple('res', ['language', 'probability'])

def run(dataset, elapsed):
  results = []

  for i, text in enumerate(dataset):
    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = pycld2.detect(text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time
    results.append(result)

  return convert_results(results)


def convert_results(results):
  converted = []
  for r in results:
    best_lang = r[2][0]
    converted.append(Result(best_lang[1], None))
  return converted
