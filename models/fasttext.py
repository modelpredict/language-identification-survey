import fasttext
import os
import time
from collections import namedtuple

Result = namedtuple('res', ['language', 'probability'])

MODEL_BIN = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin'
MODEL_COMPRESSED = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz'


def run(dataset, elapsed, model_path):
  results = []

  download_model(model_path)
  model = fasttext.load_model('/tmp/fasttext.model')

  for i, text in enumerate(dataset):
    # For some reason fasttext likes one line at a time.
    text = text.replace('\n', ' ')

    iter_start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
    result = model.predict(text)
    elapsed[i] = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - iter_start_time
    results.append(result)

  return convert_results(results)


def convert_results(results):
  converted = []
  for r in results:
    langs, probs = r
    assert len(langs) == 1
    converted.append(Result(langs[0].replace("__label__", ""), probs[0]))
  return converted


def download_model(path):
  os.system(f"wget -O /tmp/fasttext.model {path}")
