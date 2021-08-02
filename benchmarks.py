from functools import partial

from langcodes import Language
from models import gcld3, langid, langdetect, pycld2, fasttext


BENCHMARKS = {
  'fasttext': {
    'run': partial(fasttext.run, model_path=fasttext.MODEL_BIN),
    'measure_memory': partial(fasttext.measure_memory, model_path=fasttext.MODEL_BIN),
    'supported_languages': [Language.get(lang).to_alpha3() for lang in fasttext.SUPPORTED_LANGUAGES],
  },
  'fasttext-compressed': {
    'run': partial(fasttext.run, model_path=fasttext.MODEL_COMPRESSED),
    'measure_memory': partial(fasttext.measure_memory, model_path=fasttext.MODEL_COMPRESSED),
    'supported_languages': [Language.get(lang).to_alpha3() for lang in fasttext.SUPPORTED_LANGUAGES],
  },
  'gcld3': {
    'run': gcld3.run,
    'measure_memory': gcld3.measure_memory,
    'supported_languages': [Language.get(lang).to_alpha3() for lang in gcld3.SUPPORTED_LANGUAGES],
  },
  'langdetect': {
    'run': langdetect.run,
    'measure_memory': langdetect.measure_memory,
    'supported_languages': [Language.get(lang).to_alpha3() for lang in langdetect.SUPPORTED_LANGUAGES],
  },
  'langid': {
    'run': langid.run,
    'measure_memory': langid.measure_memory,
    'supported_languages': [Language.get(lang).to_alpha3() for lang in langid.SUPPORTED_LANGUAGES],
  },
  'pycld2': {
    'run': pycld2.run,
    'measure_memory': pycld2.measure_memory,
    'supported_languages': [Language.get(lang).to_alpha3() for lang in pycld2.SUPPORTED_LANGUAGES],
  },
}


def common_languages():
  supported_languages = set(BENCHMARKS['fasttext']['supported_languages'])
  for b in BENCHMARKS:
    supported_languages = supported_languages.intersection(BENCHMARKS[b]['supported_languages'])
  return supported_languages
