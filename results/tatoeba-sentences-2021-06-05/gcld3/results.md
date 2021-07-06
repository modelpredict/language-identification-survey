# Results for gcld3 on tatoeba-sentences-2021-06-05

- [Dataset stats](#dataset-stats)
- [Accuracy performance](#accuracy-performance)
  - [Stats per language](#stats-per-language)

## Dataset stats
|    | language_iso639_3   | language             |   sentences | dataset_percentage   |   mean_len |
|---:|:--------------------|:---------------------|------------:|:---------------------|-----------:|
|  1 | eng                 | English              |     1479733 | 18.42%               |    39.3277 |
|  2 | rus                 | Russian              |      849653 | 10.58%               |    33.4655 |
|  3 | ita                 | Italian              |      787053 | 9.80%                |    33.4897 |
|  4 | tur                 | Turkish              |      709573 | 8.83%                |    34.7355 |
|  5 | epo                 | Esperanto            |      659632 | 8.21%                |    40.3975 |
|  6 | deu                 | German               |      553727 | 6.89%                |    47.4774 |
|  7 | fra                 | French               |      466192 | 5.80%                |    41.3866 |
|  8 | por                 | Portuguese           |      385737 | 4.80%                |    38.2929 |
|  9 | spa                 | Spanish              |      338781 | 4.22%                |    38.8894 |
| 10 | hun                 | Hungarian            |      323048 | 4.02%                |    34.0299 |
| 11 | jpn                 | Japanese             |      208761 | 2.60%                |    18.2659 |
| 12 | ukr                 | Ukrainian            |      171674 | 2.14%                |    27.8153 |
| 13 | nld                 | Dutch                |      144340 | 1.80%                |    34.7853 |
| 14 | fin                 | Finnish              |      128011 | 1.59%                |    35.7946 |
| 15 | pol                 | Polish               |      109662 | 1.37%                |    33.2333 |
| 16 | mkd                 | Macedonian           |       77938 | 0.97%                |    27.3793 |
| 17 | mar                 | Marathi              |       64126 | 0.80%                |    27.587  |
| 18 | lit                 | Lithuanian           |       59659 | 0.74%                |    30.1439 |
| 19 | ces                 | Czech                |       57030 | 0.71%                |    28.3683 |
| 20 | dan                 | Danish               |       49399 | 0.61%                |    33.7159 |
| 21 | srp                 | Serbian              |       45176 | 0.56%                |    30.4306 |
| 22 | swe                 | Swedish              |       41677 | 0.52%                |    30.1428 |
| 23 | lat                 | Latin                |       39718 | 0.49%                |    36.1448 |
| 24 | ara                 | Arabic               |       35991 | 0.45%                |    26.7817 |
| 25 | ell                 | Modern Greek (1453-) |       34071 | 0.42%                |    30.3915 |
| 26 | ron                 | Romanian             |       24943 | 0.31%                |    34.4097 |
| 27 | bul                 | Bulgarian            |       24503 | 0.31%                |    31.7201 |
| 28 | vie                 | Vietnamese           |       19234 | 0.24%                |    38.7891 |
| 29 | slk                 | Slovak               |       14660 | 0.18%                |    25.7422 |
| 30 | ind                 | Indonesian           |       14542 | 0.18%                |    37.4785 |
| 31 | hin                 | Hindi                |       14230 | 0.18%                |    27.6058 |
| 32 | isl                 | Icelandic            |       11091 | 0.14%                |    35.3886 |
| 33 | cat                 | Catalan              |        7971 | 0.10%                |    37.334  |
| 34 | kor                 | Korean               |        7570 | 0.09%                |    16.8085 |
| 35 | yid                 | Yiddish              |        6895 | 0.09%                |    29.8983 |
| 36 | eus                 | Basque               |        6166 | 0.08%                |    32.999  |
| 37 | kat                 | Georgian             |        5732 | 0.07%                |    26.0173 |
| 38 | hrv                 | Croatian             |        5204 | 0.06%                |    30.058  |
| 39 | ben                 | Bengali              |        4714 | 0.06%                |    23.7809 |
| 40 | glg                 | Galician             |        4613 | 0.06%                |    35.8186 |
| 41 | afr                 | Afrikaans            |        4031 | 0.05%                |    29.676  |
| 42 | kaz                 | Kazakh               |        3685 | 0.05%                |    49.9183 |
| 43 | est                 | Estonian             |        3637 | 0.05%                |    27.6646 |
| 44 | tha                 | Thai                 |        3528 | 0.04%                |    20.5697 |
| 45 | mon                 | Mongolian            |        2757 | 0.03%                |    30.9387 |
| 46 | sqi                 | Albanian             |        2526 | 0.03%                |    32.2743 |
| 47 | gle                 | Irish                |        2389 | 0.03%                |    27.7765 |
| 48 | hye                 | Armenian             |        2248 | 0.03%                |    22.5934 |
| 49 | urd                 | Urdu                 |        2008 | 0.02%                |    30.7495 |
| 50 | khm                 | Central Khmer        |        1511 | 0.02%                |    24.2766 |
| 51 | ceb                 | Cebuano              |        1478 | 0.02%                |    32.1069 |
| 52 | cym                 | Welsh                |        1344 | 0.02%                |    29.3058 |
| 53 | slv                 | Slovenian            |        1093 | 0.01%                |    28.4282 |
| 54 | gla                 | Scottish Gaelic      |        1033 | 0.01%                |    33.5334 |
| 55 | uzb                 | Uzbek                |         855 | 0.01%                |    25.9813 |
| 56 | mal                 | Malayalam            |         827 | 0.01%                |    36.8222 |
| 57 | ltz                 | Luxembourgish        |         805 | 0.01%                |    25.4099 |
| 58 | jav                 | Javanese             |         615 | 0.01%                |    28.7333 |
| 59 | bos                 | Bosnian              |         567 | 0.01%                |    23.3492 |
| 60 | mya                 | Burmese              |         433 | 0.01%                |    33.5219 |
| 61 | mri                 | Maori                |         388 | 0.00%                |    39.1186 |
| 62 | fry                 | Western Frisian      |         355 | 0.00%                |    28.569  |
| 63 | tam                 | Tamil                |         334 | 0.00%                |    35.2784 |
| 64 | tel                 | Telugu               |         254 | 0.00%                |    28.0157 |
| 65 | kir                 | Kirghiz              |         254 | 0.00%                |    23.8504 |
| 66 | xho                 | Xhosa                |         252 | 0.00%                |    28.369  |
| 67 | lao                 | Lao                  |         219 | 0.00%                |    27.5388 |
| 68 | amh                 | Amharic              |         211 | 0.00%                |    12.7867 |
| 69 | mlt                 | Maltese              |         208 | 0.00%                |    25.9952 |
| 70 | pan                 | Panjabi              |         196 | 0.00%                |    32.8622 |
| 71 | kan                 | Kannada              |         176 | 0.00%                |    35.3636 |
| 72 | guj                 | Gujarati             |         168 | 0.00%                |    24.244  |
| 73 | haw                 | Hawaiian             |         155 | 0.00%                |    23.5226 |
| 74 | som                 | Somali               |          80 | 0.00%                |    30.025  |
| 75 | zul                 | Zulu                 |          77 | 0.00%                |    30.4156 |
| 76 | smo                 | Samoan               |          76 | 0.00%                |    21.4342 |
| 77 | hat                 | Haitian              |          64 | 0.00%                |    22.4688 |
| 78 | tgk                 | Tajik                |          63 | 0.00%                |    31.4603 |
| 79 | hau                 | Hausa                |          60 | 0.00%                |    31.4833 |
| 80 | mlg                 | Malagasy             |          59 | 0.00%                |    21.0339 |
| 81 | sin                 | Sinhala              |          45 | 0.00%                |    22.0222 |
| 82 | pus                 | Pushto               |          44 | 0.00%                |    35.9318 |
| 83 | sna                 | Shona                |          42 | 0.00%                |    20.5952 |
| 84 | yor                 | Yoruba               |          37 | 0.00%                |    23.2973 |
| 85 | ibo                 | Igbo                 |          32 | 0.00%                |    20.0938 |
| 86 | sun                 | Sundanese            |          31 | 0.00%                |    25.7742 |
| 87 | cos                 | Corsican             |          24 | 0.00%                |    20.1667 |
| 88 | nya                 | Nyanja               |          24 | 0.00%                |    23.375  |
| 89 | snd                 | Sindhi               |           6 | 0.00%                |    22.3333 |
| 90 | sot                 | Southern Sotho       |           2 | 0.00%                |    66.5    |

## Accuracy performance
Aggregated accuracy: **0.8684251013476171**

### Stats per language
|    | language_iso639_3   | language             |   sentences |   accuracy |
|---:|:--------------------|:---------------------|------------:|-----------:|
|  1 | eng                 | English              |     1479733 |      0.851 |
|  2 | rus                 | Russian              |      849653 |      0.858 |
|  3 | ita                 | Italian              |      787053 |      0.821 |
|  4 | tur                 | Turkish              |      709573 |      0.894 |
|  5 | epo                 | Esperanto            |      659632 |      0.922 |
|  6 | deu                 | German               |      553727 |      0.933 |
|  7 | fra                 | French               |      466192 |      0.860 |
|  8 | por                 | Portuguese           |      385737 |      0.885 |
|  9 | spa                 | Spanish              |      338781 |      0.782 |
| 10 | hun                 | Hungarian            |      323048 |      0.895 |
| 11 | jpn                 | Japanese             |      208761 |      0.999 |
| 12 | ukr                 | Ukrainian            |      171674 |      0.889 |
| 13 | nld                 | Dutch                |      144340 |      0.854 |
| 14 | fin                 | Finnish              |      128011 |      0.902 |
| 15 | pol                 | Polish               |      109662 |      0.931 |
| 16 | mkd                 | Macedonian           |       77938 |      0.741 |
| 17 | mar                 | Marathi              |       64126 |      0.911 |
| 18 | lit                 | Lithuanian           |       59659 |      0.883 |
| 19 | ces                 | Czech                |       57030 |      0.813 |
| 20 | dan                 | Danish               |       49399 |      0.746 |
| 21 | srp                 | Serbian              |       45176 |      0.449 |
| 22 | swe                 | Swedish              |       41677 |      0.861 |
| 23 | lat                 | Latin                |       39718 |      0.729 |
| 24 | ara                 | Arabic               |       35991 |      0.911 |
| 25 | ell                 | Modern Greek (1453-) |       34071 |      1.000 |
| 26 | ron                 | Romanian             |       24943 |      0.808 |
| 27 | bul                 | Bulgarian            |       24503 |      0.844 |
| 28 | vie                 | Vietnamese           |       19234 |      0.981 |
| 29 | slk                 | Slovak               |       14660 |      0.727 |
| 30 | ind                 | Indonesian           |       14542 |      0.640 |
| 31 | hin                 | Hindi                |       14230 |      0.880 |
| 32 | isl                 | Icelandic            |       11091 |      0.945 |
| 33 | cat                 | Catalan              |        7971 |      0.818 |
| 34 | kor                 | Korean               |        7570 |      0.996 |
| 35 | yid                 | Yiddish              |        6895 |      0.944 |
| 36 | eus                 | Basque               |        6166 |      0.861 |
| 37 | kat                 | Georgian             |        5732 |      0.998 |
| 38 | hrv                 | Croatian             |        5204 |      0.447 |
| 39 | ben                 | Bengali              |        4714 |      0.998 |
| 40 | glg                 | Galician             |        4613 |      0.774 |
| 41 | afr                 | Afrikaans            |        4031 |      0.865 |
| 42 | kaz                 | Kazakh               |        3685 |      0.932 |
| 43 | est                 | Estonian             |        3637 |      0.796 |
| 44 | tha                 | Thai                 |        3528 |      0.998 |
| 45 | mon                 | Mongolian            |        2757 |      0.955 |
| 46 | sqi                 | Albanian             |        2526 |      0.865 |
| 47 | gle                 | Irish                |        2389 |      0.911 |
| 48 | hye                 | Armenian             |        2248 |      0.998 |
| 49 | urd                 | Urdu                 |        2008 |      0.961 |
| 50 | khm                 | Central Khmer        |        1511 |      0.985 |
| 51 | ceb                 | Cebuano              |        1478 |      0.571 |
| 52 | cym                 | Welsh                |        1344 |      0.824 |
| 53 | slv                 | Slovenian            |        1093 |      0.724 |
| 54 | gla                 | Scottish Gaelic      |        1033 |      0.867 |
| 55 | uzb                 | Uzbek                |         855 |      0.581 |
| 56 | mal                 | Malayalam            |         827 |      1.000 |
| 57 | ltz                 | Luxembourgish        |         805 |      0.867 |
| 58 | jav                 | Javanese             |         615 |      0.361 |
| 59 | bos                 | Bosnian              |         567 |      0.388 |
| 60 | mya                 | Burmese              |         433 |      1.000 |
| 61 | mri                 | Maori                |         388 |      0.711 |
| 62 | fry                 | Western Frisian      |         355 |      0.738 |
| 63 | tam                 | Tamil                |         334 |      1.000 |
| 64 | tel                 | Telugu               |         254 |      1.000 |
| 65 | kir                 | Kirghiz              |         254 |      0.878 |
| 66 | xho                 | Xhosa                |         252 |      0.683 |
| 67 | lao                 | Lao                  |         219 |      1.000 |
| 68 | amh                 | Amharic              |         211 |      0.991 |
| 69 | mlt                 | Maltese              |         208 |      0.817 |
| 70 | pan                 | Panjabi              |         196 |      0.995 |
| 71 | kan                 | Kannada              |         176 |      1.000 |
| 72 | guj                 | Gujarati             |         168 |      0.982 |
| 73 | haw                 | Hawaiian             |         155 |      0.839 |
| 74 | som                 | Somali               |          80 |      0.912 |
| 75 | zul                 | Zulu                 |          77 |      0.753 |
| 76 | smo                 | Samoan               |          76 |      0.763 |
| 77 | hat                 | Haitian              |          64 |      0.797 |
| 78 | tgk                 | Tajik                |          63 |      0.889 |
| 79 | hau                 | Hausa                |          60 |      0.800 |
| 80 | mlg                 | Malagasy             |          59 |      0.831 |
| 81 | sin                 | Sinhala              |          45 |      1.000 |
| 82 | pus                 | Pushto               |          44 |      0.864 |
| 83 | sna                 | Shona                |          42 |      0.667 |
| 84 | yor                 | Yoruba               |          37 |      0.108 |
| 85 | ibo                 | Igbo                 |          32 |      0.688 |
| 86 | sun                 | Sundanese            |          31 |      0.548 |
| 87 | cos                 | Corsican             |          24 |      0.583 |
| 88 | nya                 | Nyanja               |          24 |      0.833 |
| 89 | snd                 | Sindhi               |           6 |      0.833 |
| 90 | sot                 | Southern Sotho       |           2 |      1.000 |