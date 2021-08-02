# Classification performance for pycld2 on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 7569549 (78.52%)
- **Aggregated accuracy: 0.8694755790602584**

## Supported languages (83)
afr (Afrikaans), sqi (Albanian), ara (Arabic), hye (Armenian), aze (Azerbaijani), eus (Basque), bel (Belarusian), ben (Bangla), bih (Bihari languages), bul (Bulgarian), cat (Catalan), ceb (Cebuano), chr (Cherokee), hrv (Croatian), ces (Czech), zho (Chinese), dan (Danish), div (Divehi), nld (Dutch), eng (English), est (Estonian), fin (Finnish), fra (French), glg (Galician), lug (Ganda), kat (Georgian), deu (German), ell (Greek), guj (Gujarati), hat (Haitian Creole), heb (Hebrew), hin (Hindi), hmn (Hmong), hun (Hungarian), isl (Icelandic), ind (Indonesian), iku (Inuktitut), gle (Irish), ita (Italian), jav (Javanese), jpn (Japanese), kan (Kannada), khm (Khmer), kin (Kinyarwanda), kor (Korean), lao (Lao), lav (Latvian), lif (Limbu), lit (Lithuanian), mkd (Macedonian), msa (Malay), mal (Malayalam), mlt (Maltese), mar (Marathi), nep (Nepali), nob (Norwegian Bokmål), ori (Odia), fas (Persian), pol (Polish), por (Portuguese), pan (Punjabi), ron (Romanian), rus (Russian), gla (Scottish Gaelic), srp (Serbian), sin (Sinhala), slk (Slovak), slv (Slovenian), spa (Spanish), swa (Swahili), swe (Swedish), syr (Syriac), fil (Filipino), tam (Tamil), tel (Telugu), tha (Thai), tur (Turkish), ukr (Ukrainian), urd (Urdu), vie (Vietnamese), cym (Welsh), yid (Yiddish), zho (Chinese)

## Stats per language
|    | language_alpha3   | language              |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |     fn |
|---:|:------------------|:----------------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|-------:|
|  1 | eng               | English               |           1479733 |       0.954 |    0.970 | 0.940 | 1435203 | 68766 | 6021050 |  44530 |
|  2 | rus               | Russian               |            849653 |       0.998 |    0.830 | 0.905 |  705549 |  1667 | 6718229 | 144104 |
|  3 | ita               | Italian               |            787053 |       0.999 |    0.689 | 0.816 |  542549 |   442 | 6782054 | 244504 |
|  4 | tur               | Turkish               |            709573 |       1.000 |    0.923 | 0.960 |  654731 |   191 | 6859785 |  54842 |
|  5 | deu               | German                |            553727 |       1.000 |    0.954 | 0.976 |  528244 |   184 | 7015638 |  25483 |
|  6 | fra               | French                |            466192 |       0.999 |    0.845 | 0.915 |  394106 |   374 | 7102983 |  72086 |
|  7 | por               | Portuguese            |            385737 |       0.981 |    0.865 | 0.912 |  333763 |  6371 | 7177441 |  51974 |
|  8 | spa               | Spanish               |            338781 |       0.994 |    0.798 | 0.883 |  270207 |  1677 | 7229091 |  68574 |
|  9 | hun               | Hungarian             |            323048 |       1.000 |    0.935 | 0.966 |  302013 |   133 | 7246368 |  21035 |
| 10 | jpn               | Japanese              |            208761 |       1.000 |    0.999 | 1.000 |  208635 |     0 | 7360788 |    126 |
| 11 | heb               | Hebrew                |            197226 |       1.000 |    0.841 | 0.914 |  165882 |    10 | 7372313 |  31344 |
| 12 | ukr               | Ukrainian             |            171674 |       0.991 |    0.791 | 0.877 |  135799 |  1168 | 7396707 |  35875 |
| 13 | nld               | Dutch                 |            144340 |       0.994 |    0.820 | 0.897 |  118356 |   664 | 7424545 |  25984 |
| 14 | fin               | Finnish               |            128011 |       0.999 |    0.909 | 0.951 |  116372 |   161 | 7441377 |  11639 |
| 15 | pol               | Polish                |            109662 |       0.999 |    0.926 | 0.961 |  101512 |    75 | 7459812 |   8150 |
| 16 | mkd               | Macedonian            |             77938 |       0.969 |    0.477 | 0.633 |   37213 |  1178 | 7490433 |  40725 |
| 17 | mar               | Marathi               |             64126 |       1.000 |    0.967 | 0.983 |   62024 |    24 | 7505399 |   2102 |
| 18 | lit               | Lithuanian            |             59659 |       0.997 |    0.914 | 0.952 |   54501 |   144 | 7509746 |   5158 |
| 19 | ces               | Czech                 |             57030 |       0.970 |    0.891 | 0.916 |   50816 |  1551 | 7510968 |   6214 |
| 20 | dan               | Danish                |             49399 |       0.866 |    0.698 | 0.729 |   34494 |  5341 | 7514809 |  14905 |
| 21 | srp               | Serbian               |             45176 |       0.246 |    0.564 | 0.225 |   25486 | 77950 | 7446423 |  19690 |
| 22 | swe               | Swedish               |             41677 |       0.995 |    0.761 | 0.861 |   31709 |   145 | 7527727 |   9968 |
| 23 | ara               | Arabic                |             35991 |       1.000 |    0.776 | 0.874 |   27916 |     1 | 7533557 |   8075 |
| 24 | ell               | Modern Greek (1453-)  |             34071 |       1.000 |    1.000 | 1.000 |   34071 |    14 | 7535464 |      0 |
| 25 | ron               | Romanian              |             24943 |       0.963 |    0.811 | 0.865 |   20227 |   787 | 7543819 |   4716 |
| 26 | bul               | Bulgarian             |             24503 |       0.852 |    0.700 | 0.721 |   17140 |  2967 | 7542079 |   7363 |
| 27 | vie               | Vietnamese            |             19234 |       0.995 |    0.991 | 0.990 |   19062 |   103 | 7550212 |    172 |
| 28 | fil               | Filipino              |             16649 |       0.988 |    0.789 | 0.872 |   13136 |   166 | 7552734 |   3513 |
| 29 | slk               | Slovak                |             14660 |       0.693 |    0.788 | 0.634 |   11559 |  5110 | 7549779 |   3101 |
| 30 | ind               | Indonesian            |             14542 |       0.864 |    0.775 | 0.768 |   11270 |  1773 | 7553234 |   3272 |
| 31 | hin               | Hindi                 |             14230 |       0.918 |    0.973 | 0.907 |   13848 |  1230 | 7554089 |    382 |
| 32 | nob               | Norwegian Bokmål      |             14223 |       0.566 |    0.796 | 0.528 |   11327 |  8682 | 7546644 |   2896 |
| 33 | bel               | Belarusian            |             12633 |       0.929 |    0.885 | 0.876 |   11176 |   855 | 7556061 |   1457 |
| 34 | isl               | Icelandic             |             11091 |       0.996 |    0.925 | 0.957 |   10261 |    43 | 7558415 |    830 |
| 35 | cat               | Catalan               |              7971 |       0.806 |    0.685 | 0.680 |    5464 |  1317 | 7560261 |   2507 |
| 36 | kor               | Korean                |              7570 |       1.000 |    0.991 | 0.995 |    7500 |     0 | 7561979 |     70 |
| 37 | yid               | Yiddish               |              6895 |       0.991 |    0.937 | 0.959 |    6460 |    60 | 7562594 |    435 |
| 38 | eus               | Basque                |              6166 |       0.972 |    0.893 | 0.918 |    5505 |   158 | 7563225 |    661 |
| 39 | kat               | Georgian              |              5732 |       1.000 |    1.000 | 1.000 |    5731 |     0 | 7563817 |      1 |
| 40 | aze               | Azerbaijani           |              5348 |       0.509 |    0.870 | 0.490 |    4651 |  4486 | 7559715 |    697 |
| 41 | hrv               | Croatian              |              5204 |       0.270 |    0.565 | 0.244 |    2942 |  7960 | 7556385 |   2262 |
| 42 | ben               | Bengali               |              4714 |       1.000 |    0.777 | 0.874 |    3662 |     0 | 7564835 |   1052 |
| 43 | glg               | Galician              |              4613 |       0.292 |    0.668 | 0.273 |    3081 |  7456 | 7557480 |   1532 |
| 44 | afr               | Afrikaans             |              4031 |       0.446 |    0.826 | 0.426 |    3330 |  4133 | 7561385 |    701 |
| 45 | est               | Estonian              |              3637 |       0.907 |    0.752 | 0.789 |    2734 |   279 | 7565633 |    903 |
| 46 | tha               | Thai                  |              3528 |       1.000 |    1.000 | 1.000 |    3528 |     0 | 7566021 |      0 |
| 47 | sqi               | Albanian              |              2526 |       0.962 |    0.909 | 0.917 |    2295 |    91 | 7566932 |    231 |
| 48 | gle               | Irish                 |              2389 |       0.938 |    0.884 | 0.883 |    2112 |   140 | 7567020 |    277 |
| 49 | hye               | Armenian              |              2248 |       1.000 |    1.000 | 1.000 |    2247 |     0 | 7567301 |      1 |
| 50 | urd               | Urdu                  |              2008 |       0.997 |    0.948 | 0.971 |    1903 |     5 | 7567536 |    105 |
| 51 | khm               | Central Khmer         |              1511 |       1.000 |    0.991 | 0.996 |    1498 |     0 | 7568038 |     13 |
| 52 | ceb               | Cebuano               |              1478 |       0.617 |    0.551 | 0.493 |     815 |   506 | 7567565 |    663 |
| 53 | cym               | Welsh                 |              1344 |       0.968 |    0.845 | 0.890 |    1136 |    37 | 7568168 |    208 |
| 54 | slv               | Slovenian             |              1093 |       0.739 |    0.550 | 0.568 |     601 |   212 | 7568244 |    492 |
| 55 | gla               | Scottish Gaelic       |              1033 |       0.927 |    0.909 | 0.886 |     939 |    74 | 7568442 |     94 |
| 56 | mal               | Malayalam             |               827 |       1.000 |    1.000 | 1.000 |     827 |     0 | 7568722 |      0 |
| 57 | jav               | Javanese              |               615 |       0.806 |    0.610 | 0.641 |     375 |    90 | 7568844 |    240 |
| 58 | ori               | Oriya (macrolanguage) |               374 |       1.000 |    1.000 | 1.000 |     374 |     0 | 7569175 |      0 |
| 59 | tam               | Tamil                 |               334 |       1.000 |    1.000 | 1.000 |     334 |     0 | 7569215 |      0 |
| 60 | tel               | Telugu                |               254 |       1.000 |    1.000 | 1.000 |     254 |     0 | 7569295 |      0 |
| 61 | lao               | Lao                   |               219 |       1.000 |    1.000 | 1.000 |     219 |     0 | 7569330 |      0 |
| 62 | mlt               | Maltese               |               208 |       0.243 |    0.803 | 0.236 |     167 |   521 | 7568820 |     41 |
| 63 | pan               | Panjabi               |               196 |       1.000 |    1.000 | 1.000 |     196 |     0 | 7569353 |      0 |
| 64 | kan               | Kannada               |               176 |       1.000 |    1.000 | 1.000 |     176 |     0 | 7569373 |      0 |
| 65 | guj               | Gujarati              |               168 |       1.000 |    1.000 | 1.000 |     168 |     0 | 7569381 |      0 |
| 66 | hat               | Haitian               |                64 |       0.114 |    0.594 | 0.110 |      38 |   294 | 7569191 |     26 |
| 67 | sin               | Sinhala               |                45 |       1.000 |    1.000 | 1.000 |      45 |     0 | 7569504 |      0 |
| 68 | chr               | Cherokee              |                28 |       1.000 |    0.964 | 0.982 |      27 |     0 | 7569521 |      1 |
| 69 | kin               | Kinyarwanda           |                28 |       0.050 |    0.679 | 0.049 |      19 |   361 | 7569160 |      9 |
| 70 | div               | Dhivehi               |                26 |       1.000 |    1.000 | 1.000 |      26 |     0 | 7569523 |      0 |
| 71 | lug               | Ganda                 |                 2 |       0.032 |    1.000 | 0.032 |       2 |    60 | 7569487 |      0 |