import langdetect
import time
import numpy as np


def run(dataset, elapsed):
  lang = np.chararray(len(dataset), itemsize=10)
  prob = np.zeros((len(dataset),), dtype=np.float)

  for i, text in enumerate(dataset):
    try:
      iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
      result = langdetect.detect_langs(text)
      elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time
    except:
      result = None

    if result:
      lang[i] = result[0].lang
      prob[i] = result[0].prob
    else:
      lang[i] = 'n/a'
      prob[i] = float('nan')

  return dict(lang=lang, prob=prob)
