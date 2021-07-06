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

  # calculate stats (count, pct, mean(text_len)) per language, sorted by count DESC
  counts = ds.groupby('language').agg({'text_len': ['count', 'mean']}).drop(r"\N").reset_index()
  counts.columns = ['language_iso639_3', 'sentences', 'mean_len']
  counts['dataset_percentage'] = (counts['sentences'] / counts['sentences'].sum() * 100).apply(lambda x: "{:.2f}%".format(x))
  counts.sort_values(['sentences'], ascending=False, inplace=True)
  counts.reset_index(inplace=True)
  counts.index += 1

  # assign language name
  counts['language'] = counts['language_iso639_3'].apply(get_language_name)

  with open(os.path.join('datasets', DATASET_NAME, 'stats.md'), 'w') as fd:
    view = counts[['language_iso639_3', 'language', 'sentences', 'dataset_percentage', 'mean_len']]
    view.to_markdown(fd, index=True)
