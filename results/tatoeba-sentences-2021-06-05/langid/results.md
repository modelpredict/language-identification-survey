# Results for langid on tatoeba-sentences-2021-06-05

- [Dataset stats](#dataset-stats)
- [Accuracy performance](#accuracy-performance)
  - [Stats per language](#stats-per-language)

## Dataset stats
|    | language_iso639_3   | language              |   sentences | dataset_percentage   |   mean_len |
|---:|:--------------------|:----------------------|------------:|:---------------------|-----------:|
|  1 | eng                 | English               |     1479733 | 17.83%               |    39.3277 |
|  2 | rus                 | Russian               |      849653 | 10.24%               |    33.4655 |
|  3 | ita                 | Italian               |      787053 | 9.48%                |    33.4897 |
|  4 | tur                 | Turkish               |      709573 | 8.55%                |    34.7355 |
|  5 | epo                 | Esperanto             |      659632 | 7.95%                |    40.3975 |
|  6 | deu                 | German                |      553727 | 6.67%                |    47.4774 |
|  7 | fra                 | French                |      466192 | 5.62%                |    41.3866 |
|  8 | por                 | Portuguese            |      385737 | 4.65%                |    38.2929 |
|  9 | spa                 | Spanish               |      338781 | 4.08%                |    38.8894 |
| 10 | hun                 | Hungarian             |      323048 | 3.89%                |    34.0299 |
| 11 | jpn                 | Japanese              |      208761 | 2.52%                |    18.2659 |
| 12 | heb                 | Hebrew                |      197226 | 2.38%                |    25.5678 |
| 13 | ukr                 | Ukrainian             |      171674 | 2.07%                |    27.8153 |
| 14 | nld                 | Dutch                 |      144340 | 1.74%                |    34.7853 |
| 15 | fin                 | Finnish               |      128011 | 1.54%                |    35.7946 |
| 16 | pol                 | Polish                |      109662 | 1.32%                |    33.2333 |
| 17 | mkd                 | Macedonian            |       77938 | 0.94%                |    27.3793 |
| 18 | mar                 | Marathi               |       64126 | 0.77%                |    27.587  |
| 19 | lit                 | Lithuanian            |       59659 | 0.72%                |    30.1439 |
| 20 | ces                 | Czech                 |       57030 | 0.69%                |    28.3683 |
| 21 | dan                 | Danish                |       49399 | 0.60%                |    33.7159 |
| 22 | srp                 | Serbian               |       45176 | 0.54%                |    30.4306 |
| 23 | swe                 | Swedish               |       41677 | 0.50%                |    30.1428 |
| 24 | lat                 | Latin                 |       39718 | 0.48%                |    36.1448 |
| 25 | ara                 | Arabic                |       35991 | 0.43%                |    26.7817 |
| 26 | ell                 | Modern Greek (1453-)  |       34071 | 0.41%                |    30.3915 |
| 27 | ron                 | Romanian              |       24943 | 0.30%                |    34.4097 |
| 28 | bul                 | Bulgarian             |       24503 | 0.30%                |    31.7201 |
| 29 | vie                 | Vietnamese            |       19234 | 0.23%                |    38.7891 |
| 30 | tgl                 | Tagalog               |       16649 | 0.20%                |    36.8098 |
| 31 | slk                 | Slovak                |       14660 | 0.18%                |    25.7422 |
| 32 | ind                 | Indonesian            |       14542 | 0.18%                |    37.4785 |
| 33 | hin                 | Hindi                 |       14230 | 0.17%                |    27.6058 |
| 34 | nob                 | Norwegian Bokmål      |       14223 | 0.17%                |    37.4732 |
| 35 | bel                 | Belarusian            |       12633 | 0.15%                |    37.3887 |
| 36 | isl                 | Icelandic             |       11091 | 0.13%                |    35.3886 |
| 37 | cat                 | Catalan               |        7971 | 0.10%                |    37.334  |
| 38 | uig                 | Uighur                |        7792 | 0.09%                |    31.1084 |
| 39 | kor                 | Korean                |        7570 | 0.09%                |    16.8085 |
| 40 | bre                 | Breton                |        7195 | 0.09%                |    27.4111 |
| 41 | eus                 | Basque                |        6166 | 0.07%                |    32.999  |
| 42 | kat                 | Georgian              |        5732 | 0.07%                |    26.0173 |
| 43 | oci                 | Occitan (post 1500)   |        5693 | 0.07%                |    32.3931 |
| 44 | aze                 | Azerbaijani           |        5348 | 0.06%                |    26.2691 |
| 45 | hrv                 | Croatian              |        5204 | 0.06%                |    30.058  |
| 46 | ben                 | Bengali               |        4714 | 0.06%                |    23.7809 |
| 47 | glg                 | Galician              |        4613 | 0.06%                |    35.8186 |
| 48 | vol                 | Volapük               |        4132 | 0.05%                |    23.3129 |
| 49 | afr                 | Afrikaans             |        4031 | 0.05%                |    29.676  |
| 50 | kaz                 | Kazakh                |        3685 | 0.04%                |    49.9183 |
| 51 | est                 | Estonian              |        3637 | 0.04%                |    27.6646 |
| 52 | tha                 | Thai                  |        3528 | 0.04%                |    20.5697 |
| 53 | asm                 | Assamese              |        2912 | 0.04%                |    24.1006 |
| 54 | mon                 | Mongolian             |        2757 | 0.03%                |    30.9387 |
| 55 | sqi                 | Albanian              |        2526 | 0.03%                |    32.2743 |
| 56 | gle                 | Irish                 |        2389 | 0.03%                |    27.7765 |
| 57 | hye                 | Armenian              |        2248 | 0.03%                |    22.5934 |
| 58 | urd                 | Urdu                  |        2008 | 0.02%                |    30.7495 |
| 59 | nno                 | Norwegian Nynorsk     |        1576 | 0.02%                |    30.8249 |
| 60 | khm                 | Central Khmer         |        1511 | 0.02%                |    24.2766 |
| 61 | cym                 | Welsh                 |        1344 | 0.02%                |    29.3058 |
| 62 | slv                 | Slovenian             |        1093 | 0.01%                |    28.4282 |
| 63 | mal                 | Malayalam             |         827 | 0.01%                |    36.8222 |
| 64 | ltz                 | Luxembourgish         |         805 | 0.01%                |    25.4099 |
| 65 | jav                 | Javanese              |         615 | 0.01%                |    28.7333 |
| 66 | bos                 | Bosnian               |         567 | 0.01%                |    23.3492 |
| 67 | que                 | Quechua               |         422 | 0.01%                |    25.6588 |
| 68 | fao                 | Faroese               |         402 | 0.00%                |    28.6119 |
| 69 | ori                 | Oriya (macrolanguage) |         374 | 0.00%                |    12.7567 |
| 70 | tam                 | Tamil                 |         334 | 0.00%                |    35.2784 |
| 71 | tel                 | Telugu                |         254 | 0.00%                |    28.0157 |
| 72 | kir                 | Kirghiz               |         254 | 0.00%                |    23.8504 |
| 73 | xho                 | Xhosa                 |         252 | 0.00%                |    28.369  |
| 74 | lao                 | Lao                   |         219 | 0.00%                |    27.5388 |
| 75 | amh                 | Amharic               |         211 | 0.00%                |    12.7867 |
| 76 | mlt                 | Maltese               |         208 | 0.00%                |    25.9952 |
| 77 | pan                 | Panjabi               |         196 | 0.00%                |    32.8622 |
| 78 | sme                 | Northern Sami         |         181 | 0.00%                |    20.0884 |
| 79 | kan                 | Kannada               |         176 | 0.00%                |    35.3636 |
| 80 | guj                 | Gujarati              |         168 | 0.00%                |    24.244  |
| 81 | arg                 | Aragonese             |         103 | 0.00%                |    15.9515 |
| 82 | zul                 | Zulu                  |          77 | 0.00%                |    30.4156 |
| 83 | hat                 | Haitian               |          64 | 0.00%                |    22.4688 |
| 84 | mlg                 | Malagasy              |          59 | 0.00%                |    21.0339 |
| 85 | wln                 | Walloon               |          53 | 0.00%                |    28.2642 |
| 86 | sin                 | Sinhala               |          45 | 0.00%                |    22.0222 |
| 87 | pus                 | Pushto                |          44 | 0.00%                |    35.9318 |
| 88 | kin                 | Kinyarwanda           |          28 | 0.00%                |    23.3571 |

## Accuracy performance
Aggregated accuracy: **0.8892028772532843**

### Stats per language
|    | language_iso639_3   | language              |   sentences |   accuracy |
|---:|:--------------------|:----------------------|------------:|-----------:|
|  1 | eng                 | English               |     1479733 |      0.973 |
|  2 | rus                 | Russian               |      849653 |      0.823 |
|  3 | ita                 | Italian               |      787053 |      0.885 |
|  4 | tur                 | Turkish               |      709573 |      0.919 |
|  5 | epo                 | Esperanto             |      659632 |      0.854 |
|  6 | deu                 | German                |      553727 |      0.974 |
|  7 | fra                 | French                |      466192 |      0.935 |
|  8 | por                 | Portuguese            |      385737 |      0.822 |
|  9 | spa                 | Spanish               |      338781 |      0.837 |
| 10 | hun                 | Hungarian             |      323048 |      0.929 |
| 11 | jpn                 | Japanese              |      208761 |      1.000 |
| 12 | heb                 | Hebrew                |      197226 |      0.999 |
| 13 | ukr                 | Ukrainian             |      171674 |      0.774 |
| 14 | nld                 | Dutch                 |      144340 |      0.901 |
| 15 | fin                 | Finnish               |      128011 |      0.931 |
| 16 | pol                 | Polish                |      109662 |      0.977 |
| 17 | mkd                 | Macedonian            |       77938 |      0.482 |
| 18 | mar                 | Marathi               |       64126 |      0.700 |
| 19 | lit                 | Lithuanian            |       59659 |      0.915 |
| 20 | ces                 | Czech                 |       57030 |      0.837 |
| 21 | dan                 | Danish                |       49399 |      0.602 |
| 22 | srp                 | Serbian               |       45176 |      0.392 |
| 23 | swe                 | Swedish               |       41677 |      0.802 |
| 24 | lat                 | Latin                 |       39718 |      0.196 |
| 25 | ara                 | Arabic                |       35991 |      0.950 |
| 26 | ell                 | Modern Greek (1453-)  |       34071 |      1.000 |
| 27 | ron                 | Romanian              |       24943 |      0.906 |
| 28 | bul                 | Bulgarian             |       24503 |      0.624 |
| 29 | vie                 | Vietnamese            |       19234 |      0.998 |
| 30 | tgl                 | Tagalog               |       16649 |      0.792 |
| 31 | slk                 | Slovak                |       14660 |      0.690 |
| 32 | ind                 | Indonesian            |       14542 |      0.731 |
| 33 | hin                 | Hindi                 |       14230 |      0.901 |
| 34 | nob                 | Norwegian Bokmål      |       14223 |      0.308 |
| 35 | bel                 | Belarusian            |       12633 |      0.879 |
| 36 | isl                 | Icelandic             |       11091 |      0.929 |
| 37 | cat                 | Catalan               |        7971 |      0.720 |
| 38 | uig                 | Uighur                |        7792 |      0.989 |
| 39 | kor                 | Korean                |        7570 |      1.000 |
| 40 | bre                 | Breton                |        7195 |      0.630 |
| 41 | eus                 | Basque                |        6166 |      0.866 |
| 42 | kat                 | Georgian              |        5732 |      0.996 |
| 43 | oci                 | Occitan (post 1500)   |        5693 |      0.505 |
| 44 | aze                 | Azerbaijani           |        5348 |      0.756 |
| 45 | hrv                 | Croatian              |        5204 |      0.650 |
| 46 | ben                 | Bengali               |        4714 |      0.977 |
| 47 | glg                 | Galician              |        4613 |      0.520 |
| 48 | vol                 | Volapük               |        4132 |      0.265 |
| 49 | afr                 | Afrikaans             |        4031 |      0.462 |
| 50 | kaz                 | Kazakh                |        3685 |      0.943 |
| 51 | est                 | Estonian              |        3637 |      0.689 |
| 52 | tha                 | Thai                  |        3528 |      1.000 |
| 53 | asm                 | Assamese              |        2912 |      0.227 |
| 54 | mon                 | Mongolian             |        2757 |      0.950 |
| 55 | sqi                 | Albanian              |        2526 |      0.905 |
| 56 | gle                 | Irish                 |        2389 |      0.840 |
| 57 | hye                 | Armenian              |        2248 |      0.911 |
| 58 | urd                 | Urdu                  |        2008 |      0.947 |
| 59 | nno                 | Norwegian Nynorsk     |        1576 |      0.501 |
| 60 | khm                 | Central Khmer         |        1511 |      0.975 |
| 61 | cym                 | Welsh                 |        1344 |      0.682 |
| 62 | slv                 | Slovenian             |        1093 |      0.681 |
| 63 | mal                 | Malayalam             |         827 |      1.000 |
| 64 | ltz                 | Luxembourgish         |         805 |      0.343 |
| 65 | jav                 | Javanese              |         615 |      0.486 |
| 66 | bos                 | Bosnian               |         567 |      0.053 |
| 67 | que                 | Quechua               |         422 |      0.382 |
| 68 | fao                 | Faroese               |         402 |      0.281 |
| 69 | ori                 | Oriya (macrolanguage) |         374 |      0.992 |
| 70 | tam                 | Tamil                 |         334 |      1.000 |
| 71 | tel                 | Telugu                |         254 |      1.000 |
| 72 | kir                 | Kirghiz               |         254 |      0.118 |
| 73 | xho                 | Xhosa                 |         252 |      0.575 |
| 74 | lao                 | Lao                   |         219 |      1.000 |
| 75 | amh                 | Amharic               |         211 |      1.000 |
| 76 | mlt                 | Maltese               |         208 |      0.817 |
| 77 | pan                 | Panjabi               |         196 |      1.000 |
| 78 | sme                 | Northern Sami         |         181 |      0.320 |
| 79 | kan                 | Kannada               |         176 |      1.000 |
| 80 | guj                 | Gujarati              |         168 |      1.000 |
| 81 | arg                 | Aragonese             |         103 |      0.029 |
| 82 | zul                 | Zulu                  |          77 |      0.286 |
| 83 | hat                 | Haitian               |          64 |      0.406 |
| 84 | mlg                 | Malagasy              |          59 |      0.559 |
| 85 | wln                 | Walloon               |          53 |      0.528 |
| 86 | sin                 | Sinhala               |          45 |      1.000 |
| 87 | pus                 | Pushto                |          44 |      0.432 |
| 88 | kin                 | Kinyarwanda           |          28 |      0.214 |