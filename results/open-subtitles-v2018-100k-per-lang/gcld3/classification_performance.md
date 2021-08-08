# Classification performance for gcld3 on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 4236418 (100.00%)
- **Aggregated accuracy: 73.08%**

<h2 id="supported-languages">Supported languages (107)</h2>

afr (Afrikaans), amh (Amharic), ara (Arabic), bul (Bulgarian), bul (Bulgarian), ben (Bangla), bos (Bosnian), cat (Catalan), ceb (Cebuano), cos (Corsican), ces (Czech), cym (Welsh), dan (Danish), deu (German), ell (Greek), ell (Greek), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fil (Filipino), fra (French), fry (Western Frisian), gle (Irish), gla (Scottish Gaelic), glg (Galician), guj (Gujarati), hau (Hausa), haw (Hawaiian), hin (Hindi), hin (Hindi), hmn (Hmong), hrv (Croatian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ind (Indonesian), ibo (Igbo), isl (Icelandic), ita (Italian), heb (Hebrew), jpn (Japanese), jpn (Japanese), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), kur (Kurdish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lao (Lao), lit (Lithuanian), lav (Latvian), mlg (Malagasy), mri (Maori), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), msa (Malay), mlt (Maltese), mya (Burmese), nep (Nepali), nld (Dutch), nob (Norwegian Bokmål), nya (Nyanja), pan (Punjabi), pol (Polish), pus (Pashto), por (Portuguese), ron (Romanian), rus (Russian), rus (Russian), snd (Sindhi), sin (Sinhala), slk (Slovak), slv (Slovenian), smo (Samoan), sna (Shona), som (Somali), sqi (Albanian), srp (Serbian), sot (Southern Sotho), sun (Sundanese), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tgk (Tajik), tha (Thai), tur (Turkish), ukr (Ukrainian), urd (Urdu), uzb (Uzbek), vie (Vietnamese), xho (Xhosa), yid (Yiddish), yor (Yoruba), zho (Chinese), zho (Chinese), zul (Zulu)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |    tp |    fp |      tn |    fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|------:|------:|--------:|------:|
|  1 | ell               | Greek            |            100000 |       0.930 |    0.991 | 0.927 | 99142 |  7411 | 4129007 |   858 |
|  2 | swe               | Swedish          |            100000 |       0.835 |    0.742 | 0.729 | 74175 | 14708 | 4121710 | 25825 |
|  3 | mkd               | Macedonian       |            100000 |       0.891 |    0.647 | 0.717 | 64667 |  7898 | 4128520 | 35333 |
|  4 | tha               | Thai             |            100000 |       0.997 |    0.942 | 0.968 | 94203 |   263 | 4136155 |  5797 |
|  5 | cat               | Catalan          |            100000 |       0.819 |    0.644 | 0.668 | 64430 | 14233 | 4122185 | 35570 |
|  6 | bul               | Bulgarian        |            100000 |       0.707 |    0.707 | 0.617 | 70659 | 29255 | 4107163 | 29341 |
|  7 | fin               | Finnish          |            100000 |       0.807 |    0.784 | 0.726 | 78440 | 18791 | 4117627 | 21560 |
|  8 | dan               | Danish           |            100000 |       0.761 |    0.614 | 0.614 | 61404 | 19263 | 4117155 | 38596 |
|  9 | hun               | Hungarian        |            100000 |       0.864 |    0.757 | 0.759 | 75722 | 11924 | 4124494 | 24278 |
| 10 | kor               | Korean           |            100000 |       0.969 |    0.955 | 0.947 | 95514 |  3081 | 4133337 |  4486 |
| 11 | spa               | Spanish          |            100000 |       0.795 |    0.666 | 0.663 | 66646 | 17195 | 4119223 | 33354 |
| 12 | zho               | Chinese          |            100000 |       0.919 |    0.858 | 0.854 | 85780 |  7585 | 4128833 | 14220 |
| 13 | slk               | Slovak           |            100000 |       0.789 |    0.608 | 0.629 | 60799 | 16304 | 4120114 | 39201 |
| 14 | ron               | Romanian         |            100000 |       0.898 |    0.611 | 0.698 | 61108 |  6976 | 4129442 | 38892 |
| 15 | ind               | Indonesian       |            100000 |       0.858 |    0.470 | 0.578 | 47018 |  7801 | 4128617 | 52982 |
| 16 | est               | Estonian         |            100000 |       0.819 |    0.710 | 0.702 | 71021 | 15723 | 4120695 | 28979 |
| 17 | por               | Portuguese       |            100000 |       0.814 |    0.677 | 0.681 | 67704 | 15509 | 4120909 | 32296 |
| 18 | hrv               | Croatian         |            100000 |       0.743 |    0.357 | 0.445 | 35706 | 12370 | 4124048 | 64294 |
| 19 | heb               | Hebrew           |            100000 |       0.999 |    0.929 | 0.962 | 92883 |    66 | 4136352 |  7117 |
| 20 | ita               | Italian          |            100000 |       0.815 |    0.695 | 0.691 | 69451 | 15732 | 4120686 | 30549 |
| 21 | slv               | Slovenian        |            100000 |       0.778 |    0.627 | 0.632 | 62668 | 17892 | 4118526 | 37332 |
| 22 | ces               | Czech            |            100000 |       0.828 |    0.659 | 0.682 | 65903 | 13732 | 4122686 | 34097 |
| 23 | mal               | Malayalam        |            100000 |       1.000 |    0.958 | 0.979 | 95809 |     0 | 4136418 |  4191 |
| 24 | lit               | Lithuanian       |            100000 |       0.839 |    0.679 | 0.700 | 67868 | 13048 | 4123370 | 32132 |
| 25 | ukr               | Ukrainian        |            100000 |       0.756 |    0.576 | 0.592 | 57647 | 18557 | 4117861 | 42353 |
| 26 | pol               | Polish           |            100000 |       0.883 |    0.774 | 0.782 | 77363 | 10245 | 4126173 | 22637 |
| 27 | fas               | Persian          |            100000 |       0.869 |    0.552 | 0.643 | 55250 |  8360 | 4128058 | 44750 |
| 28 | jpn               | Japanese         |            100000 |       0.703 |    0.967 | 0.695 | 96684 | 40843 | 4095575 |  3316 |
| 29 | hin               | Hindi            |            100000 |       0.816 |    0.735 | 0.711 | 73451 | 16519 | 4119899 | 26549 |
| 30 | eng               | English          |            100000 |       0.691 |    0.689 | 0.597 | 68859 | 30848 | 4105570 | 31141 |
| 31 | sqi               | Albanian         |            100000 |       0.945 |    0.692 | 0.781 | 69231 |  3995 | 4132423 | 30769 |
| 32 | rus               | Russian          |            100000 |       0.637 |    0.696 | 0.560 | 69635 | 39608 | 4096810 | 30365 |
| 33 | fra               | French           |            100000 |       0.863 |    0.681 | 0.718 | 68140 | 10854 | 4125564 | 31860 |
| 34 | lav               | Latvian          |            100000 |       0.830 |    0.690 | 0.699 | 68956 | 14159 | 4122259 | 31044 |
| 35 | deu               | German           |            100000 |       0.838 |    0.760 | 0.740 | 75994 | 14742 | 4121676 | 24006 |
| 36 | tur               | Turkish          |            100000 |       0.883 |    0.743 | 0.766 | 74271 |  9841 | 4126577 | 25729 |
| 37 | ara               | Arabic           |            100000 |       0.856 |    0.840 | 0.792 | 83981 | 14088 | 4122330 | 16019 |
| 38 | vie               | Vietnamese       |            100000 |       0.906 |    0.803 | 0.815 | 80261 |  8292 | 4128126 | 19739 |
| 39 | nob               | Norwegian Bokmål |            100000 |       0.683 |    0.676 | 0.587 | 67633 | 31322 | 4105096 | 32367 |
| 40 | ben               | Bangla           |            100000 |       1.000 |    0.955 | 0.977 | 95545 |     0 | 4136418 |  4455 |
| 41 | nld               | Dutch            |            100000 |       0.841 |    0.731 | 0.728 | 73077 | 13823 | 4122595 | 26923 |
| 42 | urd               | Urdu             |             46523 |       0.923 |    0.766 | 0.809 | 35638 |  2984 | 4186911 | 10885 |
| 43 | tam               | Tamil            |             40165 |       0.994 |    0.929 | 0.958 | 37303 |   210 | 4196043 |  2862 |
| 44 | tel               | Telugu           |             30416 |       0.993 |    0.898 | 0.940 | 27303 |   195 | 4205807 |  3113 |
| 45 | fil               | Filipino         |             19314 |       0.681 |    0.561 | 0.538 | 10843 |  5069 | 4212035 |  8471 |