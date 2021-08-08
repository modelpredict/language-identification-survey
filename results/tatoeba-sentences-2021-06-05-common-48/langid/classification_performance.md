# Classification performance for langid on tatoeba-sentences-2021-06-05-common-48

- Dataset coverage (sentences in supported languages): 7461627 (100.00%)
- **Aggregated accuracy: 90.15%**

<h2 id="supported-languages">Supported languages (97)</h2>

afr (Afrikaans), amh (Amharic), arg (Aragonese), ara (Arabic), asm (Assamese), aze (Azerbaijani), bel (Belarusian), bul (Bulgarian), ben (Bangla), bre (Breton), bos (Bosnian), cat (Catalan), ces (Czech), cym (Welsh), dan (Danish), deu (German), dzo (Dzongkha), ell (Greek), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fao (Faroese), fra (French), gle (Irish), glg (Galician), guj (Gujarati), heb (Hebrew), hin (Hindi), hrv (Croatian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ind (Indonesian), isl (Icelandic), ita (Italian), jpn (Japanese), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), kur (Kurdish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lao (Lao), lit (Lithuanian), lav (Latvian), mlg (Malagasy), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), msa (Malay), mlt (Maltese), nob (Norwegian Bokmål), nep (Nepali), nld (Dutch), nno (Norwegian Nynorsk), nob (Norwegian Bokmål), oci (Occitan), ori (Odia), pan (Punjabi), pol (Polish), pus (Pashto), por (Portuguese), que (Quechua), ron (Romanian), rus (Russian), kin (Kinyarwanda), sme (Northern Sami), sin (Sinhala), slk (Slovak), slv (Slovenian), sqi (Albanian), srp (Serbian), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tha (Thai), fil (Filipino), tur (Turkish), uig (Uyghur), ukr (Ukrainian), urd (Urdu), vie (Vietnamese), vol (Volapük), wln (Walloon), xho (Xhosa), zho (Chinese), zul (Zulu)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |     fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|-------:|
|  1 | eng               | English          |           1479733 |       0.965 |    0.973 | 0.952 | 1439789 | 52447 | 5929447 |  39944 |
|  2 | rus               | Russian          |            849653 |       0.968 |    0.823 | 0.876 |  699008 | 23301 | 6588673 | 150645 |
|  3 | ita               | Italian          |            787053 |       0.973 |    0.885 | 0.915 |  696690 | 19395 | 6655179 |  90363 |
|  4 | tur               | Turkish          |            709573 |       0.997 |    0.919 | 0.955 |  652061 |  1817 | 6750237 |  57512 |
|  5 | deu               | German           |            553727 |       0.958 |    0.974 | 0.946 |  539237 | 23461 | 6884439 |  14490 |
|  6 | fra               | French           |            466192 |       0.921 |    0.935 | 0.893 |  436032 | 37228 | 6958207 |  30160 |
|  7 | por               | Portuguese       |            385737 |       0.936 |    0.822 | 0.850 |  317068 | 21734 | 7054156 |  68669 |
|  8 | spa               | Spanish          |            338781 |       0.863 |    0.837 | 0.796 |  283448 | 45158 | 7077688 |  55333 |
|  9 | hun               | Hungarian        |            323048 |       0.980 |    0.929 | 0.944 |  300114 |  6226 | 7132353 |  22934 |
| 10 | jpn               | Japanese         |            208761 |       0.999 |    1.000 | 0.999 |  208702 |   109 | 7252757 |     59 |
| 11 | heb               | Hebrew           |            197226 |       1.000 |    0.999 | 1.000 |  197110 |    10 | 7264391 |    116 |
| 12 | ukr               | Ukrainian        |            171674 |       0.751 |    0.774 | 0.677 |  132961 | 44090 | 7245863 |  38713 |
| 13 | nld               | Dutch            |            144340 |       0.885 |    0.901 | 0.844 |  130115 | 16989 | 7300298 |  14225 |
| 14 | fin               | Finnish          |            128011 |       0.953 |    0.931 | 0.920 |  119175 |  5915 | 7327701 |   8836 |
| 15 | pol               | Polish           |            109662 |       0.960 |    0.977 | 0.950 |  107088 |  4405 | 7347560 |   2574 |
| 16 | mkd               | Macedonian       |             77938 |       0.619 |    0.482 | 0.464 |   37554 | 23137 | 7360552 |  40384 |
| 17 | mar               | Marathi          |             64126 |       0.988 |    0.700 | 0.815 |   44902 |   563 | 7396938 |  19224 |
| 18 | lit               | Lithuanian       |             59659 |       0.909 |    0.915 | 0.872 |   54565 |  5495 | 7396473 |   5094 |
| 19 | ces               | Czech            |             57030 |       0.893 |    0.837 | 0.822 |   47732 |  5701 | 7398896 |   9298 |
| 20 | dan               | Danish           |             49399 |       0.767 |    0.602 | 0.612 |   29753 |  9059 | 7403169 |  19646 |
| 21 | swe               | Swedish          |             41677 |       0.808 |    0.802 | 0.735 |   33438 |  7931 | 7412019 |   8239 |
| 22 | ara               | Arabic           |             35991 |       0.999 |    0.950 | 0.973 |   34184 |    30 | 7425606 |   1807 |
| 23 | ell               | Greek            |             34071 |       1.000 |    1.000 | 1.000 |   34071 |    14 | 7427542 |      0 |
| 24 | ron               | Romanian         |             24943 |       0.696 |    0.906 | 0.671 |   22605 |  9895 | 7426789 |   2338 |
| 25 | bul               | Bulgarian        |             24503 |       0.211 |    0.624 | 0.199 |   15278 | 57018 | 7380106 |   9225 |
| 26 | vie               | Vietnamese       |             19234 |       0.959 |    0.998 | 0.958 |   19192 |   819 | 7441574 |     42 |
| 27 | fil               | Filipino         |             16649 |       0.907 |    0.792 | 0.810 |   13181 |  1357 | 7443621 |   3468 |
| 28 | slk               | Slovak           |             14660 |       0.545 |    0.690 | 0.486 |   10119 |  8443 | 7438524 |   4541 |
| 29 | ind               | Indonesian       |             14542 |       0.615 |    0.731 | 0.553 |   10632 |  6650 | 7440435 |   3910 |
| 30 | hin               | Hindi            |             14230 |       0.420 |    0.901 | 0.410 |   12825 | 17724 | 7429673 |   1405 |
| 31 | nob               | Norwegian Bokmål |             14223 |       0.315 |    0.770 | 0.301 |   10958 | 23798 | 7423606 |   3265 |
| 32 | cat               | Catalan          |              7971 |       0.218 |    0.720 | 0.209 |    5739 | 20640 | 7433016 |   2232 |
| 33 | kor               | Korean           |              7570 |       0.990 |    1.000 | 0.990 |    7568 |    77 | 7453980 |      2 |
| 34 | hrv               | Croatian         |              5204 |       0.482 |    0.650 | 0.427 |    3384 |  3631 | 7452792 |   1820 |
| 35 | ben               | Bangla           |              4714 |       0.999 |    0.977 | 0.988 |    4605 |     3 | 7456910 |    109 |
| 36 | afr               | Afrikaans        |              4031 |       0.322 |    0.462 | 0.271 |    1861 |  3919 | 7453677 |   2170 |
| 37 | est               | Estonian         |              3637 |       0.306 |    0.689 | 0.286 |    2505 |  5688 | 7452302 |   1132 |
| 38 | tha               | Thai             |              3528 |       0.999 |    1.000 | 0.999 |    3528 |     3 | 7458096 |      0 |
| 39 | sqi               | Albanian         |              2526 |       0.805 |    0.905 | 0.772 |    2285 |   555 | 7458546 |    241 |
| 40 | urd               | Urdu             |              2008 |       0.855 |    0.947 | 0.835 |    1901 |   322 | 7459297 |    107 |
| 41 | cym               | Welsh            |              1344 |       0.330 |    0.682 | 0.306 |     916 |  1860 | 7458423 |    428 |
| 42 | slv               | Slovenian        |              1093 |       0.079 |    0.681 | 0.078 |     744 |  8640 | 7451894 |    349 |
| 43 | mal               | Malayalam        |               827 |       1.000 |    1.000 | 1.000 |     827 |     0 | 7460800 |      0 |
| 44 | tam               | Tamil            |               334 |       0.991 |    1.000 | 0.991 |     334 |     3 | 7461290 |      0 |
| 45 | tel               | Telugu           |               254 |       1.000 |    1.000 | 1.000 |     254 |     0 | 7461373 |      0 |
| 46 | pan               | Punjabi          |               196 |       0.990 |    1.000 | 0.990 |     196 |     2 | 7461429 |      0 |
| 47 | kan               | Kannada          |               176 |       1.000 |    1.000 | 1.000 |     176 |     0 | 7461451 |      0 |
| 48 | guj               | Gujarati         |               168 |       0.971 |    1.000 | 0.971 |     168 |     5 | 7461454 |      0 |