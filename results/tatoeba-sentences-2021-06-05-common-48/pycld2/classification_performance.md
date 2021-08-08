# Classification performance for pycld2 on tatoeba-sentences-2021-06-05-common-48

- Dataset coverage (sentences in supported languages): 7461627 (100.00%)
- **Aggregated accuracy: 87.12%**

<h2 id="supported-languages">Supported languages (83)</h2>

afr (Afrikaans), sqi (Albanian), ara (Arabic), hye (Armenian), aze (Azerbaijani), eus (Basque), bel (Belarusian), ben (Bangla), bih (Bihari languages), bul (Bulgarian), cat (Catalan), ceb (Cebuano), chr (Cherokee), hrv (Croatian), ces (Czech), zho (Chinese), dan (Danish), div (Divehi), nld (Dutch), eng (English), est (Estonian), fin (Finnish), fra (French), glg (Galician), lug (Ganda), kat (Georgian), deu (German), ell (Greek), guj (Gujarati), hat (Haitian Creole), heb (Hebrew), hin (Hindi), hmn (Hmong), hun (Hungarian), isl (Icelandic), ind (Indonesian), iku (Inuktitut), gle (Irish), ita (Italian), jav (Javanese), jpn (Japanese), kan (Kannada), khm (Khmer), kin (Kinyarwanda), kor (Korean), lao (Lao), lav (Latvian), lif (Limbu), lit (Lithuanian), mkd (Macedonian), msa (Malay), mal (Malayalam), mlt (Maltese), mar (Marathi), nep (Nepali), nob (Norwegian Bokmål), ori (Odia), fas (Persian), pol (Polish), por (Portuguese), pan (Punjabi), ron (Romanian), rus (Russian), gla (Scottish Gaelic), srp (Serbian), sin (Sinhala), slk (Slovak), slv (Slovenian), spa (Spanish), swa (Swahili), swe (Swedish), syr (Syriac), fil (Filipino), tam (Tamil), tel (Telugu), tha (Thai), tur (Turkish), ukr (Ukrainian), urd (Urdu), vie (Vietnamese), cym (Welsh), yid (Yiddish), zho (Chinese)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |     fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|-------:|
|  1 | eng               | English          |           1479733 |       0.955 |    0.970 | 0.941 | 1435203 | 68178 | 5913716 |  44530 |
|  2 | rus               | Russian          |            849653 |       0.998 |    0.830 | 0.905 |  705549 |  1619 | 6610355 | 144104 |
|  3 | ita               | Italian          |            787053 |       0.999 |    0.689 | 0.816 |  542549 |   441 | 6674133 | 244504 |
|  4 | tur               | Turkish          |            709573 |       1.000 |    0.923 | 0.960 |  654731 |   110 | 6751944 |  54842 |
|  5 | deu               | German           |            553727 |       1.000 |    0.954 | 0.976 |  528244 |   180 | 6907720 |  25483 |
|  6 | fra               | French           |            466192 |       0.999 |    0.845 | 0.915 |  394106 |   372 | 6995063 |  72086 |
|  7 | por               | Portuguese       |            385737 |       0.982 |    0.865 | 0.912 |  333763 |  6080 | 7069810 |  51974 |
|  8 | spa               | Spanish          |            338781 |       0.995 |    0.798 | 0.883 |  270207 |  1476 | 7121370 |  68574 |
|  9 | hun               | Hungarian        |            323048 |       1.000 |    0.935 | 0.966 |  302013 |   131 | 7138448 |  21035 |
| 10 | jpn               | Japanese         |            208761 |       1.000 |    0.999 | 1.000 |  208635 |     0 | 7252866 |    126 |
| 11 | heb               | Hebrew           |            197226 |       1.000 |    0.841 | 0.914 |  165882 |     4 | 7264397 |  31344 |
| 12 | ukr               | Ukrainian        |            171674 |       0.992 |    0.791 | 0.877 |  135799 |  1148 | 7288805 |  35875 |
| 13 | nld               | Dutch            |            144340 |       0.994 |    0.820 | 0.897 |  118356 |   664 | 7316623 |  25984 |
| 14 | fin               | Finnish          |            128011 |       0.999 |    0.909 | 0.951 |  116372 |   159 | 7333457 |  11639 |
| 15 | pol               | Polish           |            109662 |       0.999 |    0.926 | 0.961 |  101512 |    68 | 7351897 |   8150 |
| 16 | mkd               | Macedonian       |             77938 |       0.973 |    0.477 | 0.635 |   37213 |  1038 | 7382651 |  40725 |
| 17 | mar               | Marathi          |             64126 |       1.000 |    0.967 | 0.983 |   62024 |    24 | 7397477 |   2102 |
| 18 | lit               | Lithuanian       |             59659 |       0.997 |    0.914 | 0.952 |   54501 |   144 | 7401824 |   5158 |
| 19 | ces               | Czech            |             57030 |       0.971 |    0.891 | 0.917 |   50816 |  1511 | 7403086 |   6214 |
| 20 | dan               | Danish           |             49399 |       0.866 |    0.698 | 0.730 |   34494 |  5317 | 7406911 |  14905 |
| 21 | swe               | Swedish          |             41677 |       0.995 |    0.761 | 0.861 |   31709 |   145 | 7419805 |   9968 |
| 22 | ara               | Arabic           |             35991 |       1.000 |    0.776 | 0.874 |   27916 |     1 | 7425635 |   8075 |
| 23 | ell               | Greek            |             34071 |       1.000 |    1.000 | 1.000 |   34071 |    14 | 7427542 |      0 |
| 24 | ron               | Romanian         |             24943 |       0.963 |    0.811 | 0.866 |   20227 |   780 | 7435904 |   4716 |
| 25 | bul               | Bulgarian        |             24503 |       0.854 |    0.700 | 0.722 |   17140 |  2925 | 7434199 |   7363 |
| 26 | vie               | Vietnamese       |             19234 |       0.995 |    0.991 | 0.990 |   19062 |   103 | 7442290 |    172 |
| 27 | fil               | Filipino         |             16649 |       0.994 |    0.789 | 0.878 |   13136 |    75 | 7444903 |   3513 |
| 28 | slk               | Slovak           |             14660 |       0.704 |    0.788 | 0.643 |   11559 |  4854 | 7442113 |   3101 |
| 29 | ind               | Indonesian       |             14542 |       0.867 |    0.775 | 0.770 |   11270 |  1727 | 7445358 |   3272 |
| 30 | hin               | Hindi            |             14230 |       0.918 |    0.973 | 0.907 |   13848 |  1230 | 7446167 |    382 |
| 31 | nob               | Norwegian Bokmål |             14223 |       0.566 |    0.796 | 0.528 |   11327 |  8676 | 7438728 |   2896 |
| 32 | cat               | Catalan          |              7971 |       0.807 |    0.685 | 0.681 |    5464 |  1305 | 7452351 |   2507 |
| 33 | kor               | Korean           |              7570 |       1.000 |    0.991 | 0.995 |    7500 |     0 | 7454057 |     70 |
| 34 | hrv               | Croatian         |              5204 |       0.940 |    0.565 | 0.690 |    2942 |   189 | 7456234 |   2262 |
| 35 | ben               | Bangla           |              4714 |       1.000 |    0.777 | 0.874 |    3662 |     0 | 7456913 |   1052 |
| 36 | afr               | Afrikaans        |              4031 |       0.446 |    0.826 | 0.426 |    3330 |  4129 | 7453467 |    701 |
| 37 | est               | Estonian         |              3637 |       0.908 |    0.752 | 0.790 |    2734 |   276 | 7457714 |    903 |
| 38 | tha               | Thai             |              3528 |       1.000 |    1.000 | 1.000 |    3528 |     0 | 7458099 |      0 |
| 39 | sqi               | Albanian         |              2526 |       0.962 |    0.909 | 0.918 |    2295 |    90 | 7459011 |    231 |
| 40 | urd               | Urdu             |              2008 |       0.997 |    0.948 | 0.971 |    1903 |     5 | 7459614 |    105 |
| 41 | cym               | Welsh            |              1344 |       0.968 |    0.845 | 0.890 |    1136 |    37 | 7460246 |    208 |
| 42 | slv               | Slovenian        |              1093 |       0.802 |    0.550 | 0.604 |     601 |   148 | 7460386 |    492 |
| 43 | mal               | Malayalam        |               827 |       1.000 |    1.000 | 1.000 |     827 |     0 | 7460800 |      0 |
| 44 | tam               | Tamil            |               334 |       1.000 |    1.000 | 1.000 |     334 |     0 | 7461293 |      0 |
| 45 | tel               | Telugu           |               254 |       1.000 |    1.000 | 1.000 |     254 |     0 | 7461373 |      0 |
| 46 | pan               | Punjabi          |               196 |       1.000 |    1.000 | 1.000 |     196 |     0 | 7461431 |      0 |
| 47 | kan               | Kannada          |               176 |       1.000 |    1.000 | 1.000 |     176 |     0 | 7461451 |      0 |
| 48 | guj               | Gujarati         |               168 |       1.000 |    1.000 | 1.000 |     168 |     0 | 7461459 |      0 |