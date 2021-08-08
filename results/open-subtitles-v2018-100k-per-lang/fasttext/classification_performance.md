# Classification performance for fasttext on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 4236418 (100.00%)
- **Aggregated accuracy: 0.8015608941327319**

<h2 id="supported-languages">Supported languages (176)</h2>

afr (Afrikaans), als (Tosk Albanian), amh (Amharic), arg (Aragonese), ara (Arabic), arz (Egyptian Arabic), asm (Assamese), ast (Asturian), ava (Avaric), aze (Azerbaijani), azb (South Azerbaijani), bak (Bashkir), bar (Bavarian), bcl (Central Bikol), bel (Belarusian), bul (Bulgarian), bih (Bihari languages), ben (Bangla), bod (Tibetan), bpy (Bishnupriya), bre (Breton), bos (Bosnian), bxr (Russia Buriat), cat (Catalan), cbk (Chavacano), che (Chechen), ceb (Cebuano), ckb (Central Kurdish), cos (Corsican), ces (Czech), chv (Chuvash), cym (Welsh), dan (Danish), deu (German), diq (Dimli (individual language)), dsb (Lower Sorbian), dty (Dotyali), div (Divehi), ell (Greek), eml (Unknown language [eml]), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fra (French), frr (Northern Frisian), fry (Western Frisian), gle (Irish), gla (Scottish Gaelic), glg (Galician), grn (Guarani), gom (Goan Konkani), guj (Gujarati), glv (Manx), heb (Hebrew), hin (Hindi), hif (Fiji Hindi), hrv (Croatian), hsb (Upper Sorbian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ina (Interlingua), ind (Indonesian), ile (Interlingue), ilo (Iloko), ido (Ido), isl (Icelandic), ita (Italian), jpn (Japanese), jbo (Lojban), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), krc (Karachay-Balkar), kur (Kurdish), kom (Komi), cor (Cornish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lez (Lezghian), lim (Limburgish), lmo (Lombard), lao (Lao), lrc (Northern Luri), lit (Lithuanian), lav (Latvian), mai (Maithili), mlg (Malagasy), mhr (Eastern Mari), min (Minangkabau), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), mrj (Western Mari), msa (Malay), mlt (Maltese), mwl (Mirandese), mya (Burmese), myv (Erzya), mzn (Mazanderani), nah (Nahuatl languages), nap (Neapolitan), nds (Low German), nep (Nepali), new (Newari), nld (Dutch), nno (Norwegian Nynorsk), nob (Norwegian Bokmål), oci (Occitan), ori (Odia), oss (Ossetic), pan (Punjabi), pam (Pampanga), pfl (Palatine German), pol (Polish), pms (Piedmontese), pnb (Western Panjabi), pus (Pashto), por (Portuguese), que (Quechua), roh (Romansh), ron (Romanian), rus (Russian), rue (Rusyn), san (Sanskrit), sah (Sakha), srd (Sardinian), scn (Sicilian), sco (Scots), snd (Sindhi), srp (Serbian), sin (Sinhala), slk (Slovak), slv (Slovenian), som (Somali), sqi (Albanian), srp (Serbian), sun (Sundanese), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tgk (Tajik), tha (Thai), tuk (Turkmen), fil (Filipino), tur (Turkish), tat (Tatar), tyv (Tuvinian), uig (Uyghur), ukr (Ukrainian), urd (Urdu), uzb (Uzbek), vec (Venetian), vep (Veps), vie (Vietnamese), vls (West Flemish), vol (Volapük), wln (Walloon), war (Waray), wuu (Wu Chinese), xal (Kalmyk), xmf (Mingrelian), yid (Yiddish), yor (Yoruba), yue (Cantonese), zho (Chinese)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |    tp |     fp |      tn |    fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|------:|-------:|--------:|------:|
|  1 | ell               | Greek            |            100000 |       0.993 |    0.993 | 0.990 | 99294 |    693 | 4135725 |   706 |
|  2 | swe               | Swedish          |            100000 |       0.861 |    0.820 | 0.787 | 81969 |  13210 | 4123208 | 18031 |
|  3 | mkd               | Macedonian       |            100000 |       0.910 |    0.848 | 0.841 | 84828 |   8412 | 4128006 | 15172 |
|  4 | tha               | Thai             |            100000 |       0.998 |    0.958 | 0.977 | 95843 |    150 | 4136268 |  4157 |
|  5 | cat               | Catalan          |            100000 |       0.950 |    0.598 | 0.720 | 59808 |   3148 | 4133270 | 40192 |
|  6 | bul               | Bulgarian        |            100000 |       0.947 |    0.787 | 0.839 | 78701 |   4413 | 4132005 | 21299 |
|  7 | fin               | Finnish          |            100000 |       0.865 |    0.895 | 0.824 | 89517 |  13918 | 4122500 | 10483 |
|  8 | dan               | Danish           |            100000 |       0.619 |    0.747 | 0.560 | 74699 |  45945 | 4090473 | 25301 |
|  9 | hun               | Hungarian        |            100000 |       0.844 |    0.932 | 0.818 | 93172 |  17283 | 4119135 |  6828 |
| 10 | kor               | Korean           |            100000 |       0.987 |    0.930 | 0.952 | 92967 |   1182 | 4135236 |  7033 |
| 11 | spa               | Spanish          |            100000 |       0.706 |    0.936 | 0.689 | 93648 |  39086 | 4097332 |  6352 |
| 12 | zho               | Chinese          |            100000 |       0.928 |    0.850 | 0.858 | 85002 |   6573 | 4129845 | 14998 |
| 13 | slk               | Slovak           |            100000 |       0.918 |    0.512 | 0.639 | 51250 |   4573 | 4131845 | 48750 |
| 14 | ron               | Romanian         |            100000 |       0.961 |    0.723 | 0.812 | 72276 |   2908 | 4133510 | 27724 |
| 15 | ind               | Indonesian       |            100000 |       0.920 |    0.725 | 0.783 | 72503 |   6296 | 4130122 | 27497 |
| 16 | est               | Estonian         |            100000 |       0.941 |    0.678 | 0.769 | 67801 |   4256 | 4132162 | 32199 |
| 17 | por               | Portuguese       |            100000 |       0.735 |    0.883 | 0.701 | 88308 |  31776 | 4104642 | 11692 |
| 18 | hrv               | Croatian         |            100000 |       0.732 |    0.305 | 0.399 | 30462 |  11167 | 4125251 | 69538 |
| 19 | heb               | Hebrew           |            100000 |       1.000 |    0.980 | 0.990 | 98046 |     41 | 4136377 |  1954 |
| 20 | ita               | Italian          |            100000 |       0.639 |    0.925 | 0.622 | 92461 |  52332 | 4084086 |  7539 |
| 21 | slv               | Slovenian        |            100000 |       0.858 |    0.386 | 0.510 | 38621 |   6372 | 4130046 | 61379 |
| 22 | ces               | Czech            |            100000 |       0.781 |    0.793 | 0.709 | 79295 |  22186 | 4114232 | 20705 |
| 23 | mal               | Malayalam        |            100000 |       0.999 |    0.967 | 0.982 | 96741 |     99 | 4136319 |  3259 |
| 24 | lit               | Lithuanian       |            100000 |       0.909 |    0.765 | 0.797 | 76457 |   7678 | 4128740 | 23543 |
| 25 | ukr               | Ukrainian        |            100000 |       0.932 |    0.676 | 0.762 | 67632 |   4955 | 4131463 | 32368 |
| 26 | pol               | Polish           |            100000 |       0.837 |    0.894 | 0.798 | 89392 |  17360 | 4119058 | 10608 |
| 27 | fas               | Persian          |            100000 |       0.948 |    0.577 | 0.703 | 57657 |   3136 | 4133282 | 42343 |
| 28 | jpn               | Japanese         |            100000 |       0.942 |    0.934 | 0.912 | 93404 |   5734 | 4130684 |  6596 |
| 29 | hin               | Hindi            |            100000 |       0.998 |    0.850 | 0.917 | 84951 |    138 | 4136280 | 15049 |
| 30 | eng               | English          |            100000 |       0.433 |    0.939 | 0.427 | 93908 | 123135 | 4013283 |  6092 |
| 31 | sqi               | Albanian         |            100000 |       0.987 |    0.700 | 0.814 | 69957 |    933 | 4135485 | 30043 |
| 32 | rus               | Russian          |            100000 |       0.679 |    0.962 | 0.670 | 96174 |  45549 | 4090869 |  3826 |
| 33 | fra               | French           |            100000 |       0.709 |    0.919 | 0.687 | 91892 |  37802 | 4098616 |  8108 |
| 34 | lav               | Latvian          |            100000 |       0.989 |    0.668 | 0.794 | 66756 |    724 | 4135694 | 33244 |
| 35 | deu               | German           |            100000 |       0.813 |    0.891 | 0.775 | 89068 |  20443 | 4115975 | 10932 |
| 36 | tur               | Turkish          |            100000 |       0.881 |    0.933 | 0.854 | 93281 |  12574 | 4123844 |  6719 |
| 37 | ara               | Arabic           |            100000 |       0.783 |    0.924 | 0.759 | 92437 |  25579 | 4110839 |  7563 |
| 38 | vie               | Vietnamese       |            100000 |       0.991 |    0.870 | 0.922 | 86978 |    798 | 4135620 | 13022 |
| 39 | nob               | Norwegian Bokmål |            100000 |       0.770 |    0.342 | 0.443 | 34206 |  10192 | 4126226 | 65794 |
| 40 | ben               | Bangla           |            100000 |       0.999 |    0.947 | 0.971 | 94676 |    141 | 4136277 |  5324 |
| 41 | nld               | Dutch            |            100000 |       0.877 |    0.855 | 0.816 | 85450 |  12031 | 4124387 | 14550 |
| 42 | urd               | Urdu             |             46523 |       0.970 |    0.761 | 0.842 | 35426 |   1100 | 4188795 | 11097 |
| 43 | tam               | Tamil            |             40165 |       0.995 |    0.944 | 0.967 | 37924 |    177 | 4196076 |  2241 |
| 44 | tel               | Telugu           |             30416 |       0.994 |    0.931 | 0.959 | 28330 |    167 | 4205835 |  2086 |
| 45 | fil               | Filipino         |             19314 |       0.838 |    0.651 | 0.684 | 12579 |   2435 | 4214669 |  6735 |