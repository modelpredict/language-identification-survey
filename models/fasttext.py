import fasttext
import os
import time
import numpy as np

MODEL_BIN = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin'
MODEL_COMPRESSED = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz'


def run(dataset, elapsed, model_path):
  lang = np.chararray(len(dataset), itemsize=15)
  prob = np.zeros((len(dataset),), dtype=np.float)

  download_model(model_path)
  model = fasttext.load_model('/tmp/fasttext.model')

  for i, text in enumerate(dataset):
    # For some reason fasttext likes one line at a time.
    text = text.replace('\n', ' ')

    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = model.predict(text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time

    assert len(result[0]) == 1
    lang[i] = result[0][0]
    prob[i] = result[1][0]

  return dict(lang=lang, prob=prob)


def download_model(path):
  os.system(f"wget -O /tmp/fasttext.model {path}")
