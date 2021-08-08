# Classification performance for fasttext-compressed on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 4236418 (100.00%)
- **Aggregated accuracy: 75.21%**

<h2 id="supported-languages">Supported languages (176)</h2>

afr (Afrikaans), als (Tosk Albanian), amh (Amharic), arg (Aragonese), ara (Arabic), arz (Egyptian Arabic), asm (Assamese), ast (Asturian), ava (Avaric), aze (Azerbaijani), azb (South Azerbaijani), bak (Bashkir), bar (Bavarian), bcl (Central Bikol), bel (Belarusian), bul (Bulgarian), bih (Bihari languages), ben (Bangla), bod (Tibetan), bpy (Bishnupriya), bre (Breton), bos (Bosnian), bxr (Russia Buriat), cat (Catalan), cbk (Chavacano), che (Chechen), ceb (Cebuano), ckb (Central Kurdish), cos (Corsican), ces (Czech), chv (Chuvash), cym (Welsh), dan (Danish), deu (German), diq (Dimli (individual language)), dsb (Lower Sorbian), dty (Dotyali), div (Divehi), ell (Greek), eml (Unknown language [eml]), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fra (French), frr (Northern Frisian), fry (Western Frisian), gle (Irish), gla (Scottish Gaelic), glg (Galician), grn (Guarani), gom (Goan Konkani), guj (Gujarati), glv (Manx), heb (Hebrew), hin (Hindi), hif (Fiji Hindi), hrv (Croatian), hsb (Upper Sorbian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ina (Interlingua), ind (Indonesian), ile (Interlingue), ilo (Iloko), ido (Ido), isl (Icelandic), ita (Italian), jpn (Japanese), jbo (Lojban), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), krc (Karachay-Balkar), kur (Kurdish), kom (Komi), cor (Cornish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lez (Lezghian), lim (Limburgish), lmo (Lombard), lao (Lao), lrc (Northern Luri), lit (Lithuanian), lav (Latvian), mai (Maithili), mlg (Malagasy), mhr (Eastern Mari), min (Minangkabau), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), mrj (Western Mari), msa (Malay), mlt (Maltese), mwl (Mirandese), mya (Burmese), myv (Erzya), mzn (Mazanderani), nah (Nahuatl languages), nap (Neapolitan), nds (Low German), nep (Nepali), new (Newari), nld (Dutch), nno (Norwegian Nynorsk), nob (Norwegian Bokmål), oci (Occitan), ori (Odia), oss (Ossetic), pan (Punjabi), pam (Pampanga), pfl (Palatine German), pol (Polish), pms (Piedmontese), pnb (Western Panjabi), pus (Pashto), por (Portuguese), que (Quechua), roh (Romansh), ron (Romanian), rus (Russian), rue (Rusyn), san (Sanskrit), sah (Sakha), srd (Sardinian), scn (Sicilian), sco (Scots), snd (Sindhi), srp (Serbian), sin (Sinhala), slk (Slovak), slv (Slovenian), som (Somali), sqi (Albanian), srp (Serbian), sun (Sundanese), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tgk (Tajik), tha (Thai), tuk (Turkmen), fil (Filipino), tur (Turkish), tat (Tatar), tyv (Tuvinian), uig (Uyghur), ukr (Ukrainian), urd (Urdu), uzb (Uzbek), vec (Venetian), vep (Veps), vie (Vietnamese), vls (West Flemish), vol (Volapük), wln (Walloon), war (Waray), wuu (Wu Chinese), xal (Kalmyk), xmf (Mingrelian), yid (Yiddish), yor (Yoruba), yue (Cantonese), zho (Chinese)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |    tp |     fp |      tn |    fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|------:|-------:|--------:|------:|
|  1 | ell               | Greek            |            100000 |       0.997 |    0.982 | 0.988 | 98172 |    253 | 4136165 |  1828 |
|  2 | swe               | Swedish          |            100000 |       0.831 |    0.793 | 0.749 | 79263 |  16147 | 4120271 | 20737 |
|  3 | mkd               | Macedonian       |            100000 |       0.870 |    0.761 | 0.765 | 76086 |  11387 | 4125031 | 23914 |
|  4 | tha               | Thai             |            100000 |       0.999 |    0.957 | 0.977 | 95713 |    124 | 4136294 |  4287 |
|  5 | cat               | Catalan          |            100000 |       0.918 |    0.508 | 0.635 | 50786 |   4527 | 4131891 | 49214 |
|  6 | bul               | Bulgarian        |            100000 |       0.951 |    0.654 | 0.760 | 65408 |   3357 | 4133061 | 34592 |
|  7 | fin               | Finnish          |            100000 |       0.818 |    0.865 | 0.768 | 86466 |  19296 | 4117122 | 13534 |
|  8 | dan               | Danish           |            100000 |       0.601 |    0.700 | 0.533 | 69996 |  46449 | 4089969 | 30004 |
|  9 | hun               | Hungarian        |            100000 |       0.831 |    0.880 | 0.787 | 88007 |  17864 | 4118554 | 11993 |
| 10 | kor               | Korean           |            100000 |       0.995 |    0.891 | 0.938 | 89072 |    435 | 4135983 | 10928 |
| 11 | spa               | Spanish          |            100000 |       0.625 |    0.908 | 0.606 | 90765 |  54449 | 4081969 |  9235 |
| 12 | zho               | Chinese          |            100000 |       0.934 |    0.757 | 0.812 | 75651 |   5310 | 4131108 | 24349 |
| 13 | slk               | Slovak           |            100000 |       0.902 |    0.400 | 0.538 | 39987 |   4356 | 4132062 | 60013 |
| 14 | ron               | Romanian         |            100000 |       0.971 |    0.631 | 0.756 | 63068 |   1876 | 4134542 | 36932 |
| 15 | ind               | Indonesian       |            100000 |       0.949 |    0.671 | 0.770 | 67114 |   3624 | 4132794 | 32886 |
| 16 | est               | Estonian         |            100000 |       0.952 |    0.551 | 0.686 | 55128 |   2808 | 4133610 | 44872 |
| 17 | por               | Portuguese       |            100000 |       0.790 |    0.810 | 0.722 | 80970 |  21587 | 4114831 | 19030 |
| 18 | hrv               | Croatian         |            100000 |       0.728 |    0.264 | 0.361 | 26401 |   9843 | 4126575 | 73599 |
| 19 | heb               | Hebrew           |            100000 |       1.000 |    0.969 | 0.984 | 96866 |     44 | 4136374 |  3134 |
| 20 | ita               | Italian          |            100000 |       0.514 |    0.890 | 0.498 | 88985 |  84250 | 4052168 | 11015 |
| 21 | slv               | Slovenian        |            100000 |       0.749 |    0.334 | 0.429 | 33416 |  11213 | 4125205 | 66584 |
| 22 | ces               | Czech            |            100000 |       0.713 |    0.737 | 0.632 | 73683 |  29706 | 4106712 | 26317 |
| 23 | mal               | Malayalam        |            100000 |       0.999 |    0.964 | 0.980 | 96373 |    125 | 4136293 |  3627 |
| 24 | lit               | Lithuanian       |            100000 |       0.899 |    0.686 | 0.746 | 68646 |   7737 | 4128681 | 31354 |
| 25 | ukr               | Ukrainian        |            100000 |       0.899 |    0.591 | 0.686 | 59075 |   6613 | 4129805 | 40925 |
| 26 | pol               | Polish           |            100000 |       0.826 |    0.848 | 0.769 | 84830 |  17928 | 4118490 | 15170 |
| 27 | fas               | Persian          |            100000 |       0.881 |    0.442 | 0.566 | 44234 |   5991 | 4130427 | 55766 |
| 28 | jpn               | Japanese         |            100000 |       0.926 |    0.911 | 0.886 | 91080 |   7300 | 4129118 |  8920 |
| 29 | hin               | Hindi            |            100000 |       0.998 |    0.797 | 0.886 | 79742 |    176 | 4136242 | 20258 |
| 30 | eng               | English          |            100000 |       0.272 |    0.931 | 0.269 | 93052 | 249357 | 3887061 |  6948 |
| 31 | sqi               | Albanian         |            100000 |       0.994 |    0.679 | 0.805 | 67935 |    395 | 4136023 | 32065 |
| 32 | rus               | Russian          |            100000 |       0.563 |    0.956 | 0.556 | 95628 |  74265 | 4062153 |  4372 |
| 33 | fra               | French           |            100000 |       0.727 |    0.864 | 0.688 | 86424 |  32405 | 4104013 | 13576 |
| 34 | lav               | Latvian          |            100000 |       0.985 |    0.621 | 0.758 | 62101 |    931 | 4135487 | 37899 |
| 35 | deu               | German           |            100000 |       0.745 |    0.849 | 0.699 | 84936 |  29124 | 4107294 | 15064 |
| 36 | tur               | Turkish          |            100000 |       0.863 |    0.896 | 0.822 | 89562 |  14158 | 4122260 | 10438 |
| 37 | ara               | Arabic           |            100000 |       0.661 |    0.916 | 0.642 | 91590 |  46947 | 4089471 |  8410 |
| 38 | vie               | Vietnamese       |            100000 |       0.986 |    0.842 | 0.903 | 84224 |   1188 | 4135230 | 15776 |
| 39 | nob               | Norwegian Bokmål |            100000 |       0.755 |    0.303 | 0.404 | 30259 |   9843 | 4126575 | 69741 |
| 40 | ben               | Bangla           |            100000 |       0.999 |    0.938 | 0.967 | 93803 |     93 | 4136325 |  6197 |
| 41 | nld               | Dutch            |            100000 |       0.897 |    0.798 | 0.806 | 79835 |   9125 | 4127293 | 20165 |
| 42 | urd               | Urdu             |             46523 |       0.984 |    0.751 | 0.846 | 34930 |    564 | 4189331 | 11593 |
| 43 | tam               | Tamil            |             40165 |       0.998 |    0.943 | 0.968 | 37857 |     84 | 4196169 |  2308 |
| 44 | tel               | Telugu           |             30416 |       0.998 |    0.927 | 0.961 | 28199 |     51 | 4205951 |  2217 |
| 45 | fil               | Filipino         |             19314 |       0.836 |    0.566 | 0.633 | 10925 |   2136 | 4214968 |  8389 |