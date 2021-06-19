import gcld3
import time

detector = None

# https://github.com/google/cld3

def run(dataset, elapsed):
  detector = gcld3.NNetLanguageIdentifier(min_num_bytes=0, max_num_bytes=3000)
  results = []

  for i, text in enumerate(dataset):
    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = detector.FindLanguage(text=text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time
    results.append(result)

  return results
