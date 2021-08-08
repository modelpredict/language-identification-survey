# Classification performance for fasttext-compressed on tatoeba-sentences-2021-06-05-common-48

- Dataset coverage (sentences in supported languages): 7461627 (100.00%)
- **Aggregated accuracy: 0.978965445471879**

<h2 id="supported-languages">Supported languages (176)</h2>

afr (Afrikaans), als (Tosk Albanian), amh (Amharic), arg (Aragonese), ara (Arabic), arz (Egyptian Arabic), asm (Assamese), ast (Asturian), ava (Avaric), aze (Azerbaijani), azb (South Azerbaijani), bak (Bashkir), bar (Bavarian), bcl (Central Bikol), bel (Belarusian), bul (Bulgarian), bih (Bihari languages), ben (Bangla), bod (Tibetan), bpy (Bishnupriya), bre (Breton), bos (Bosnian), bxr (Russia Buriat), cat (Catalan), cbk (Chavacano), che (Chechen), ceb (Cebuano), ckb (Central Kurdish), cos (Corsican), ces (Czech), chv (Chuvash), cym (Welsh), dan (Danish), deu (German), diq (Dimli (individual language)), dsb (Lower Sorbian), dty (Dotyali), div (Divehi), ell (Greek), eml (Unknown language [eml]), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fra (French), frr (Northern Frisian), fry (Western Frisian), gle (Irish), gla (Scottish Gaelic), glg (Galician), grn (Guarani), gom (Goan Konkani), guj (Gujarati), glv (Manx), heb (Hebrew), hin (Hindi), hif (Fiji Hindi), hrv (Croatian), hsb (Upper Sorbian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ina (Interlingua), ind (Indonesian), ile (Interlingue), ilo (Iloko), ido (Ido), isl (Icelandic), ita (Italian), jpn (Japanese), jbo (Lojban), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), krc (Karachay-Balkar), kur (Kurdish), kom (Komi), cor (Cornish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lez (Lezghian), lim (Limburgish), lmo (Lombard), lao (Lao), lrc (Northern Luri), lit (Lithuanian), lav (Latvian), mai (Maithili), mlg (Malagasy), mhr (Eastern Mari), min (Minangkabau), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), mrj (Western Mari), msa (Malay), mlt (Maltese), mwl (Mirandese), mya (Burmese), myv (Erzya), mzn (Mazanderani), nah (Nahuatl languages), nap (Neapolitan), nds (Low German), nep (Nepali), new (Newari), nld (Dutch), nno (Norwegian Nynorsk), nob (Norwegian Bokmål), oci (Occitan), ori (Odia), oss (Ossetic), pan (Punjabi), pam (Pampanga), pfl (Palatine German), pol (Polish), pms (Piedmontese), pnb (Western Panjabi), pus (Pashto), por (Portuguese), que (Quechua), roh (Romansh), ron (Romanian), rus (Russian), rue (Rusyn), san (Sanskrit), sah (Sakha), srd (Sardinian), scn (Sicilian), sco (Scots), snd (Sindhi), srp (Serbian), sin (Sinhala), slk (Slovak), slv (Slovenian), som (Somali), sqi (Albanian), srp (Serbian), sun (Sundanese), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tgk (Tajik), tha (Thai), tuk (Turkmen), fil (Filipino), tur (Turkish), tat (Tatar), tyv (Tuvinian), uig (Uyghur), ukr (Ukrainian), urd (Urdu), uzb (Uzbek), vec (Venetian), vep (Veps), vie (Vietnamese), vls (West Flemish), vol (Volapük), wln (Walloon), war (Waray), wuu (Wu Chinese), xal (Kalmyk), xmf (Mingrelian), yid (Yiddish), yor (Yoruba), yue (Cantonese), zho (Chinese)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |    fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|------:|
|  1 | eng               | English          |           1479733 |       0.985 |    0.997 | 0.984 | 1475222 | 22413 | 5959481 |  4511 |
|  2 | rus               | Russian          |            849653 |       0.979 |    0.996 | 0.977 |  846620 | 18559 | 6593415 |  3033 |
|  3 | ita               | Italian          |            787053 |       0.984 |    0.987 | 0.978 |  776749 | 12310 | 6662264 | 10304 |
|  4 | tur               | Turkish          |            709573 |       0.998 |    0.994 | 0.995 |  705300 |  1312 | 6750742 |  4273 |
|  5 | deu               | German           |            553727 |       0.990 |    0.993 | 0.987 |  549727 |  5449 | 6902451 |  4000 |
|  6 | fra               | French           |            466192 |       0.984 |    0.988 | 0.978 |  460626 |  7670 | 6987765 |  5566 |
|  7 | por               | Portuguese       |            385737 |       0.986 |    0.965 | 0.968 |  372107 |  5326 | 7070564 | 13630 |
|  8 | spa               | Spanish          |            338781 |       0.952 |    0.977 | 0.942 |  331141 | 16754 | 7106092 |  7640 |
|  9 | hun               | Hungarian        |            323048 |       0.992 |    0.981 | 0.982 |  316851 |  2660 | 7135919 |  6197 |
| 10 | jpn               | Japanese         |            208761 |       0.999 |    0.997 | 0.998 |  208113 |   109 | 7252757 |   648 |
| 11 | heb               | Hebrew           |            197226 |       1.000 |    0.999 | 0.999 |  197021 |     1 | 7264400 |   205 |
| 12 | ukr               | Ukrainian        |            171674 |       0.991 |    0.916 | 0.948 |  157290 |  1385 | 7288568 | 14384 |
| 13 | nld               | Dutch            |            144340 |       0.983 |    0.927 | 0.946 |  133805 |  2324 | 7314963 | 10535 |
| 14 | fin               | Finnish          |            128011 |       0.986 |    0.964 | 0.968 |  123392 |  1776 | 7331840 |  4619 |
| 15 | pol               | Polish           |            109662 |       0.979 |    0.983 | 0.970 |  107820 |  2367 | 7349598 |  1842 |
| 16 | mkd               | Macedonian       |             77938 |       0.954 |    0.936 | 0.924 |   72941 |  3508 | 7380181 |  4997 |
| 17 | mar               | Marathi          |             64126 |       0.993 |    0.984 | 0.985 |   63072 |   434 | 7397067 |  1054 |
| 18 | lit               | Lithuanian       |             59659 |       0.993 |    0.916 | 0.950 |   54676 |   402 | 7401566 |  4983 |
| 19 | ces               | Czech            |             57030 |       0.923 |    0.908 | 0.881 |   51757 |  4326 | 7400271 |  5273 |
| 20 | dan               | Danish           |             49399 |       0.837 |    0.871 | 0.788 |   43048 |  8398 | 7403830 |  6351 |
| 21 | swe               | Swedish          |             41677 |       0.929 |    0.918 | 0.892 |   38263 |  2925 | 7417025 |  3414 |
| 22 | ara               | Arabic           |             35991 |       1.000 |    0.984 | 0.991 |   35415 |    17 | 7425619 |   576 |
| 23 | ell               | Greek            |             34071 |       1.000 |    0.999 | 0.999 |   34042 |    10 | 7427546 |    29 |
| 24 | ron               | Romanian         |             24943 |       0.978 |    0.891 | 0.922 |   22222 |   509 | 7436175 |  2721 |
| 25 | bul               | Bulgarian        |             24503 |       0.900 |    0.815 | 0.817 |   19969 |  2215 | 7434909 |  4534 |
| 26 | vie               | Vietnamese       |             19234 |       0.987 |    0.988 | 0.981 |   19008 |   250 | 7442143 |   226 |
| 27 | fil               | Filipino         |             16649 |       0.989 |    0.878 | 0.925 |   14619 |   165 | 7444813 |  2030 |
| 28 | slk               | Slovak           |             14660 |       0.884 |    0.478 | 0.596 |    7005 |   919 | 7446048 |  7655 |
| 29 | ind               | Indonesian       |             14542 |       0.955 |    0.880 | 0.897 |   12793 |   602 | 7446483 |  1749 |
| 30 | hin               | Hindi            |             14230 |       0.933 |    0.962 | 0.916 |   13687 |   978 | 7446419 |   543 |
| 31 | nob               | Norwegian Bokmål |             14223 |       0.630 |    0.381 | 0.417 |    5421 |  3190 | 7444214 |  8802 |
| 32 | cat               | Catalan          |              7971 |       0.821 |    0.686 | 0.691 |    5469 |  1196 | 7452460 |  2502 |
| 33 | kor               | Korean           |              7570 |       0.996 |    0.970 | 0.981 |    7344 |    32 | 7454025 |   226 |
| 34 | hrv               | Croatian         |              5204 |       0.702 |    0.353 | 0.427 |    1839 |   781 | 7455642 |  3365 |
| 35 | ben               | Bangla           |              4714 |       0.998 |    0.996 | 0.996 |    4693 |     8 | 7456905 |    21 |
| 36 | afr               | Afrikaans        |              4031 |       0.844 |    0.627 | 0.675 |    2528 |   468 | 7457128 |  1503 |
| 37 | est               | Estonian         |              3637 |       0.745 |    0.654 | 0.622 |    2380 |   816 | 7457174 |  1257 |
| 38 | tha               | Thai             |              3528 |       0.996 |    0.999 | 0.996 |    3524 |    13 | 7458086 |     4 |
| 39 | sqi               | Albanian         |              2526 |       0.967 |    0.835 | 0.883 |    2109 |    72 | 7459029 |   417 |
| 40 | urd               | Urdu             |              2008 |       0.987 |    0.954 | 0.964 |    1915 |    26 | 7459593 |    93 |
| 41 | cym               | Welsh            |              1344 |       0.892 |    0.541 | 0.647 |     727 |    88 | 7460195 |   617 |
| 42 | slv               | Slovenian        |              1093 |       0.226 |    0.431 | 0.197 |     471 |  1611 | 7458923 |   622 |
| 43 | mal               | Malayalam        |               827 |       0.981 |    0.999 | 0.980 |     826 |    16 | 7460784 |     1 |
| 44 | tam               | Tamil            |               334 |       0.991 |    1.000 | 0.991 |     334 |     3 | 7461290 |     0 |
| 45 | tel               | Telugu           |               254 |       0.973 |    1.000 | 0.973 |     254 |     7 | 7461366 |     0 |
| 46 | pan               | Punjabi          |               196 |       0.933 |    1.000 | 0.933 |     196 |    14 | 7461417 |     0 |
| 47 | kan               | Kannada          |               176 |       0.967 |    1.000 | 0.967 |     176 |     6 | 7461445 |     0 |
| 48 | guj               | Gujarati         |               168 |       0.994 |    1.000 | 0.994 |     168 |     1 | 7461458 |     0 |