# Classification performance for langdetect on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 7461707 (77.40%)
- **Aggregated accuracy: 0.9245361684665453**

## Supported languages (55)
afr (Afrikaans), ara (Arabic), bul (Bulgarian), ben (Bangla), cat (Catalan), ces (Czech), cym (Welsh), dan (Danish), deu (German), ell (Greek), eng (English), spa (Spanish), est (Estonian), fas (Persian), fin (Finnish), fra (French), guj (Gujarati), heb (Hebrew), hin (Hindi), hrv (Croatian), hun (Hungarian), ind (Indonesian), ita (Italian), jpn (Japanese), kan (Kannada), kor (Korean), lit (Lithuanian), lav (Latvian), mkd (Macedonian), mal (Malayalam), mar (Marathi), nep (Nepali), nld (Dutch), nob (Norwegian Bokmål), pan (Punjabi), pol (Polish), por (Portuguese), ron (Romanian), rus (Russian), slk (Slovak), slv (Slovenian), som (Somali), sqi (Albanian), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tha (Thai), fil (Filipino), tur (Turkish), ukr (Ukrainian), urd (Urdu), vie (Vietnamese), zho (Chinese), zho (Chinese)

## Stats per language
|    | language_alpha3   | language             |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |    fn |
|---:|:------------------|:---------------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|------:|
|  1 | eng               | English              |           1479733 |       0.988 |    0.933 | 0.954 | 1380911 | 17010 | 5964964 | 98822 |
|  2 | rus               | Russian              |            849653 |       0.970 |    0.916 | 0.928 |  777866 | 24227 | 6587827 | 71787 |
|  3 | ita               | Italian              |            787053 |       0.973 |    0.897 | 0.922 |  705630 | 19337 | 6655317 | 81423 |
|  4 | tur               | Turkish              |            709573 |       0.996 |    0.971 | 0.982 |  689294 |  2589 | 6749545 | 20279 |
|  5 | deu               | German               |            553727 |       0.985 |    0.967 | 0.968 |  535363 |  8311 | 6899669 | 18364 |
|  6 | fra               | French               |            466192 |       0.945 |    0.946 | 0.920 |  441184 | 25895 | 6969620 | 25008 |
|  7 | por               | Portuguese           |            385737 |       0.877 |    0.899 | 0.836 |  346968 | 48757 | 7027213 | 38769 |
|  8 | spa               | Spanish              |            338781 |       0.917 |    0.830 | 0.838 |  281211 | 25423 | 7097503 | 57570 |
|  9 | hun               | Hungarian            |            323048 |       0.990 |    0.950 | 0.965 |  306776 |  3022 | 7135637 | 16272 |
| 10 | jpn               | Japanese             |            208761 |       1.000 |    0.999 | 1.000 |  208586 |     0 | 7252946 |   175 |
| 11 | heb               | Hebrew               |            197226 |       1.000 |    1.000 | 1.000 |  197225 |     0 | 7264481 |     1 |
| 12 | ukr               | Ukrainian            |            171674 |       0.895 |    0.796 | 0.803 |  136663 | 16080 | 7273953 | 35011 |
| 13 | nld               | Dutch                |            144340 |       0.871 |    0.815 | 0.793 |  117639 | 17432 | 7299935 | 26701 |
| 14 | fin               | Finnish              |            128011 |       0.943 |    0.971 | 0.930 |  124344 |  7534 | 7326162 |  3667 |
| 15 | pol               | Polish               |            109662 |       0.985 |    0.972 | 0.971 |  106595 |  1645 | 7350400 |  3067 |
| 16 | mkd               | Macedonian           |             77938 |       0.684 |    0.889 | 0.656 |   69298 | 32067 | 7351702 |  8640 |
| 17 | mar               | Marathi              |             64126 |       0.997 |    0.932 | 0.962 |   59783 |   194 | 7397387 |  4343 |
| 18 | lit               | Lithuanian           |             59659 |       0.933 |    0.944 | 0.907 |   56303 |  4063 | 7397985 |  3356 |
| 19 | ces               | Czech                |             57030 |       0.937 |    0.848 | 0.864 |   48335 |  3243 | 7401434 |  8695 |
| 20 | dan               | Danish               |             49399 |       0.695 |    0.697 | 0.604 |   34415 | 15080 | 7397228 | 14984 |
| 21 | swe               | Swedish              |             41677 |       0.815 |    0.852 | 0.761 |   35494 |  8039 | 7411991 |  6183 |
| 22 | ara               | Arabic               |             35991 |       1.000 |    0.979 | 0.989 |   35240 |     4 | 7425712 |   751 |
| 23 | ell               | Modern Greek (1453-) |             34071 |       1.000 |    1.000 | 1.000 |   34071 |     2 | 7427634 |     0 |
| 24 | ron               | Romanian             |             24943 |       0.539 |    0.942 | 0.531 |   23490 | 20051 | 7416713 |  1453 |
| 25 | bul               | Bulgarian            |             24503 |       0.284 |    0.782 | 0.273 |   19154 | 48399 | 7388805 |  5349 |
| 26 | vie               | Vietnamese           |             19234 |       0.969 |    0.999 | 0.969 |   19220 |   607 | 7441866 |    14 |
| 27 | fil               | Filipino             |             16649 |       0.579 |    0.941 | 0.568 |   15674 | 11413 | 7433645 |   975 |
| 28 | slk               | Slovak               |             14660 |       0.519 |    0.762 | 0.480 |   11167 | 10366 | 7436681 |  3493 |
| 29 | ind               | Indonesian           |             14542 |       0.495 |    0.942 | 0.488 |   13698 | 13963 | 7433202 |   844 |
| 30 | hin               | Hindi                |             14230 |       0.786 |    0.957 | 0.773 |   13618 |  3697 | 7443780 |   612 |
| 31 | nob               | Norwegian Bokmål     |             14223 |       0.251 |    0.818 | 0.244 |   11639 | 34806 | 7412678 |  2584 |
| 32 | cat               | Catalan              |              7971 |       0.143 |    0.841 | 0.141 |    6702 | 40066 | 7413670 |  1269 |
| 33 | kor               | Korean               |              7570 |       0.985 |    0.999 | 0.984 |    7559 |   119 | 7454018 |    11 |
| 34 | hrv               | Croatian             |              5204 |       0.334 |    0.805 | 0.321 |    4189 |  8362 | 7448141 |  1015 |
| 35 | ben               | Bengali              |              4714 |       1.000 |    1.000 | 1.000 |    4714 |     0 | 7456993 |     0 |
| 36 | afr               | Afrikaans            |              4031 |       0.072 |    0.854 | 0.071 |    3441 | 44440 | 7413236 |   590 |
| 37 | est               | Estonian             |              3637 |       0.196 |    0.860 | 0.193 |    3129 | 12850 | 7445220 |   508 |
| 38 | tha               | Thai                 |              3528 |       1.000 |    1.000 | 1.000 |    3528 |     0 | 7458179 |     0 |
| 39 | sqi               | Albanian             |              2526 |       0.564 |    0.947 | 0.555 |    2391 |  1846 | 7457335 |   135 |
| 40 | urd               | Urdu                 |              2008 |       0.922 |    0.992 | 0.918 |    1991 |   169 | 7459530 |    17 |
| 41 | cym               | Welsh                |              1344 |       0.142 |    0.940 | 0.142 |    1264 |  7614 | 7452749 |    80 |
| 42 | slv               | Slovenian            |              1093 |       0.074 |    0.752 | 0.073 |     822 | 10262 | 7450352 |   271 |
| 43 | mal               | Malayalam            |               827 |       1.000 |    1.000 | 1.000 |     827 |     0 | 7460880 |     0 |
| 44 | tam               | Tamil                |               334 |       1.000 |    1.000 | 1.000 |     334 |     0 | 7461373 |     0 |
| 45 | tel               | Telugu               |               254 |       1.000 |    1.000 | 1.000 |     254 |     0 | 7461453 |     0 |
| 46 | pan               | Panjabi              |               196 |       1.000 |    1.000 | 1.000 |     196 |     0 | 7461511 |     0 |
| 47 | kan               | Kannada              |               176 |       1.000 |    1.000 | 1.000 |     176 |     0 | 7461531 |     0 |
| 48 | guj               | Gujarati             |               168 |       1.000 |    1.000 | 1.000 |     168 |     0 | 7461539 |     0 |
| 49 | som               | Somali               |                80 |       0.014 |    0.988 | 0.014 |      79 |  5524 | 7456103 |     1 |