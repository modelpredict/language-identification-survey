# Classification performance for gcld3 on tatoeba-sentences-2021-06-05-common-48

- Dataset coverage (sentences in supported languages): 7461627 (100.00%)
- **Aggregated accuracy: 86.98%**

<h2 id="supported-languages">Supported languages (107)</h2>

afr (Afrikaans), amh (Amharic), ara (Arabic), bul (Bulgarian), bul (Bulgarian), ben (Bangla), bos (Bosnian), cat (Catalan), ceb (Cebuano), cos (Corsican), ces (Czech), cym (Welsh), dan (Danish), deu (German), ell (Greek), ell (Greek), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fil (Filipino), fra (French), fry (Western Frisian), gle (Irish), gla (Scottish Gaelic), glg (Galician), guj (Gujarati), hau (Hausa), haw (Hawaiian), hin (Hindi), hin (Hindi), hmn (Hmong), hrv (Croatian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ind (Indonesian), ibo (Igbo), isl (Icelandic), ita (Italian), heb (Hebrew), jpn (Japanese), jpn (Japanese), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), kur (Kurdish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lao (Lao), lit (Lithuanian), lav (Latvian), mlg (Malagasy), mri (Maori), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), msa (Malay), mlt (Maltese), mya (Burmese), nep (Nepali), nld (Dutch), nob (Norwegian Bokmål), nya (Nyanja), pan (Punjabi), pol (Polish), pus (Pashto), por (Portuguese), ron (Romanian), rus (Russian), rus (Russian), snd (Sindhi), sin (Sinhala), slk (Slovak), slv (Slovenian), smo (Samoan), sna (Shona), som (Somali), sqi (Albanian), srp (Serbian), sot (Southern Sotho), sun (Sundanese), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tgk (Tajik), tha (Thai), tur (Turkish), ukr (Ukrainian), urd (Urdu), uzb (Uzbek), vie (Vietnamese), xho (Xhosa), yid (Yiddish), yor (Yoruba), zho (Chinese), zho (Chinese), zul (Zulu)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |     fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|-------:|
|  1 | eng               | English          |           1479733 |       0.995 |    0.851 | 0.915 | 1258584 |  6421 | 5975473 | 221149 |
|  2 | rus               | Russian          |            849653 |       0.975 |    0.858 | 0.903 |  729212 | 18499 | 6593475 | 120441 |
|  3 | ita               | Italian          |            787053 |       0.976 |    0.821 | 0.882 |  646316 | 16123 | 6658451 | 140737 |
|  4 | tur               | Turkish          |            709573 |       0.994 |    0.894 | 0.939 |  634612 |  3790 | 6748264 |  74961 |
|  5 | deu               | German           |            553727 |       0.978 |    0.933 | 0.945 |  516822 | 11764 | 6896136 |  36905 |
|  6 | fra               | French           |            466192 |       0.975 |    0.860 | 0.903 |  400941 | 10202 | 6985233 |  65251 |
|  7 | por               | Portuguese       |            385737 |       0.916 |    0.885 | 0.864 |  341427 | 31415 | 7044475 |  44310 |
|  8 | spa               | Spanish          |            338781 |       0.924 |    0.782 | 0.819 |  264941 | 21705 | 7101141 |  73840 |
|  9 | hun               | Hungarian        |            323048 |       0.969 |    0.895 | 0.917 |  289189 |  9311 | 7129268 |  33859 |
| 10 | jpn               | Japanese         |            208761 |       0.983 |    0.999 | 0.983 |  208552 |  3592 | 7249274 |    209 |
| 11 | heb               | Hebrew           |            197226 |       1.000 |    0.991 | 0.995 |  195374 |    48 | 7264353 |   1852 |
| 12 | ukr               | Ukrainian        |            171674 |       0.802 |    0.889 | 0.764 |  152579 | 37666 | 7252287 |  19095 |
| 13 | nld               | Dutch            |            144340 |       0.877 |    0.854 | 0.816 |  123199 | 17204 | 7300083 |  21141 |
| 14 | fin               | Finnish          |            128011 |       0.954 |    0.902 | 0.907 |  115404 |  5554 | 7328062 |  12607 |
| 15 | pol               | Polish           |            109662 |       0.918 |    0.931 | 0.888 |  102084 |  9094 | 7342871 |   7578 |
| 16 | mkd               | Macedonian       |             77938 |       0.875 |    0.741 | 0.759 |   57730 |  8238 | 7375451 |  20208 |
| 17 | mar               | Marathi          |             64126 |       0.989 |    0.911 | 0.944 |   58406 |   632 | 7396869 |   5720 |
| 18 | lit               | Lithuanian       |             59659 |       0.908 |    0.883 | 0.856 |   52661 |  5352 | 7396616 |   6998 |
| 19 | ces               | Czech            |             57030 |       0.885 |    0.813 | 0.803 |   46341 |  6049 | 7398548 |  10689 |
| 20 | dan               | Danish           |             49399 |       0.656 |    0.746 | 0.590 |   36848 | 19288 | 7392940 |  12551 |
| 21 | swe               | Swedish          |             41677 |       0.794 |    0.861 | 0.746 |   35870 |  9310 | 7410640 |   5807 |
| 22 | ara               | Arabic           |             35991 |       0.999 |    0.911 | 0.952 |   32774 |    30 | 7425606 |   3217 |
| 23 | ell               | Greek            |             34071 |       0.806 |    1.000 | 0.806 |   34062 |  8213 | 7419343 |      9 |
| 24 | ron               | Romanian         |             24943 |       0.623 |    0.808 | 0.580 |   20164 | 12187 | 7424497 |   4779 |
| 25 | bul               | Bulgarian        |             24503 |       0.327 |    0.844 | 0.318 |   20688 | 42483 | 7394641 |   3815 |
| 26 | vie               | Vietnamese       |             19234 |       0.890 |    0.981 | 0.882 |   18870 |  2332 | 7440061 |    364 |
| 27 | fil               | Filipino         |             16649 |       0.746 |    0.780 | 0.675 |   12994 |  4426 | 7440552 |   3655 |
| 28 | slk               | Slovak           |             14660 |       0.425 |    0.727 | 0.394 |   10664 | 14404 | 7432563 |   3996 |
| 29 | ind               | Indonesian       |             14542 |       0.688 |    0.640 | 0.577 |    9304 |  4210 | 7442875 |   5238 |
| 30 | hin               | Hindi            |             14230 |       0.527 |    0.880 | 0.509 |   12527 | 11232 | 7436165 |   1703 |
| 31 | nob               | Norwegian Bokmål |             14223 |       0.288 |    0.829 | 0.280 |   11791 | 29106 | 7418298 |   2432 |
| 32 | cat               | Catalan          |              7971 |       0.181 |    0.818 | 0.177 |    6520 | 29565 | 7424091 |   1451 |
| 33 | kor               | Korean           |              7570 |       0.917 |    0.996 | 0.915 |    7536 |   685 | 7453372 |     34 |
| 34 | hrv               | Croatian         |              5204 |       0.270 |    0.447 | 0.231 |    2324 |  6278 | 7450145 |   2880 |
| 35 | ben               | Bangla           |              4714 |       1.000 |    0.998 | 0.999 |    4704 |     0 | 7456913 |     10 |
| 36 | afr               | Afrikaans        |              4031 |       0.147 |    0.865 | 0.145 |    3485 | 20233 | 7437363 |    546 |
| 37 | est               | Estonian         |              3637 |       0.202 |    0.796 | 0.197 |    2894 | 11430 | 7446560 |    743 |
| 38 | tha               | Thai             |              3528 |       0.995 |    0.998 | 0.994 |    3522 |    18 | 7458081 |      6 |
| 39 | sqi               | Albanian         |              2526 |       0.332 |    0.865 | 0.323 |    2184 |  4404 | 7454697 |    342 |
| 40 | urd               | Urdu             |              2008 |       0.882 |    0.961 | 0.867 |    1930 |   257 | 7459362 |     78 |
| 41 | cym               | Welsh            |              1344 |       0.105 |    0.824 | 0.104 |    1108 |  9469 | 7450814 |    236 |
| 42 | slv               | Slovenian        |              1093 |       0.060 |    0.724 | 0.059 |     791 | 12479 | 7448055 |    302 |
| 43 | mal               | Malayalam        |               827 |       1.000 |    1.000 | 1.000 |     827 |     0 | 7460800 |      0 |
| 44 | tam               | Tamil            |               334 |       1.000 |    1.000 | 1.000 |     334 |     0 | 7461293 |      0 |
| 45 | tel               | Telugu           |               254 |       1.000 |    1.000 | 1.000 |     254 |     0 | 7461373 |      0 |
| 46 | pan               | Punjabi          |               196 |       1.000 |    0.995 | 0.997 |     195 |     0 | 7461431 |      1 |
| 47 | kan               | Kannada          |               176 |       1.000 |    1.000 | 1.000 |     176 |     0 | 7461451 |      0 |
| 48 | guj               | Gujarati         |               168 |       1.000 |    0.982 | 0.991 |     165 |     0 | 7461459 |      3 |