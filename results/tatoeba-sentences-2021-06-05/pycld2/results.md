# Results for pycld2 on tatoeba-sentences-2021-06-05

- [Dataset stats](#dataset-stats)
- [Accuracy performance](#accuracy-performance)
  - [Stats per language](#stats-per-language)

## Dataset stats
|    | language_iso639_3   | language              |   sentences | dataset_percentage   |   mean_len |
|---:|:--------------------|:----------------------|------------:|:---------------------|-----------:|
|  1 | eng                 | English               |     1479733 | 20.11%               |    39.3277 |
|  2 | rus                 | Russian               |      849653 | 11.55%               |    33.4655 |
|  3 | ita                 | Italian               |      787053 | 10.70%               |    33.4897 |
|  4 | tur                 | Turkish               |      709573 | 9.64%                |    34.7355 |
|  5 | deu                 | German                |      553727 | 7.53%                |    47.4774 |
|  6 | fra                 | French                |      466192 | 6.34%                |    41.3866 |
|  7 | por                 | Portuguese            |      385737 | 5.24%                |    38.2929 |
|  8 | spa                 | Spanish               |      338781 | 4.60%                |    38.8894 |
|  9 | hun                 | Hungarian             |      323048 | 4.39%                |    34.0299 |
| 10 | jpn                 | Japanese              |      208761 | 2.84%                |    18.2659 |
| 11 | ukr                 | Ukrainian             |      171674 | 2.33%                |    27.8153 |
| 12 | nld                 | Dutch                 |      144340 | 1.96%                |    34.7853 |
| 13 | fin                 | Finnish               |      128011 | 1.74%                |    35.7946 |
| 14 | pol                 | Polish                |      109662 | 1.49%                |    33.2333 |
| 15 | mkd                 | Macedonian            |       77938 | 1.06%                |    27.3793 |
| 16 | mar                 | Marathi               |       64126 | 0.87%                |    27.587  |
| 17 | lit                 | Lithuanian            |       59659 | 0.81%                |    30.1439 |
| 18 | ces                 | Czech                 |       57030 | 0.78%                |    28.3683 |
| 19 | dan                 | Danish                |       49399 | 0.67%                |    33.7159 |
| 20 | srp                 | Serbian               |       45176 | 0.61%                |    30.4306 |
| 21 | swe                 | Swedish               |       41677 | 0.57%                |    30.1428 |
| 22 | ara                 | Arabic                |       35991 | 0.49%                |    26.7817 |
| 23 | ell                 | Modern Greek (1453-)  |       34071 | 0.46%                |    30.3915 |
| 24 | ron                 | Romanian              |       24943 | 0.34%                |    34.4097 |
| 25 | bul                 | Bulgarian             |       24503 | 0.33%                |    31.7201 |
| 26 | vie                 | Vietnamese            |       19234 | 0.26%                |    38.7891 |
| 27 | tgl                 | Tagalog               |       16649 | 0.23%                |    36.8098 |
| 28 | slk                 | Slovak                |       14660 | 0.20%                |    25.7422 |
| 29 | ind                 | Indonesian            |       14542 | 0.20%                |    37.4785 |
| 30 | hin                 | Hindi                 |       14230 | 0.19%                |    27.6058 |
| 31 | bel                 | Belarusian            |       12633 | 0.17%                |    37.3887 |
| 32 | isl                 | Icelandic             |       11091 | 0.15%                |    35.3886 |
| 33 | cat                 | Catalan               |        7971 | 0.11%                |    37.334  |
| 34 | kor                 | Korean                |        7570 | 0.10%                |    16.8085 |
| 35 | yid                 | Yiddish               |        6895 | 0.09%                |    29.8983 |
| 36 | eus                 | Basque                |        6166 | 0.08%                |    32.999  |
| 37 | kat                 | Georgian              |        5732 | 0.08%                |    26.0173 |
| 38 | aze                 | Azerbaijani           |        5348 | 0.07%                |    26.2691 |
| 39 | hrv                 | Croatian              |        5204 | 0.07%                |    30.058  |
| 40 | ben                 | Bengali               |        4714 | 0.06%                |    23.7809 |
| 41 | glg                 | Galician              |        4613 | 0.06%                |    35.8186 |
| 42 | afr                 | Afrikaans             |        4031 | 0.05%                |    29.676  |
| 43 | est                 | Estonian              |        3637 | 0.05%                |    27.6646 |
| 44 | tha                 | Thai                  |        3528 | 0.05%                |    20.5697 |
| 45 | sqi                 | Albanian              |        2526 | 0.03%                |    32.2743 |
| 46 | gle                 | Irish                 |        2389 | 0.03%                |    27.7765 |
| 47 | hye                 | Armenian              |        2248 | 0.03%                |    22.5934 |
| 48 | urd                 | Urdu                  |        2008 | 0.03%                |    30.7495 |
| 49 | khm                 | Central Khmer         |        1511 | 0.02%                |    24.2766 |
| 50 | ceb                 | Cebuano               |        1478 | 0.02%                |    32.1069 |
| 51 | cym                 | Welsh                 |        1344 | 0.02%                |    29.3058 |
| 52 | slv                 | Slovenian             |        1093 | 0.01%                |    28.4282 |
| 53 | gla                 | Scottish Gaelic       |        1033 | 0.01%                |    33.5334 |
| 54 | mal                 | Malayalam             |         827 | 0.01%                |    36.8222 |
| 55 | ori                 | Oriya (macrolanguage) |         374 | 0.01%                |    12.7567 |
| 56 | tam                 | Tamil                 |         334 | 0.00%                |    35.2784 |
| 57 | tel                 | Telugu                |         254 | 0.00%                |    28.0157 |
| 58 | lao                 | Lao                   |         219 | 0.00%                |    27.5388 |
| 59 | mlt                 | Maltese               |         208 | 0.00%                |    25.9952 |
| 60 | pan                 | Panjabi               |         196 | 0.00%                |    32.8622 |
| 61 | kan                 | Kannada               |         176 | 0.00%                |    35.3636 |
| 62 | guj                 | Gujarati              |         168 | 0.00%                |    24.244  |
| 63 | hat                 | Haitian               |          64 | 0.00%                |    22.4688 |
| 64 | sin                 | Sinhala               |          45 | 0.00%                |    22.0222 |
| 65 | chr                 | Cherokee              |          28 | 0.00%                |    11.9643 |
| 66 | kin                 | Kinyarwanda           |          28 | 0.00%                |    23.3571 |
| 67 | div                 | Dhivehi               |          26 | 0.00%                |    45.7692 |
| 68 | lug                 | Ganda                 |           2 | 0.00%                |    23.5    |

## Accuracy performance
Aggregated accuracy: **0.8703998716952872**

### Stats per language
|    | language_iso639_3   | language              |   sentences |   accuracy |
|---:|:--------------------|:----------------------|------------:|-----------:|
|  1 | eng                 | English               |     1479733 |      0.970 |
|  2 | rus                 | Russian               |      849653 |      0.830 |
|  3 | ita                 | Italian               |      787053 |      0.689 |
|  4 | tur                 | Turkish               |      709573 |      0.923 |
|  5 | deu                 | German                |      553727 |      0.954 |
|  6 | fra                 | French                |      466192 |      0.845 |
|  7 | por                 | Portuguese            |      385737 |      0.865 |
|  8 | spa                 | Spanish               |      338781 |      0.798 |
|  9 | hun                 | Hungarian             |      323048 |      0.935 |
| 10 | jpn                 | Japanese              |      208761 |      0.999 |
| 11 | ukr                 | Ukrainian             |      171674 |      0.791 |
| 12 | nld                 | Dutch                 |      144340 |      0.820 |
| 13 | fin                 | Finnish               |      128011 |      0.909 |
| 14 | pol                 | Polish                |      109662 |      0.926 |
| 15 | mkd                 | Macedonian            |       77938 |      0.477 |
| 16 | mar                 | Marathi               |       64126 |      0.967 |
| 17 | lit                 | Lithuanian            |       59659 |      0.914 |
| 18 | ces                 | Czech                 |       57030 |      0.891 |
| 19 | dan                 | Danish                |       49399 |      0.698 |
| 20 | srp                 | Serbian               |       45176 |      0.564 |
| 21 | swe                 | Swedish               |       41677 |      0.761 |
| 22 | ara                 | Arabic                |       35991 |      0.776 |
| 23 | ell                 | Modern Greek (1453-)  |       34071 |      1.000 |
| 24 | ron                 | Romanian              |       24943 |      0.811 |
| 25 | bul                 | Bulgarian             |       24503 |      0.700 |
| 26 | vie                 | Vietnamese            |       19234 |      0.991 |
| 27 | tgl                 | Tagalog               |       16649 |      0.789 |
| 28 | slk                 | Slovak                |       14660 |      0.788 |
| 29 | ind                 | Indonesian            |       14542 |      0.775 |
| 30 | hin                 | Hindi                 |       14230 |      0.973 |
| 31 | bel                 | Belarusian            |       12633 |      0.885 |
| 32 | isl                 | Icelandic             |       11091 |      0.925 |
| 33 | cat                 | Catalan               |        7971 |      0.685 |
| 34 | kor                 | Korean                |        7570 |      0.991 |
| 35 | yid                 | Yiddish               |        6895 |      0.937 |
| 36 | eus                 | Basque                |        6166 |      0.893 |
| 37 | kat                 | Georgian              |        5732 |      1.000 |
| 38 | aze                 | Azerbaijani           |        5348 |      0.870 |
| 39 | hrv                 | Croatian              |        5204 |      0.565 |
| 40 | ben                 | Bengali               |        4714 |      0.777 |
| 41 | glg                 | Galician              |        4613 |      0.668 |
| 42 | afr                 | Afrikaans             |        4031 |      0.826 |
| 43 | est                 | Estonian              |        3637 |      0.752 |
| 44 | tha                 | Thai                  |        3528 |      1.000 |
| 45 | sqi                 | Albanian              |        2526 |      0.909 |
| 46 | gle                 | Irish                 |        2389 |      0.884 |
| 47 | hye                 | Armenian              |        2248 |      1.000 |
| 48 | urd                 | Urdu                  |        2008 |      0.948 |
| 49 | khm                 | Central Khmer         |        1511 |      0.991 |
| 50 | ceb                 | Cebuano               |        1478 |      0.551 |
| 51 | cym                 | Welsh                 |        1344 |      0.845 |
| 52 | slv                 | Slovenian             |        1093 |      0.550 |
| 53 | gla                 | Scottish Gaelic       |        1033 |      0.909 |
| 54 | mal                 | Malayalam             |         827 |      1.000 |
| 55 | ori                 | Oriya (macrolanguage) |         374 |      1.000 |
| 56 | tam                 | Tamil                 |         334 |      1.000 |
| 57 | tel                 | Telugu                |         254 |      1.000 |
| 58 | lao                 | Lao                   |         219 |      1.000 |
| 59 | mlt                 | Maltese               |         208 |      0.803 |
| 60 | pan                 | Panjabi               |         196 |      1.000 |
| 61 | kan                 | Kannada               |         176 |      1.000 |
| 62 | guj                 | Gujarati              |         168 |      1.000 |
| 63 | hat                 | Haitian               |          64 |      0.594 |
| 64 | sin                 | Sinhala               |          45 |      1.000 |
| 65 | chr                 | Cherokee              |          28 |      0.964 |
| 66 | kin                 | Kinyarwanda           |          28 |      0.679 |
| 67 | div                 | Dhivehi               |          26 |      1.000 |
| 68 | lug                 | Ganda                 |           2 |      1.000 |