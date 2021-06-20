import gcld3
import time
import numpy as np

# https://github.com/google/cld3

def run(dataset, elapsed):
  detector = gcld3.NNetLanguageIdentifier(min_num_bytes=0, max_num_bytes=3000)

  lang = np.chararray(len(dataset), itemsize=10)
  prob = np.zeros((len(dataset),), dtype=np.float)
  for i, text in enumerate(dataset):
    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = detector.FindLanguage(text=text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time

    lang[i] = result.language
    prob[i] = result.probability

  return dict(lang=lang, prob=prob)
