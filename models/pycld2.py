import pycld2
import time
import numpy as np


def get_supported_languages():
  # from https://github.com/CLD2Owners/cld2
  langs = """
  Afrikaans Albanian Arabic Armenian Azerbaijani Basque Belarusian Bengali Bihari Bulgarian Catalan Cebuano Cherokee Croatian Czech Chinese Chinese_T Danish Dhivehi Dutch English Estonian Finnish French Galician Ganda Georgian German Greek Gujarati Haitian_Creole Hebrew Hindi Hmong Hungarian Icelandic Indonesian Inuktitut Irish Italian Javanese Japanese Kannada Khmer Kinyarwanda Korean Laothian Latvian Limbu Lithuanian Macedonian Malay Malayalam Maltese Marathi Nepali Norwegian Oriya Persian Polish Portuguese Punjabi Romanian Russian Scots_Gaelic Serbian Sinhalese Slovak Slovenian Spanish Swahili Swedish Syriac Tagalog Tamil Telugu Thai Turkish Ukrainian Urdu Vietnamese Welsh Yiddish
  """.upper().strip().split(" ")
  langs.remove("CHINESE_T")
  langs.append("CHINESET")
  name_to_code = {name.upper(): code for name, code in pycld2.LANGUAGES}
  return [name_to_code[name] for name in langs]


SUPPORTED_LANGUAGES = get_supported_languages()


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
