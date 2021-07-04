import pandas as pd
import numpy as np
import pycountry

import datasets
import models.fasttext
import models.gcld3
import models.langid


def get_iso_alpha3(label):
    if not label:
        return None

    if label == 'zh-cn':
      return 'cmn'

    if len(label) == 2:
        lang = pycountry.languages.get(alpha_2=label)
    else:
        lang = pycountry.languages.get(alpha_3=label)
    if lang:
        return lang.alpha_3
    return label


def read_results(dataset_name, benchmark_name='fasttext'):
  results = pd.read_csv(f'results/{dataset_name}/{benchmark_name}/results.csv', sep=',', index_col=0, names=['detected_lang', 'detected_prob'])
  results['iso_lang_code'] = results['detected_lang'].apply(lambda x: get_iso_alpha3(x.replace('__label__', '')))
  return results


def get_supported_dataset_subset(dataset, supported_languages):
  return dataset[dataset['language'].isin(supported_languages)]


def join_results(dataset, results):
  joined = dataset.join(results)
  joined['correct'] = (joined['language'] == joined['iso_lang_code']).astype(int)
  joined['incorrect'] = 1 - joined['correct']
  return joined



BENCHMARKS = {
  'fasttext': {
    'supported_languages': [get_iso_alpha3(lang) for lang in models.fasttext.SUPPORTED_LANGUAGES],
  },
  'gcld3': {
    'supported_languages': [get_iso_alpha3(lang) for lang in models.gcld3.SUPPORTED_LANGUAGES],
  },
  'langid': {
    'supported_languages': [get_iso_alpha3(lang) for lang in models.langid.SUPPORTED_LANGUAGES],
  },
}


if __name__ == "__main__":
  dataset_name = 'tatoeba-sentences-2021-06-05'
  benchmark_name = 'fasttext-compressed'

  print(f"Analyzing {benchmark_name} on {dataset_name}")
  dataset = datasets.tatoeba_2021_06_05()
  results = read_results('tatoeba-sentences-2021-06-05', benchmark_name)
  supported_langs = BENCHMARKS[benchmark_name]['supported_languages']
  dataset_subset = get_supported_dataset_subset(dataset, supported_languages=supported_langs)
  joined_results = join_results(dataset_subset, results)

  accuracy = joined_results['correct'].mean()
  print(f"Accuracy: {accuracy}")

  accuracy_per_language = joined_results.groupby('language').agg({'correct': [np.mean, 'count']})
  accuracy_per_language.columns = ['accuracy', 'datapoints']
  accuracy_per_language['datapoints'] = accuracy_per_language['datapoints'].astype(int)
  accuracy_per_language = accuracy_per_language.sort_values(['accuracy'], ascending=False)
  accuracy_per_language.to_markdown(open(f'results/{dataset_name}/{benchmark_name}/accuracy_per_language.md', 'w'), floatfmt=".3f")

  # TODO
  # confusion_matrix = pd.pivot_table(joined_results, values='incorrect', index=['language', 'iso_lang_code'], aggfunc=np.sum)

  # confusion_matrix['incorrect'].quantile([i/100 for i in itertools.chain(range(0, 90, 10), range(90, 100))])
  # confusion_matrix[confusion_matrix['incorrect'] > 600]
  # fasttext_dataset['language'] == 'hrv'
  # (fasttext_dataset['language'] == 'hrv').value_counts()
