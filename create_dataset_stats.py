import iso639
import os
import datasets


DATASET_NAME = "tatoeba-sentences-2021-06-05"


def get_language_name(alpha3):
    properties = ['part1','part2b', 'part2t', 'part3', 'part5','retired']
    for prop in properties:
        if alpha3 in getattr(iso639.languages, prop):
            lang = getattr(iso639.languages, prop)[alpha3]
            return lang.name
    return "--"


if __name__ == "__main__":
  print(f"Dumping stats for dataset {DATASET_NAME}")

  ds = datasets.tatoeba_2021_06_05()
  ds['text_len'] = ds['text'].str.len()

  counts = ds.groupby('language').agg({'text_len': ['count', 'mean']}).drop(r"\N").reset_index()
  counts.columns = ['language_iso639_3', 'sentences', 'mean_len']
  counts.sort_values(['sentences'], ascending=False, inplace=True)
  counts['language'] = counts['language_iso639_3'].apply(get_language_name)
  counts['pct'] = (counts['sentences'] / counts['sentences'].sum() * 100).apply(lambda x: "{:.2f}%".format(x))

  with open(os.path.join('datasets', DATASET_NAME, 'stats.md'), 'w') as fd:
    view = counts[['language_iso639_3', 'language', 'sentences', 'pct', 'mean_len']]
    view.to_markdown(fd, index=False)
