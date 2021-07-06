# Results for fasttext-compressed on tatoeba-sentences-2021-06-05

- [Dataset stats](#dataset-stats)
- [Accuracy performance](#accuracy-performance)
  - [Stats per language](#stats-per-language)

## Dataset stats
|     | language_iso639_3   | language                                                   |   sentences | dataset_percentage   |   mean_len |
|----:|:--------------------|:-----------------------------------------------------------|------------:|:---------------------|-----------:|
|   1 | eng                 | English                                                    |     1479733 | 17.54%               |    39.3277 |
|   2 | rus                 | Russian                                                    |      849653 | 10.07%               |    33.4655 |
|   3 | ita                 | Italian                                                    |      787053 | 9.33%                |    33.4897 |
|   4 | tur                 | Turkish                                                    |      709573 | 8.41%                |    34.7355 |
|   5 | epo                 | Esperanto                                                  |      659632 | 7.82%                |    40.3975 |
|   6 | deu                 | German                                                     |      553727 | 6.56%                |    47.4774 |
|   7 | fra                 | French                                                     |      466192 | 5.53%                |    41.3866 |
|   8 | por                 | Portuguese                                                 |      385737 | 4.57%                |    38.2929 |
|   9 | spa                 | Spanish                                                    |      338781 | 4.02%                |    38.8894 |
|  10 | hun                 | Hungarian                                                  |      323048 | 3.83%                |    34.0299 |
|  11 | jpn                 | Japanese                                                   |      208761 | 2.48%                |    18.2659 |
|  12 | heb                 | Hebrew                                                     |      197226 | 2.34%                |    25.5678 |
|  13 | ukr                 | Ukrainian                                                  |      171674 | 2.04%                |    27.8153 |
|  14 | nld                 | Dutch                                                      |      144340 | 1.71%                |    34.7853 |
|  15 | fin                 | Finnish                                                    |      128011 | 1.52%                |    35.7946 |
|  16 | pol                 | Polish                                                     |      109662 | 1.30%                |    33.2333 |
|  17 | mkd                 | Macedonian                                                 |       77938 | 0.92%                |    27.3793 |
|  18 | mar                 | Marathi                                                    |       64126 | 0.76%                |    27.587  |
|  19 | lit                 | Lithuanian                                                 |       59659 | 0.71%                |    30.1439 |
|  20 | ces                 | Czech                                                      |       57030 | 0.68%                |    28.3683 |
|  21 | dan                 | Danish                                                     |       49399 | 0.59%                |    33.7159 |
|  22 | srp                 | Serbian                                                    |       45176 | 0.54%                |    30.4306 |
|  23 | swe                 | Swedish                                                    |       41677 | 0.49%                |    30.1428 |
|  24 | lat                 | Latin                                                      |       39718 | 0.47%                |    36.1448 |
|  25 | ara                 | Arabic                                                     |       35991 | 0.43%                |    26.7817 |
|  26 | ell                 | Modern Greek (1453-)                                       |       34071 | 0.40%                |    30.3915 |
|  27 | ina                 | Interlingua (International Auxiliary Language Association) |       26680 | 0.32%                |    47.0018 |
|  28 | ron                 | Romanian                                                   |       24943 | 0.30%                |    34.4097 |
|  29 | bul                 | Bulgarian                                                  |       24503 | 0.29%                |    31.7201 |
|  30 | vie                 | Vietnamese                                                 |       19234 | 0.23%                |    38.7891 |
|  31 | nds                 | Low German                                                 |       17921 | 0.21%                |    33.1626 |
|  32 | tgl                 | Tagalog                                                    |       16649 | 0.20%                |    36.8098 |
|  33 | jbo                 | Lojban                                                     |       15925 | 0.19%                |    30.7496 |
|  34 | slk                 | Slovak                                                     |       14660 | 0.17%                |    25.7422 |
|  35 | ind                 | Indonesian                                                 |       14542 | 0.17%                |    37.4785 |
|  36 | hin                 | Hindi                                                      |       14230 | 0.17%                |    27.6058 |
|  37 | tat                 | Tatar                                                      |       13674 | 0.16%                |    44.7585 |
|  38 | bel                 | Belarusian                                                 |       12633 | 0.15%                |    37.3887 |
|  39 | isl                 | Icelandic                                                  |       11091 | 0.13%                |    35.3886 |
|  40 | cat                 | Catalan                                                    |        7971 | 0.09%                |    37.334  |
|  41 | uig                 | Uighur                                                     |        7792 | 0.09%                |    31.1084 |
|  42 | kor                 | Korean                                                     |        7570 | 0.09%                |    16.8085 |
|  43 | ido                 | Ido                                                        |        7373 | 0.09%                |    29.0663 |
|  44 | ile                 | Interlingue                                                |        7352 | 0.09%                |    26.2331 |
|  45 | bre                 | Breton                                                     |        7195 | 0.09%                |    27.4111 |
|  46 | yid                 | Yiddish                                                    |        6895 | 0.08%                |    29.8983 |
|  47 | tuk                 | Turkmen                                                    |        6729 | 0.08%                |    33.9633 |
|  48 | eus                 | Basque                                                     |        6166 | 0.07%                |    32.999  |
|  49 | yue                 | Yue Chinese                                                |        6134 | 0.07%                |    11.739  |
|  50 | kat                 | Georgian                                                   |        5732 | 0.07%                |    26.0173 |
|  51 | oci                 | Occitan (post 1500)                                        |        5693 | 0.07%                |    32.3931 |
|  52 | aze                 | Azerbaijani                                                |        5348 | 0.06%                |    26.2691 |
|  53 | hrv                 | Croatian                                                   |        5204 | 0.06%                |    30.058  |
|  54 | ben                 | Bengali                                                    |        4714 | 0.06%                |    23.7809 |
|  55 | glg                 | Galician                                                   |        4613 | 0.05%                |    35.8186 |
|  56 | wuu                 | Wu Chinese                                                 |        4549 | 0.05%                |    12.0015 |
|  57 | mhr                 | Eastern Mari                                               |        4300 | 0.05%                |    33.9802 |
|  58 | vol                 | Volapük                                                    |        4132 | 0.05%                |    23.3129 |
|  59 | afr                 | Afrikaans                                                  |        4031 | 0.05%                |    29.676  |
|  60 | cor                 | Cornish                                                    |        3925 | 0.05%                |    21.5801 |
|  61 | kaz                 | Kazakh                                                     |        3685 | 0.04%                |    49.9183 |
|  62 | est                 | Estonian                                                   |        3637 | 0.04%                |    27.6646 |
|  63 | tha                 | Thai                                                       |        3528 | 0.04%                |    20.5697 |
|  64 | grn                 | Guarani                                                    |        2961 | 0.04%                |    28.4691 |
|  65 | asm                 | Assamese                                                   |        2912 | 0.03%                |    24.1006 |
|  66 | frr                 | Northern Frisian                                           |        2855 | 0.03%                |    28.1916 |
|  67 | mon                 | Mongolian                                                  |        2757 | 0.03%                |    30.9387 |
|  68 | cbk                 | Chavacano                                                  |        2621 | 0.03%                |    30.0397 |
|  69 | sqi                 | Albanian                                                   |        2526 | 0.03%                |    32.2743 |
|  70 | ilo                 | Iloko                                                      |        2455 | 0.03%                |    34.4794 |
|  71 | gle                 | Irish                                                      |        2389 | 0.03%                |    27.7765 |
|  72 | hye                 | Armenian                                                   |        2248 | 0.03%                |    22.5934 |
|  73 | war                 | Waray (Philippines)                                        |        2025 | 0.02%                |    34.3274 |
|  74 | urd                 | Urdu                                                       |        2008 | 0.02%                |    30.7495 |
|  75 | nno                 | Norwegian Nynorsk                                          |        1576 | 0.02%                |    30.8249 |
|  76 | chv                 | Chuvash                                                    |        1566 | 0.02%                |    25.6124 |
|  77 | khm                 | Central Khmer                                              |        1511 | 0.02%                |    24.2766 |
|  78 | pam                 | Pampanga                                                   |        1482 | 0.02%                |    29.168  |
|  79 | ceb                 | Cebuano                                                    |        1478 | 0.02%                |    32.1069 |
|  80 | hsb                 | Upper Sorbian                                              |        1423 | 0.02%                |    23.6339 |
|  81 | cym                 | Welsh                                                      |        1344 | 0.02%                |    29.3058 |
|  82 | slv                 | Slovenian                                                  |        1093 | 0.01%                |    28.4282 |
|  83 | ckb                 | Central Kurdish                                            |        1089 | 0.01%                |    22.5794 |
|  84 | gla                 | Scottish Gaelic                                            |        1033 | 0.01%                |    33.5334 |
|  85 | dsb                 | Lower Sorbian                                              |         991 | 0.01%                |    26.7508 |
|  86 | sah                 | Yakut                                                      |         943 | 0.01%                |    28.315  |
|  87 | xal                 | Kalmyk                                                     |         870 | 0.01%                |    29.3621 |
|  88 | uzb                 | Uzbek                                                      |         855 | 0.01%                |    25.9813 |
|  89 | mal                 | Malayalam                                                  |         827 | 0.01%                |    36.8222 |
|  90 | pms                 | Piemontese                                                 |         823 | 0.01%                |    34.9721 |
|  91 | ltz                 | Luxembourgish                                              |         805 | 0.01%                |    25.4099 |
|  92 | arz                 | Egyptian Arabic                                            |         798 | 0.01%                |    20.2331 |
|  93 | jav                 | Javanese                                                   |         615 | 0.01%                |    28.7333 |
|  94 | bos                 | Bosnian                                                    |         567 | 0.01%                |    23.3492 |
|  95 | mya                 | Burmese                                                    |         433 | 0.01%                |    33.5219 |
|  96 | que                 | Quechua                                                    |         422 | 0.01%                |    25.6588 |
|  97 | ori                 | Oriya (macrolanguage)                                      |         374 | 0.00%                |    12.7567 |
|  98 | fry                 | Western Frisian                                            |         355 | 0.00%                |    28.569  |
|  99 | tam                 | Tamil                                                      |         334 | 0.00%                |    35.2784 |
| 100 | ast                 | Asturian                                                   |         280 | 0.00%                |    27.4429 |
| 101 | tel                 | Telugu                                                     |         254 | 0.00%                |    28.0157 |
| 102 | kir                 | Kirghiz                                                    |         254 | 0.00%                |    23.8504 |
| 103 | oss                 | Ossetian                                                   |         236 | 0.00%                |    24.5297 |
| 104 | lao                 | Lao                                                        |         219 | 0.00%                |    27.5388 |
| 105 | bak                 | Bashkir                                                    |         215 | 0.00%                |    38.6512 |
| 106 | nah                 | Nahuatl languages                                          |         212 | 0.00%                |    40.1274 |
| 107 | amh                 | Amharic                                                    |         211 | 0.00%                |    12.7867 |
| 108 | mlt                 | Maltese                                                    |         208 | 0.00%                |    25.9952 |
| 109 | bar                 | Bavarian                                                   |         200 | 0.00%                |    35.065  |
| 110 | pan                 | Panjabi                                                    |         196 | 0.00%                |    32.8622 |
| 111 | vec                 | Venetian                                                   |         190 | 0.00%                |    31.5947 |
| 112 | kan                 | Kannada                                                    |         176 | 0.00%                |    35.3636 |
| 113 | guj                 | Gujarati                                                   |         168 | 0.00%                |    24.244  |
| 114 | san                 | Sanskrit                                                   |         156 | 0.00%                |    24.0962 |
| 115 | krc                 | Karachay-Balkar                                            |         148 | 0.00%                |    30.1824 |
| 116 | min                 | Minangkabau                                                |         121 | 0.00%                |    23.0826 |
| 117 | rue                 | Rusyn                                                      |         116 | 0.00%                |    16.9052 |
| 118 | arg                 | Aragonese                                                  |         103 | 0.00%                |    15.9515 |
| 119 | mrj                 | Western Mari                                               |          83 | 0.00%                |    35.5181 |
| 120 | sco                 | Scots                                                      |          82 | 0.00%                |    37.2561 |
| 121 | som                 | Somali                                                     |          80 | 0.00%                |    30.025  |
| 122 | hat                 | Haitian                                                    |          64 | 0.00%                |    22.4688 |
| 123 | tgk                 | Tajik                                                      |          63 | 0.00%                |    31.4603 |
| 124 | mlg                 | Malagasy                                                   |          59 | 0.00%                |    21.0339 |
| 125 | xmf                 | Mingrelian                                                 |          58 | 0.00%                |    24.2069 |
| 126 | wln                 | Walloon                                                    |          53 | 0.00%                |    28.2642 |
| 127 | sin                 | Sinhala                                                    |          45 | 0.00%                |    22.0222 |
| 128 | pus                 | Pushto                                                     |          44 | 0.00%                |    35.9318 |
| 129 | bod                 | Tibetan                                                    |          41 | 0.00%                |    33.1951 |
| 130 | yor                 | Yoruba                                                     |          37 | 0.00%                |    23.2973 |
| 131 | scn                 | Sicilian                                                   |          35 | 0.00%                |    35.3429 |
| 132 | pnb                 | Western Panjabi                                            |          35 | 0.00%                |    24.6857 |
| 133 | hif                 | Fiji Hindi                                                 |          34 | 0.00%                |    28.0588 |
| 134 | lim                 | Limburgan                                                  |          33 | 0.00%                |    19.303  |
| 135 | glv                 | Manx                                                       |          33 | 0.00%                |    19.5455 |
| 136 | sun                 | Sundanese                                                  |          31 | 0.00%                |    25.7742 |
| 137 | lmo                 | Lombard                                                    |          29 | 0.00%                |    20.9655 |
| 138 | che                 | Chechen                                                    |          28 | 0.00%                |    26.6429 |
| 139 | div                 | Dhivehi                                                    |          26 | 0.00%                |    45.7692 |
| 140 | myv                 | Erzya                                                      |          26 | 0.00%                |    19      |
| 141 | cos                 | Corsican                                                   |          24 | 0.00%                |    20.1667 |
| 142 | mwl                 | Mirandese                                                  |          22 | 0.00%                |    28.9091 |
| 143 | roh                 | Romansh                                                    |          20 | 0.00%                |    56.55   |
| 144 | tyv                 | Tuvinian                                                   |          17 | 0.00%                |    20      |
| 145 | new                 | Newari                                                     |          17 | 0.00%                |    16.7647 |
| 146 | srd                 | Sardinian                                                  |          15 | 0.00%                |    31.0667 |
| 147 | vep                 | Veps                                                       |          13 | 0.00%                |    33.9231 |
| 148 | mai                 | Maithili                                                   |           8 | 0.00%                |     9.75   |
| 149 | diq                 | Dimli (individual language)                                |           6 | 0.00%                |    15.5    |
| 150 | snd                 | Sindhi                                                     |           6 | 0.00%                |    22.3333 |
| 151 | bcl                 | Central Bikol                                              |           5 | 0.00%                |    21.8    |
| 152 | gom                 | Goan Konkani                                               |           4 | 0.00%                |    37.5    |
| 153 | pfl                 | Pfaelzisch                                                 |           3 | 0.00%                |    39.3333 |

## Accuracy performance
Aggregated accuracy: **0.968988637122133**

### Stats per language
|     | language_iso639_3   | language                                                   |   sentences |   accuracy |
|----:|:--------------------|:-----------------------------------------------------------|------------:|-----------:|
|   1 | eng                 | English                                                    |     1479733 |      0.997 |
|   2 | rus                 | Russian                                                    |      849653 |      0.996 |
|   3 | ita                 | Italian                                                    |      787053 |      0.987 |
|   4 | tur                 | Turkish                                                    |      709573 |      0.994 |
|   5 | epo                 | Esperanto                                                  |      659632 |      0.993 |
|   6 | deu                 | German                                                     |      553727 |      0.993 |
|   7 | fra                 | French                                                     |      466192 |      0.988 |
|   8 | por                 | Portuguese                                                 |      385737 |      0.965 |
|   9 | spa                 | Spanish                                                    |      338781 |      0.977 |
|  10 | hun                 | Hungarian                                                  |      323048 |      0.981 |
|  11 | jpn                 | Japanese                                                   |      208761 |      0.997 |
|  12 | heb                 | Hebrew                                                     |      197226 |      0.999 |
|  13 | ukr                 | Ukrainian                                                  |      171674 |      0.916 |
|  14 | nld                 | Dutch                                                      |      144340 |      0.927 |
|  15 | fin                 | Finnish                                                    |      128011 |      0.964 |
|  16 | pol                 | Polish                                                     |      109662 |      0.983 |
|  17 | mkd                 | Macedonian                                                 |       77938 |      0.936 |
|  18 | mar                 | Marathi                                                    |       64126 |      0.984 |
|  19 | lit                 | Lithuanian                                                 |       59659 |      0.916 |
|  20 | ces                 | Czech                                                      |       57030 |      0.908 |
|  21 | dan                 | Danish                                                     |       49399 |      0.871 |
|  22 | srp                 | Serbian                                                    |       45176 |      0.648 |
|  23 | swe                 | Swedish                                                    |       41677 |      0.918 |
|  24 | lat                 | Latin                                                      |       39718 |      0.771 |
|  25 | ara                 | Arabic                                                     |       35991 |      0.984 |
|  26 | ell                 | Modern Greek (1453-)                                       |       34071 |      0.999 |
|  27 | ina                 | Interlingua (International Auxiliary Language Association) |       26680 |      0.574 |
|  28 | ron                 | Romanian                                                   |       24943 |      0.891 |
|  29 | bul                 | Bulgarian                                                  |       24503 |      0.815 |
|  30 | vie                 | Vietnamese                                                 |       19234 |      0.988 |
|  31 | nds                 | Low German                                                 |       17921 |      0.787 |
|  32 | tgl                 | Tagalog                                                    |       16649 |      0.878 |
|  33 | jbo                 | Lojban                                                     |       15925 |      0.895 |
|  34 | slk                 | Slovak                                                     |       14660 |      0.478 |
|  35 | ind                 | Indonesian                                                 |       14542 |      0.880 |
|  36 | hin                 | Hindi                                                      |       14230 |      0.962 |
|  37 | tat                 | Tatar                                                      |       13674 |      0.850 |
|  38 | bel                 | Belarusian                                                 |       12633 |      0.712 |
|  39 | isl                 | Icelandic                                                  |       11091 |      0.922 |
|  40 | cat                 | Catalan                                                    |        7971 |      0.686 |
|  41 | uig                 | Uighur                                                     |        7792 |      0.978 |
|  42 | kor                 | Korean                                                     |        7570 |      0.970 |
|  43 | ido                 | Ido                                                        |        7373 |      0.362 |
|  44 | ile                 | Interlingue                                                |        7352 |      0.299 |
|  45 | bre                 | Breton                                                     |        7195 |      0.739 |
|  46 | yid                 | Yiddish                                                    |        6895 |      0.823 |
|  47 | tuk                 | Turkmen                                                    |        6729 |      0.403 |
|  48 | eus                 | Basque                                                     |        6166 |      0.783 |
|  49 | yue                 | Yue Chinese                                                |        6134 |      0.645 |
|  50 | kat                 | Georgian                                                   |        5732 |      0.987 |
|  51 | oci                 | Occitan (post 1500)                                        |        5693 |      0.544 |
|  52 | aze                 | Azerbaijani                                                |        5348 |      0.725 |
|  53 | hrv                 | Croatian                                                   |        5204 |      0.353 |
|  54 | ben                 | Bengali                                                    |        4714 |      0.996 |
|  55 | glg                 | Galician                                                   |        4613 |      0.323 |
|  56 | wuu                 | Wu Chinese                                                 |        4549 |      0.544 |
|  57 | mhr                 | Eastern Mari                                               |        4300 |      0.721 |
|  58 | vol                 | Volapük                                                    |        4132 |      0.460 |
|  59 | afr                 | Afrikaans                                                  |        4031 |      0.627 |
|  60 | cor                 | Cornish                                                    |        3925 |      0.769 |
|  61 | kaz                 | Kazakh                                                     |        3685 |      0.871 |
|  62 | est                 | Estonian                                                   |        3637 |      0.654 |
|  63 | tha                 | Thai                                                       |        3528 |      0.999 |
|  64 | grn                 | Guarani                                                    |        2961 |      0.223 |
|  65 | asm                 | Assamese                                                   |        2912 |      0.594 |
|  66 | frr                 | Northern Frisian                                           |        2855 |      0.000 |
|  67 | mon                 | Mongolian                                                  |        2757 |      0.750 |
|  68 | cbk                 | Chavacano                                                  |        2621 |      0.204 |
|  69 | sqi                 | Albanian                                                   |        2526 |      0.835 |
|  70 | ilo                 | Iloko                                                      |        2455 |      0.600 |
|  71 | gle                 | Irish                                                      |        2389 |      0.684 |
|  72 | hye                 | Armenian                                                   |        2248 |      0.992 |
|  73 | war                 | Waray (Philippines)                                        |        2025 |      0.420 |
|  74 | urd                 | Urdu                                                       |        2008 |      0.954 |
|  75 | nno                 | Norwegian Nynorsk                                          |        1576 |      0.414 |
|  76 | chv                 | Chuvash                                                    |        1566 |      0.683 |
|  77 | khm                 | Central Khmer                                              |        1511 |      0.981 |
|  78 | pam                 | Pampanga                                                   |        1482 |      0.333 |
|  79 | ceb                 | Cebuano                                                    |        1478 |      0.415 |
|  80 | hsb                 | Upper Sorbian                                              |        1423 |      0.247 |
|  81 | cym                 | Welsh                                                      |        1344 |      0.541 |
|  82 | slv                 | Slovenian                                                  |        1093 |      0.431 |
|  83 | ckb                 | Central Kurdish                                            |        1089 |      0.842 |
|  84 | gla                 | Scottish Gaelic                                            |        1033 |      0.639 |
|  85 | dsb                 | Lower Sorbian                                              |         991 |      0.222 |
|  86 | sah                 | Yakut                                                      |         943 |      0.758 |
|  87 | xal                 | Kalmyk                                                     |         870 |      0.249 |
|  88 | uzb                 | Uzbek                                                      |         855 |      0.214 |
|  89 | mal                 | Malayalam                                                  |         827 |      0.999 |
|  90 | pms                 | Piemontese                                                 |         823 |      0.469 |
|  91 | ltz                 | Luxembourgish                                              |         805 |      0.366 |
|  92 | arz                 | Egyptian Arabic                                            |         798 |      0.045 |
|  93 | jav                 | Javanese                                                   |         615 |      0.333 |
|  94 | bos                 | Bosnian                                                    |         567 |      0.016 |
|  95 | mya                 | Burmese                                                    |         433 |      0.998 |
|  96 | que                 | Quechua                                                    |         422 |      0.254 |
|  97 | ori                 | Oriya (macrolanguage)                                      |         374 |      0.741 |
|  98 | fry                 | Western Frisian                                            |         355 |      0.307 |
|  99 | tam                 | Tamil                                                      |         334 |      1.000 |
| 100 | ast                 | Asturian                                                   |         280 |      0.104 |
| 101 | tel                 | Telugu                                                     |         254 |      1.000 |
| 102 | kir                 | Kirghiz                                                    |         254 |      0.535 |
| 103 | oss                 | Ossetian                                                   |         236 |      0.686 |
| 104 | lao                 | Lao                                                        |         219 |      0.817 |
| 105 | bak                 | Bashkir                                                    |         215 |      0.688 |
| 106 | nah                 | Nahuatl languages                                          |         212 |      0.033 |
| 107 | amh                 | Amharic                                                    |         211 |      0.981 |
| 108 | mlt                 | Maltese                                                    |         208 |      0.423 |
| 109 | bar                 | Bavarian                                                   |         200 |      0.015 |
| 110 | pan                 | Panjabi                                                    |         196 |      1.000 |
| 111 | vec                 | Venetian                                                   |         190 |      0.132 |
| 112 | kan                 | Kannada                                                    |         176 |      1.000 |
| 113 | guj                 | Gujarati                                                   |         168 |      1.000 |
| 114 | san                 | Sanskrit                                                   |         156 |      0.500 |
| 115 | krc                 | Karachay-Balkar                                            |         148 |      0.128 |
| 116 | min                 | Minangkabau                                                |         121 |      0.033 |
| 117 | rue                 | Rusyn                                                      |         116 |      0.000 |
| 118 | arg                 | Aragonese                                                  |         103 |      0.019 |
| 119 | mrj                 | Western Mari                                               |          83 |      0.325 |
| 120 | sco                 | Scots                                                      |          82 |      0.073 |
| 121 | som                 | Somali                                                     |          80 |      0.025 |
| 122 | hat                 | Haitian                                                    |          64 |      0.016 |
| 123 | tgk                 | Tajik                                                      |          63 |      0.603 |
| 124 | mlg                 | Malagasy                                                   |          59 |      0.153 |
| 125 | xmf                 | Mingrelian                                                 |          58 |      0.052 |
| 126 | wln                 | Walloon                                                    |          53 |      0.226 |
| 127 | sin                 | Sinhala                                                    |          45 |      1.000 |
| 128 | pus                 | Pushto                                                     |          44 |      0.409 |
| 129 | bod                 | Tibetan                                                    |          41 |      1.000 |
| 130 | yor                 | Yoruba                                                     |          37 |      0.189 |
| 131 | scn                 | Sicilian                                                   |          35 |      0.171 |
| 132 | pnb                 | Western Panjabi                                            |          35 |      0.429 |
| 133 | hif                 | Fiji Hindi                                                 |          34 |      0.000 |
| 134 | lim                 | Limburgan                                                  |          33 |      0.121 |
| 135 | glv                 | Manx                                                       |          33 |      0.030 |
| 136 | sun                 | Sundanese                                                  |          31 |      0.032 |
| 137 | lmo                 | Lombard                                                    |          29 |      0.103 |
| 138 | che                 | Chechen                                                    |          28 |      0.393 |
| 139 | div                 | Dhivehi                                                    |          26 |      0.962 |
| 140 | myv                 | Erzya                                                      |          26 |      0.000 |
| 141 | cos                 | Corsican                                                   |          24 |      0.042 |
| 142 | mwl                 | Mirandese                                                  |          22 |      0.045 |
| 143 | roh                 | Romansh                                                    |          20 |      0.050 |
| 144 | tyv                 | Tuvinian                                                   |          17 |      0.059 |
| 145 | new                 | Newari                                                     |          17 |      0.059 |
| 146 | srd                 | Sardinian                                                  |          15 |      0.000 |
| 147 | vep                 | Veps                                                       |          13 |      0.000 |
| 148 | mai                 | Maithili                                                   |           8 |      0.125 |
| 149 | diq                 | Dimli (individual language)                                |           6 |      0.000 |
| 150 | snd                 | Sindhi                                                     |           6 |      0.333 |
| 151 | bcl                 | Central Bikol                                              |           5 |      0.000 |
| 152 | gom                 | Goan Konkani                                               |           4 |      0.000 |
| 153 | pfl                 | Pfaelzisch                                                 |           3 |      0.000 |