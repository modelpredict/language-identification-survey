# Classification performance for langid on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 4236418 (100.00%)
- **Aggregated accuracy: 74.19%**

<h2 id="supported-languages">Supported languages (97)</h2>

afr (Afrikaans), amh (Amharic), arg (Aragonese), ara (Arabic), asm (Assamese), aze (Azerbaijani), bel (Belarusian), bul (Bulgarian), ben (Bangla), bre (Breton), bos (Bosnian), cat (Catalan), ces (Czech), cym (Welsh), dan (Danish), deu (German), dzo (Dzongkha), ell (Greek), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fao (Faroese), fra (French), gle (Irish), glg (Galician), guj (Gujarati), heb (Hebrew), hin (Hindi), hrv (Croatian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ind (Indonesian), isl (Icelandic), ita (Italian), jpn (Japanese), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), kur (Kurdish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lao (Lao), lit (Lithuanian), lav (Latvian), mlg (Malagasy), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), msa (Malay), mlt (Maltese), nob (Norwegian Bokmål), nep (Nepali), nld (Dutch), nno (Norwegian Nynorsk), nob (Norwegian Bokmål), oci (Occitan), ori (Odia), pan (Punjabi), pol (Polish), pus (Pashto), por (Portuguese), que (Quechua), ron (Romanian), rus (Russian), kin (Kinyarwanda), sme (Northern Sami), sin (Sinhala), slk (Slovak), slv (Slovenian), sqi (Albanian), srp (Serbian), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tha (Thai), fil (Filipino), tur (Turkish), uig (Uyghur), ukr (Ukrainian), urd (Urdu), vie (Vietnamese), vol (Volapük), wln (Walloon), xho (Xhosa), zho (Chinese), zul (Zulu)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |    tp |     fp |      tn |    fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|------:|-------:|--------:|------:|
|  1 | ell               | Greek            |            100000 |       0.999 |    0.996 | 0.998 | 99645 |     69 | 4136349 |   355 |
|  2 | swe               | Swedish          |            100000 |       0.856 |    0.710 | 0.728 | 70956 |  11937 | 4124481 | 29044 |
|  3 | mkd               | Macedonian       |            100000 |       0.782 |    0.433 | 0.517 | 43309 |  12082 | 4124336 | 56691 |
|  4 | tha               | Thai             |            100000 |       1.000 |    0.961 | 0.980 | 96095 |     20 | 4136398 |  3905 |
|  5 | cat               | Catalan          |            100000 |       0.930 |    0.505 | 0.639 | 50550 |   3830 | 4132588 | 49450 |
|  6 | bul               | Bulgarian        |            100000 |       0.689 |    0.570 | 0.547 | 57031 |  25798 | 4110620 | 42969 |
|  7 | fin               | Finnish          |            100000 |       0.813 |    0.826 | 0.749 | 82642 |  18954 | 4117464 | 17358 |
|  8 | dan               | Danish           |            100000 |       0.674 |    0.521 | 0.514 | 52077 |  25239 | 4111179 | 47923 |
|  9 | hun               | Hungarian        |            100000 |       0.884 |    0.795 | 0.794 | 79534 |  10437 | 4125981 | 20466 |
| 10 | kor               | Korean           |            100000 |       0.999 |    0.962 | 0.980 | 96165 |     68 | 4136350 |  3835 |
| 11 | spa               | Spanish          |            100000 |       0.615 |    0.719 | 0.549 | 71937 |  44996 | 4091422 | 28063 |
| 12 | zho               | Chinese          |            100000 |       0.890 |    0.916 | 0.855 | 91584 |  11311 | 4125107 |  8416 |
| 13 | slk               | Slovak           |            100000 |       0.796 |    0.575 | 0.615 | 57535 |  14775 | 4121643 | 42465 |
| 14 | ron               | Romanian         |            100000 |       0.934 |    0.682 | 0.767 | 68239 |   4830 | 4131588 | 31761 |
| 15 | ind               | Indonesian       |            100000 |       0.875 |    0.529 | 0.630 | 52912 |   7540 | 4128878 | 47088 |
| 16 | est               | Estonian         |            100000 |       0.867 |    0.632 | 0.692 | 63160 |   9726 | 4126692 | 36840 |
| 17 | por               | Portuguese       |            100000 |       0.833 |    0.646 | 0.678 | 64621 |  12978 | 4123440 | 35379 |
| 18 | hrv               | Croatian         |            100000 |       0.803 |    0.505 | 0.576 | 50470 |  12351 | 4124067 | 49530 |
| 19 | heb               | Hebrew           |            100000 |       0.999 |    0.974 | 0.985 | 97363 |    121 | 4136297 |  2637 |
| 20 | ita               | Italian          |            100000 |       0.729 |    0.711 | 0.635 | 71086 |  26488 | 4109930 | 28914 |
| 21 | slv               | Slovenian        |            100000 |       0.631 |    0.569 | 0.509 | 56891 |  33249 | 4103169 | 43109 |
| 22 | ces               | Czech            |            100000 |       0.768 |    0.694 | 0.657 | 69366 |  20953 | 4115465 | 30634 |
| 23 | mal               | Malayalam        |            100000 |       1.000 |    0.977 | 0.988 | 97661 |      2 | 4136416 |  2339 |
| 24 | lit               | Lithuanian       |            100000 |       0.821 |    0.710 | 0.703 | 71019 |  15497 | 4120921 | 28981 |
| 25 | ukr               | Ukrainian        |            100000 |       0.805 |    0.500 | 0.574 | 49995 |  12080 | 4124338 | 50005 |
| 26 | pol               | Polish           |            100000 |       0.841 |    0.862 | 0.787 | 86150 |  16323 | 4120095 | 13850 |
| 27 | fas               | Persian          |            100000 |       0.830 |    0.526 | 0.604 | 52589 |  10748 | 4125670 | 47411 |
| 28 | jpn               | Japanese         |            100000 |       0.974 |    0.966 | 0.957 | 96556 |   2623 | 4133795 |  3444 |
| 29 | hin               | Hindi            |            100000 |       0.999 |    0.788 | 0.881 | 78804 |     65 | 4136353 | 21196 |
| 30 | eng               | English          |            100000 |       0.239 |    0.912 | 0.236 | 91242 | 291069 | 3845349 |  8758 |
| 31 | sqi               | Albanian         |            100000 |       0.987 |    0.747 | 0.846 | 74695 |    995 | 4135423 | 25305 |
| 32 | rus               | Russian          |            100000 |       0.592 |    0.710 | 0.528 | 71033 |  48977 | 4087441 | 28967 |
| 33 | fra               | French           |            100000 |       0.675 |    0.766 | 0.612 | 76607 |  36932 | 4099486 | 23393 |
| 34 | lav               | Latvian          |            100000 |       0.930 |    0.749 | 0.804 | 74883 |   5659 | 4130759 | 25117 |
| 35 | deu               | German           |            100000 |       0.639 |    0.827 | 0.599 | 82719 |  46756 | 4089662 | 17281 |
| 36 | tur               | Turkish          |            100000 |       0.939 |    0.778 | 0.828 | 77837 |   5089 | 4131329 | 22163 |
| 37 | ara               | Arabic           |            100000 |       0.847 |    0.888 | 0.804 | 88771 |  15980 | 4120438 | 11229 |
| 38 | vie               | Vietnamese       |            100000 |       0.962 |    0.899 | 0.912 | 89889 |   3570 | 4132848 | 10111 |
| 39 | nob               | Norwegian Bokmål |            100000 |       0.618 |    0.565 | 0.499 | 56473 |  34838 | 4101580 | 43527 |
| 40 | ben               | Bangla           |            100000 |       1.000 |    0.929 | 0.963 | 92897 |     10 | 4136408 |  7103 |
| 41 | nld               | Dutch            |            100000 |       0.831 |    0.780 | 0.744 | 77955 |  15815 | 4120603 | 22045 |
| 42 | urd               | Urdu             |             46523 |       0.710 |    0.763 | 0.640 | 35497 |  14494 | 4175401 | 11026 |
| 43 | tam               | Tamil            |             40165 |       1.000 |    0.950 | 0.974 | 38148 |      5 | 4196248 |  2017 |
| 44 | tel               | Telugu           |             30416 |       0.999 |    0.945 | 0.971 | 28735 |     23 | 4205979 |  1681 |
| 45 | fil               | Filipino         |             19314 |       0.783 |    0.503 | 0.564 |  9714 |   2695 | 4214409 |  9600 |