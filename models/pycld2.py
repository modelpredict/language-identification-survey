import pycld2
import time
import numpy as np

def run(dataset, elapsed):
  lang = np.chararray(len(dataset), itemsize=10)
  prob = np.zeros((len(dataset),), dtype=np.float)

  for i, text in enumerate(dataset):
    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = pycld2.detect(text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time

    lang[i] = result[2][0][1]
    prob[i] = float('nan')

  return dict(lang=lang, prob=prob)
