from functools import partial
from models import gcld3, langid, langdetect, pycld2, fasttext
from langtools import get_iso_alpha3


BENCHMARKS = {
  'fasttext': {
    'run': partial(fasttext.run, model_path=fasttext.MODEL_BIN),
    'measure_memory': partial(fasttext.measure_memory, model_path=fasttext.MODEL_BIN),
    'supported_languages': [get_iso_alpha3(lang) for lang in fasttext.SUPPORTED_LANGUAGES],
    'supported_languages_raw': fasttext.SUPPORTED_LANGUAGES,
  },
  'fasttext-compressed': {
    'run': partial(fasttext.run, model_path=fasttext.MODEL_COMPRESSED),
    'measure_memory': partial(fasttext.measure_memory, model_path=fasttext.MODEL_COMPRESSED),
    'supported_languages': [get_iso_alpha3(lang) for lang in fasttext.SUPPORTED_LANGUAGES],
    'supported_languages_raw': fasttext.SUPPORTED_LANGUAGES,
  },
  'gcld3': {
    'run': gcld3.run,
    'measure_memory': gcld3.measure_memory,
    'supported_languages': [get_iso_alpha3(lang) for lang in gcld3.SUPPORTED_LANGUAGES],
    'supported_languages_raw': gcld3.SUPPORTED_LANGUAGES,
  },
  'langdetect': {
    'run': langdetect.run,
    'measure_memory': langdetect.measure_memory,
    'supported_languages': [get_iso_alpha3(lang) for lang in langdetect.SUPPORTED_LANGUAGES],
    'supported_languages_raw': langdetect.SUPPORTED_LANGUAGES,
  },
  'langid': {
    'run': langid.run,
    'measure_memory': langid.measure_memory,
    'supported_languages': [get_iso_alpha3(lang) for lang in langid.SUPPORTED_LANGUAGES],
    'supported_languages_raw': langid.SUPPORTED_LANGUAGES,
  },
  'pycld2': {
    'run': pycld2.run,
    'measure_memory': pycld2.measure_memory,
    'supported_languages': [get_iso_alpha3(lang) for lang in pycld2.SUPPORTED_LANGUAGES],
    'supported_languages_raw': pycld2.SUPPORTED_LANGUAGES,
  },
}

