# Classification performance for fasttext on tatoeba-sentences-2021-06-05-common-48

- Dataset coverage (sentences in supported languages): 7461627 (100.00%)
- **Aggregated accuracy: 98.94%**

<h2 id="supported-languages">Supported languages (176)</h2>

afr (Afrikaans), als (Tosk Albanian), amh (Amharic), arg (Aragonese), ara (Arabic), arz (Egyptian Arabic), asm (Assamese), ast (Asturian), ava (Avaric), aze (Azerbaijani), azb (South Azerbaijani), bak (Bashkir), bar (Bavarian), bcl (Central Bikol), bel (Belarusian), bul (Bulgarian), bih (Bihari languages), ben (Bangla), bod (Tibetan), bpy (Bishnupriya), bre (Breton), bos (Bosnian), bxr (Russia Buriat), cat (Catalan), cbk (Chavacano), che (Chechen), ceb (Cebuano), ckb (Central Kurdish), cos (Corsican), ces (Czech), chv (Chuvash), cym (Welsh), dan (Danish), deu (German), diq (Dimli (individual language)), dsb (Lower Sorbian), dty (Dotyali), div (Divehi), ell (Greek), eml (Unknown language [eml]), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fra (French), frr (Northern Frisian), fry (Western Frisian), gle (Irish), gla (Scottish Gaelic), glg (Galician), grn (Guarani), gom (Goan Konkani), guj (Gujarati), glv (Manx), heb (Hebrew), hin (Hindi), hif (Fiji Hindi), hrv (Croatian), hsb (Upper Sorbian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ina (Interlingua), ind (Indonesian), ile (Interlingue), ilo (Iloko), ido (Ido), isl (Icelandic), ita (Italian), jpn (Japanese), jbo (Lojban), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), krc (Karachay-Balkar), kur (Kurdish), kom (Komi), cor (Cornish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lez (Lezghian), lim (Limburgish), lmo (Lombard), lao (Lao), lrc (Northern Luri), lit (Lithuanian), lav (Latvian), mai (Maithili), mlg (Malagasy), mhr (Eastern Mari), min (Minangkabau), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), mrj (Western Mari), msa (Malay), mlt (Maltese), mwl (Mirandese), mya (Burmese), myv (Erzya), mzn (Mazanderani), nah (Nahuatl languages), nap (Neapolitan), nds (Low German), nep (Nepali), new (Newari), nld (Dutch), nno (Norwegian Nynorsk), nob (Norwegian Bokmål), oci (Occitan), ori (Odia), oss (Ossetic), pan (Punjabi), pam (Pampanga), pfl (Palatine German), pol (Polish), pms (Piedmontese), pnb (Western Panjabi), pus (Pashto), por (Portuguese), que (Quechua), roh (Romansh), ron (Romanian), rus (Russian), rue (Rusyn), san (Sanskrit), sah (Sakha), srd (Sardinian), scn (Sicilian), sco (Scots), snd (Sindhi), srp (Serbian), sin (Sinhala), slk (Slovak), slv (Slovenian), som (Somali), sqi (Albanian), srp (Serbian), sun (Sundanese), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tgk (Tajik), tha (Thai), tuk (Turkmen), fil (Filipino), tur (Turkish), tat (Tatar), tyv (Tuvinian), uig (Uyghur), ukr (Ukrainian), urd (Urdu), uzb (Uzbek), vec (Venetian), vep (Veps), vie (Vietnamese), vls (West Flemish), vol (Volapük), wln (Walloon), war (Waray), wuu (Wu Chinese), xal (Kalmyk), xmf (Mingrelian), yid (Yiddish), yor (Yoruba), yue (Cantonese), zho (Chinese)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |      tp |   fp |      tn |   fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|--------:|-----:|--------:|-----:|
|  1 | eng               | English          |           1479733 |       0.994 |    0.999 | 0.993 | 1478395 | 9216 | 5972678 | 1338 |
|  2 | rus               | Russian          |            849653 |       0.995 |    0.998 | 0.994 |  848237 | 4129 | 6607845 | 1416 |
|  3 | ita               | Italian          |            787053 |       0.994 |    0.996 | 0.992 |  783712 | 4984 | 6669590 | 3341 |
|  4 | tur               | Turkish          |            709573 |       0.999 |    0.998 | 0.998 |  707878 |  812 | 6751242 | 1695 |
|  5 | deu               | German           |            553727 |       0.996 |    0.997 | 0.994 |  552153 | 2391 | 6905509 | 1574 |
|  6 | fra               | French           |            466192 |       0.994 |    0.994 | 0.991 |  463322 | 2814 | 6992621 | 2870 |
|  7 | por               | Portuguese       |            385737 |       0.991 |    0.983 | 0.982 |  379214 | 3624 | 7072266 | 6523 |
|  8 | spa               | Spanish          |            338781 |       0.979 |    0.987 | 0.972 |  334473 | 7311 | 7115535 | 4308 |
|  9 | hun               | Hungarian        |            323048 |       0.996 |    0.993 | 0.993 |  320862 | 1315 | 7137264 | 2186 |
| 10 | jpn               | Japanese         |            208761 |       1.000 |    1.000 | 1.000 |  208682 |   28 | 7252838 |   79 |
| 11 | heb               | Hebrew           |            197226 |       1.000 |    1.000 | 1.000 |  197205 |    0 | 7264401 |   21 |
| 12 | ukr               | Ukrainian        |            171674 |       0.996 |    0.978 | 0.985 |  167950 |  738 | 7289215 | 3724 |
| 13 | nld               | Dutch            |            144340 |       0.988 |    0.955 | 0.966 |  137902 | 1685 | 7315602 | 6438 |
| 14 | fin               | Finnish          |            128011 |       0.994 |    0.981 | 0.984 |  125521 |  797 | 7332819 | 2490 |
| 15 | pol               | Polish           |            109662 |       0.988 |    0.992 | 0.984 |  108795 | 1366 | 7350599 |  867 |
| 16 | mkd               | Macedonian       |             77938 |       0.982 |    0.986 | 0.976 |   76873 | 1395 | 7382294 | 1065 |
| 17 | mar               | Marathi          |             64126 |       0.999 |    0.998 | 0.998 |   64016 |   96 | 7397405 |  110 |
| 18 | lit               | Lithuanian       |             59659 |       0.996 |    0.960 | 0.976 |   57282 |  212 | 7401756 | 2377 |
| 19 | ces               | Czech            |             57030 |       0.945 |    0.951 | 0.923 |   54248 | 3141 | 7401456 | 2782 |
| 20 | dan               | Danish           |             49399 |       0.856 |    0.907 | 0.820 |   44828 | 7523 | 7404705 | 4571 |
| 21 | swe               | Swedish          |             41677 |       0.953 |    0.948 | 0.929 |   39504 | 1944 | 7418006 | 2173 |
| 22 | ara               | Arabic           |             35991 |       1.000 |    0.993 | 0.997 |   35750 |    5 | 7425631 |  241 |
| 23 | ell               | Greek            |             34071 |       1.000 |    1.000 | 1.000 |   34069 |   10 | 7427546 |    2 |
| 24 | ron               | Romanian         |             24943 |       0.983 |    0.937 | 0.951 |   23375 |  416 | 7436268 | 1568 |
| 25 | bul               | Bulgarian        |             24503 |       0.966 |    0.944 | 0.939 |   23127 |  802 | 7436322 | 1376 |
| 26 | vie               | Vietnamese       |             19234 |       0.993 |    0.997 | 0.992 |   19178 |  132 | 7442261 |   56 |
| 27 | fil               | Filipino         |             16649 |       0.992 |    0.938 | 0.961 |   15621 |  122 | 7444856 | 1028 |
| 28 | slk               | Slovak           |             14660 |       0.934 |    0.627 | 0.731 |    9190 |  651 | 7446316 | 5470 |
| 29 | ind               | Indonesian       |             14542 |       0.963 |    0.921 | 0.925 |   13398 |  510 | 7446575 | 1144 |
| 30 | hin               | Hindi            |             14230 |       0.994 |    0.989 | 0.989 |   14076 |   82 | 7447315 |  154 |
| 31 | nob               | Norwegian Bokmål |             14223 |       0.676 |    0.422 | 0.462 |    5997 | 2872 | 7444532 | 8226 |
| 32 | cat               | Catalan          |              7971 |       0.914 |    0.800 | 0.820 |    6377 |  601 | 7453055 | 1594 |
| 33 | kor               | Korean           |              7570 |       0.997 |    0.994 | 0.994 |    7525 |   20 | 7454037 |   45 |
| 34 | hrv               | Croatian         |              5204 |       0.786 |    0.451 | 0.532 |    2349 |  638 | 7455785 | 2855 |
| 35 | ben               | Bangla           |              4714 |       0.998 |    0.999 | 0.998 |    4709 |    8 | 7456905 |    5 |
| 36 | afr               | Afrikaans        |              4031 |       0.859 |    0.700 | 0.725 |    2823 |  465 | 7457131 | 1208 |
| 37 | est               | Estonian         |              3637 |       0.842 |    0.818 | 0.770 |    2975 |  559 | 7457431 |  662 |
| 38 | tha               | Thai             |              3528 |       0.999 |    1.000 | 0.999 |    3527 |    2 | 7458097 |    1 |
| 39 | sqi               | Albanian         |              2526 |       0.967 |    0.865 | 0.899 |    2184 |   75 | 7459026 |  342 |
| 40 | urd               | Urdu             |              2008 |       0.974 |    0.982 | 0.965 |    1972 |   53 | 7459566 |   36 |
| 41 | cym               | Welsh            |              1344 |       0.965 |    0.721 | 0.813 |     969 |   35 | 7460248 |  375 |
| 42 | slv               | Slovenian        |              1093 |       0.436 |    0.510 | 0.360 |     557 |  721 | 7459813 |  536 |
| 43 | mal               | Malayalam        |               827 |       0.992 |    1.000 | 0.992 |     827 |    7 | 7460793 |    0 |
| 44 | tam               | Tamil            |               334 |       0.991 |    1.000 | 0.991 |     334 |    3 | 7461290 |    0 |
| 45 | tel               | Telugu           |               254 |       0.981 |    1.000 | 0.981 |     254 |    5 | 7461368 |    0 |
| 46 | pan               | Punjabi          |               196 |       1.000 |    1.000 | 1.000 |     196 |    0 | 7461431 |    0 |
| 47 | kan               | Kannada          |               176 |       0.926 |    1.000 | 0.926 |     176 |   14 | 7461437 |    0 |
| 48 | guj               | Gujarati         |               168 |       0.988 |    1.000 | 0.988 |     168 |    2 | 7461457 |    0 |