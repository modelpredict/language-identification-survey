# Classification performance for langdetect on tatoeba-sentences-2021-06-05-common-48

- Dataset coverage (sentences in supported languages): 7461627 (100.00%)
- **Aggregated accuracy: 0.9246825122724575**

<h2 id="supported-languages">Supported languages (55)</h2>

afr (Afrikaans), ara (Arabic), bul (Bulgarian), ben (Bangla), cat (Catalan), ces (Czech), cym (Welsh), dan (Danish), deu (German), ell (Greek), eng (English), spa (Spanish), est (Estonian), fas (Persian), fin (Finnish), fra (French), guj (Gujarati), heb (Hebrew), hin (Hindi), hrv (Croatian), hun (Hungarian), ind (Indonesian), ita (Italian), jpn (Japanese), kan (Kannada), kor (Korean), lit (Lithuanian), lav (Latvian), mkd (Macedonian), mal (Malayalam), mar (Marathi), nep (Nepali), nld (Dutch), nob (Norwegian Bokmål), pan (Punjabi), pol (Polish), por (Portuguese), ron (Romanian), rus (Russian), slk (Slovak), slv (Slovenian), som (Somali), sqi (Albanian), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tha (Thai), fil (Filipino), tur (Turkish), ukr (Ukrainian), urd (Urdu), vie (Vietnamese), zho (Chinese), zho (Chinese)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |    fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|------:|
|  1 | eng               | English          |           1479733 |       0.988 |    0.933 | 0.954 | 1381214 | 16940 | 5964954 | 98519 |
|  2 | rus               | Russian          |            849653 |       0.970 |    0.916 | 0.928 |  778060 | 24120 | 6587854 | 71593 |
|  3 | ita               | Italian          |            787053 |       0.974 |    0.897 | 0.922 |  705735 | 19187 | 6655387 | 81318 |
|  4 | tur               | Turkish          |            709573 |       0.996 |    0.971 | 0.982 |  689314 |  2543 | 6749511 | 20259 |
|  5 | deu               | German           |            553727 |       0.985 |    0.967 | 0.969 |  535515 |  8255 | 6899645 | 18212 |
|  6 | fra               | French           |            466192 |       0.944 |    0.947 | 0.920 |  441289 | 25946 | 6969489 | 24903 |
|  7 | por               | Portuguese       |            385737 |       0.877 |    0.900 | 0.836 |  346971 | 48693 | 7027197 | 38766 |
|  8 | spa               | Spanish          |            338781 |       0.916 |    0.831 | 0.838 |  281382 | 25647 | 7097199 | 57399 |
|  9 | hun               | Hungarian        |            323048 |       0.991 |    0.950 | 0.965 |  306757 |  2935 | 7135644 | 16291 |
| 10 | jpn               | Japanese         |            208761 |       1.000 |    0.999 | 1.000 |  208592 |     0 | 7252866 |   169 |
| 11 | heb               | Hebrew           |            197226 |       1.000 |    1.000 | 1.000 |  197226 |     0 | 7264401 |     0 |
| 12 | ukr               | Ukrainian        |            171674 |       0.895 |    0.796 | 0.803 |  136621 | 15996 | 7273957 | 35053 |
| 13 | nld               | Dutch            |            144340 |       0.872 |    0.815 | 0.793 |  117650 | 17344 | 7299943 | 26690 |
| 14 | fin               | Finnish          |            128011 |       0.943 |    0.971 | 0.930 |  124354 |  7511 | 7326105 |  3657 |
| 15 | pol               | Polish           |            109662 |       0.985 |    0.972 | 0.971 |  106609 |  1641 | 7350324 |  3053 |
| 16 | mkd               | Macedonian       |             77938 |       0.684 |    0.889 | 0.656 |   69298 | 32058 | 7351631 |  8640 |
| 17 | mar               | Marathi          |             64126 |       0.997 |    0.932 | 0.962 |   59755 |   190 | 7397311 |  4371 |
| 18 | lit               | Lithuanian       |             59659 |       0.934 |    0.944 | 0.908 |   56302 |  4006 | 7397962 |  3357 |
| 19 | ces               | Czech            |             57030 |       0.937 |    0.848 | 0.865 |   48335 |  3225 | 7401372 |  8695 |
| 20 | dan               | Danish           |             49399 |       0.697 |    0.697 | 0.606 |   34438 | 14948 | 7397280 | 14961 |
| 21 | swe               | Swedish          |             41677 |       0.815 |    0.852 | 0.761 |   35494 |  8046 | 7411904 |  6183 |
| 22 | ara               | Arabic           |             35991 |       1.000 |    0.979 | 0.989 |   35231 |     4 | 7425632 |   760 |
| 23 | ell               | Greek            |             34071 |       1.000 |    1.000 | 1.000 |   34071 |     2 | 7427554 |     0 |
| 24 | ron               | Romanian         |             24943 |       0.541 |    0.942 | 0.532 |   23508 | 19948 | 7416736 |  1435 |
| 25 | bul               | Bulgarian        |             24503 |       0.284 |    0.783 | 0.273 |   19182 | 48422 | 7388702 |  5321 |
| 26 | vie               | Vietnamese       |             19234 |       0.971 |    0.999 | 0.970 |   19220 |   580 | 7441813 |    14 |
| 27 | fil               | Filipino         |             16649 |       0.579 |    0.943 | 0.569 |   15707 | 11441 | 7433537 |   942 |
| 28 | slk               | Slovak           |             14660 |       0.520 |    0.762 | 0.481 |   11175 | 10312 | 7436655 |  3485 |
| 29 | ind               | Indonesian       |             14542 |       0.496 |    0.943 | 0.488 |   13717 | 13953 | 7433132 |   825 |
| 30 | hin               | Hindi            |             14230 |       0.785 |    0.957 | 0.772 |   13622 |  3722 | 7443675 |   608 |
| 31 | nob               | Norwegian Bokmål |             14223 |       0.250 |    0.816 | 0.243 |   11613 | 34844 | 7412560 |  2610 |
| 32 | cat               | Catalan          |              7971 |       0.143 |    0.839 | 0.141 |    6686 | 39974 | 7413682 |  1285 |
| 33 | kor               | Korean           |              7570 |       0.986 |    0.999 | 0.985 |    7560 |   108 | 7453949 |    10 |
| 34 | hrv               | Croatian         |              5204 |       0.333 |    0.803 | 0.320 |    4181 |  8360 | 7448063 |  1023 |
| 35 | ben               | Bangla           |              4714 |       1.000 |    1.000 | 1.000 |    4714 |     0 | 7456913 |     0 |
| 36 | afr               | Afrikaans        |              4031 |       0.072 |    0.855 | 0.072 |    3447 | 44438 | 7413158 |   584 |
| 37 | est               | Estonian         |              3637 |       0.195 |    0.859 | 0.192 |    3124 | 12874 | 7445116 |   513 |
| 38 | tha               | Thai             |              3528 |       1.000 |    1.000 | 1.000 |    3528 |     0 | 7458099 |     0 |
| 39 | sqi               | Albanian         |              2526 |       0.571 |    0.947 | 0.562 |    2391 |  1794 | 7457307 |   135 |
| 40 | urd               | Urdu             |              2008 |       0.921 |    0.992 | 0.918 |    1992 |   170 | 7459449 |    16 |
| 41 | cym               | Welsh            |              1344 |       0.143 |    0.940 | 0.142 |    1263 |  7564 | 7452719 |    81 |
| 42 | slv               | Slovenian        |              1093 |       0.076 |    0.767 | 0.075 |     838 | 10179 | 7450355 |   255 |
| 43 | mal               | Malayalam        |               827 |       1.000 |    1.000 | 1.000 |     827 |     0 | 7460800 |     0 |
| 44 | tam               | Tamil            |               334 |       1.000 |    1.000 | 1.000 |     334 |     0 | 7461293 |     0 |
| 45 | tel               | Telugu           |               254 |       1.000 |    1.000 | 1.000 |     254 |     0 | 7461373 |     0 |
| 46 | pan               | Punjabi          |               196 |       1.000 |    1.000 | 1.000 |     196 |     0 | 7461431 |     0 |
| 47 | kan               | Kannada          |               176 |       1.000 |    1.000 | 1.000 |     176 |     0 | 7461451 |     0 |
| 48 | guj               | Gujarati         |               168 |       1.000 |    1.000 | 1.000 |     168 |     0 | 7461459 |     0 |