# Classification performance for fasttext-compressed on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 8448970 (87.64%)
- **Aggregated accuracy: 96.81%**

<h2 id="supported-languages">Supported languages (176)</h2>

afr (Afrikaans), als (Tosk Albanian), amh (Amharic), arg (Aragonese), ara (Arabic), arz (Egyptian Arabic), asm (Assamese), ast (Asturian), ava (Avaric), aze (Azerbaijani), azb (South Azerbaijani), bak (Bashkir), bar (Bavarian), bcl (Central Bikol), bel (Belarusian), bul (Bulgarian), bih (Bihari languages), ben (Bangla), bod (Tibetan), bpy (Bishnupriya), bre (Breton), bos (Bosnian), bxr (Russia Buriat), cat (Catalan), cbk (Chavacano), che (Chechen), ceb (Cebuano), ckb (Central Kurdish), cos (Corsican), ces (Czech), chv (Chuvash), cym (Welsh), dan (Danish), deu (German), diq (Dimli (individual language)), dsb (Lower Sorbian), dty (Dotyali), div (Divehi), ell (Greek), eml (Unknown language [eml]), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fra (French), frr (Northern Frisian), fry (Western Frisian), gle (Irish), gla (Scottish Gaelic), glg (Galician), grn (Guarani), gom (Goan Konkani), guj (Gujarati), glv (Manx), heb (Hebrew), hin (Hindi), hif (Fiji Hindi), hrv (Croatian), hsb (Upper Sorbian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ina (Interlingua), ind (Indonesian), ile (Interlingue), ilo (Iloko), ido (Ido), isl (Icelandic), ita (Italian), jpn (Japanese), jbo (Lojban), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), krc (Karachay-Balkar), kur (Kurdish), kom (Komi), cor (Cornish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lez (Lezghian), lim (Limburgish), lmo (Lombard), lao (Lao), lrc (Northern Luri), lit (Lithuanian), lav (Latvian), mai (Maithili), mlg (Malagasy), mhr (Eastern Mari), min (Minangkabau), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), mrj (Western Mari), msa (Malay), mlt (Maltese), mwl (Mirandese), mya (Burmese), myv (Erzya), mzn (Mazanderani), nah (Nahuatl languages), nap (Neapolitan), nds (Low German), nep (Nepali), new (Newari), nld (Dutch), nno (Norwegian Nynorsk), nob (Norwegian Bokmål), oci (Occitan), ori (Odia), oss (Ossetic), pan (Punjabi), pam (Pampanga), pfl (Palatine German), pol (Polish), pms (Piedmontese), pnb (Western Panjabi), pus (Pashto), por (Portuguese), que (Quechua), roh (Romansh), ron (Romanian), rus (Russian), rue (Rusyn), san (Sanskrit), sah (Sakha), srd (Sardinian), scn (Sicilian), sco (Scots), snd (Sindhi), srp (Serbian), sin (Sinhala), slk (Slovak), slv (Slovenian), som (Somali), sqi (Albanian), srp (Serbian), sun (Sundanese), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tgk (Tajik), tha (Thai), tuk (Turkmen), fil (Filipino), tur (Turkish), tat (Tatar), tyv (Tuvinian), uig (Uyghur), ukr (Ukrainian), urd (Urdu), uzb (Uzbek), vec (Venetian), vep (Veps), vie (Vietnamese), vls (West Flemish), vol (Volapük), wln (Walloon), war (Waray), wuu (Wu Chinese), xal (Kalmyk), xmf (Mingrelian), yid (Yiddish), yor (Yoruba), yue (Cantonese), zho (Chinese)

<h2 id="metrics-per-language">Stats per language</h2>

|     | language_alpha3   | language                    |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |    fn |
|----:|:------------------|:----------------------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|------:|
|   1 | eng               | English                     |           1479733 |       0.979 |    0.997 | 0.978 | 1475222 | 31575 | 6937662 |  4511 |
|   2 | rus               | Russian                     |            849653 |       0.969 |    0.996 | 0.967 |  846620 | 27344 | 7571973 |  3033 |
|   3 | ita               | Italian                     |            787053 |       0.969 |    0.987 | 0.963 |  776749 | 24795 | 7637122 | 10304 |
|   4 | tur               | Turkish                     |            709573 |       0.991 |    0.994 | 0.988 |  705300 |  6120 | 7733277 |  4273 |
|   5 | epo               | Esperanto                   |            659632 |       0.984 |    0.993 | 0.981 |  654744 | 10481 | 7778857 |  4888 |
|   6 | deu               | German                      |            553727 |       0.985 |    0.993 | 0.981 |  549727 |  8561 | 7886682 |  4000 |
|   7 | fra               | French                      |            466192 |       0.972 |    0.988 | 0.966 |  460626 | 13434 | 7969344 |  5566 |
|   8 | por               | Portuguese                  |            385737 |       0.976 |    0.965 | 0.959 |  372107 |  9154 | 8054079 | 13630 |
|   9 | spa               | Spanish                     |            338781 |       0.913 |    0.977 | 0.903 |  331141 | 31633 | 8078556 |  7640 |
|  10 | hun               | Hungarian                   |            323048 |       0.986 |    0.981 | 0.977 |  316851 |  4477 | 8121445 |  6197 |
|  11 | jpn               | Japanese                    |            208761 |       0.995 |    0.997 | 0.993 |  208113 |  1054 | 8239155 |   648 |
|  12 | heb               | Hebrew                      |            197226 |       0.994 |    0.999 | 0.994 |  197021 |  1184 | 8250560 |   205 |
|  13 | ukr               | Ukrainian                   |            171674 |       0.979 |    0.916 | 0.937 |  157290 |  3404 | 8273892 | 14384 |
|  14 | nld               | Dutch                       |            144340 |       0.967 |    0.927 | 0.931 |  133805 |  4601 | 8300029 | 10535 |
|  15 | fin               | Finnish                     |            128011 |       0.977 |    0.964 | 0.959 |  123392 |  2947 | 8318012 |  4619 |
|  16 | pol               | Polish                      |            109662 |       0.965 |    0.983 | 0.958 |  107820 |  3861 | 8335447 |  1842 |
|  17 | mkd               | Macedonian                  |             77938 |       0.889 |    0.936 | 0.862 |   72941 |  9146 | 8361886 |  4997 |
|  18 | mar               | Marathi                     |             64126 |       0.993 |    0.984 | 0.985 |   63072 |   455 | 8384389 |  1054 |
|  19 | lit               | Lithuanian                  |             59659 |       0.987 |    0.916 | 0.945 |   54676 |   706 | 8388605 |  4983 |
|  20 | ces               | Czech                       |             57030 |       0.908 |    0.908 | 0.868 |   51757 |  5257 | 8386683 |  5273 |
|  21 | dan               | Danish                      |             49399 |       0.827 |    0.871 | 0.780 |   43048 |  8994 | 8390577 |  6351 |
|  22 | srp               | Serbian                     |             45176 |       0.827 |    0.669 | 0.687 |   30221 |  6311 | 8397483 | 14955 |
|  23 | swe               | Swedish                     |             41677 |       0.913 |    0.918 | 0.877 |   38263 |  3664 | 8403629 |  3414 |
|  24 | lat               | Latin                       |             39718 |       0.941 |    0.771 | 0.825 |   30608 |  1933 | 8407319 |  9110 |
|  25 | ara               | Arabic                      |             35991 |       0.975 |    0.984 | 0.967 |   35415 |   917 | 8412062 |   576 |
|  26 | ell               | Greek                       |             34071 |       0.999 |    0.999 | 0.999 |   34042 |    19 | 8414880 |    29 |
|  27 | ina               | Interlingua                 |             26680 |       0.942 |    0.574 | 0.697 |   15302 |   948 | 8421342 | 11378 |
|  28 | ron               | Romanian                    |             24943 |       0.960 |    0.891 | 0.907 |   22222 |   930 | 8423097 |  2721 |
|  29 | bul               | Bulgarian                   |             24503 |       0.868 |    0.815 | 0.790 |   19969 |  3048 | 8421419 |  4534 |
|  30 | vie               | Vietnamese                  |             19234 |       0.982 |    0.988 | 0.977 |   19008 |   339 | 8429397 |   226 |
|  31 | nds               | Low German                  |             17921 |       0.896 |    0.787 | 0.799 |   14102 |  1636 | 8429413 |  3819 |
|  32 | fil               | Filipino                    |             16649 |       0.922 |    0.878 | 0.866 |   14619 |  1243 | 8431078 |  2030 |
|  33 | jbo               | Lojban                      |             15925 |       0.977 |    0.895 | 0.924 |   14245 |   331 | 8432714 |  1680 |
|  34 | slk               | Slovak                      |             14660 |       0.863 |    0.478 | 0.586 |    7005 |  1113 | 8433197 |  7655 |
|  35 | ind               | Indonesian                  |             14542 |       0.912 |    0.880 | 0.858 |   12793 |  1237 | 8433191 |  1749 |
|  36 | hin               | Hindi                       |             14230 |       0.927 |    0.962 | 0.910 |   13687 |  1075 | 8433665 |   543 |
|  37 | nob               | Norwegian Bokmål            |             14223 |       0.584 |    0.381 | 0.396 |    5421 |  3860 | 8430887 |  8802 |
|  38 | tat               | Tatar                       |             13674 |       0.956 |    0.850 | 0.882 |   11627 |   537 | 8434759 |  2047 |
|  39 | bel               | Belarusian                  |             12633 |       0.957 |    0.712 | 0.802 |    9000 |   400 | 8435937 |  3633 |
|  40 | isl               | Icelandic                   |             11091 |       0.978 |    0.922 | 0.939 |   10221 |   231 | 8437648 |   870 |
|  41 | cat               | Catalan                     |              7971 |       0.722 |    0.686 | 0.620 |    5469 |  2104 | 8438895 |  2502 |
|  42 | uig               | Uyghur                      |              7792 |       0.996 |    0.978 | 0.985 |    7624 |    34 | 8441144 |   168 |
|  43 | kor               | Korean                      |              7570 |       0.992 |    0.970 | 0.977 |    7344 |    59 | 8441341 |   226 |
|  44 | ido               | Ido                         |              7373 |       0.836 |    0.362 | 0.482 |    2671 |   524 | 8441073 |  4702 |
|  45 | ile               | Interlingue                 |              7352 |       0.854 |    0.299 | 0.427 |    2201 |   375 | 8441243 |  5151 |
|  46 | bre               | Breton                      |              7195 |       0.941 |    0.739 | 0.807 |    5318 |   335 | 8441440 |  1877 |
|  47 | yid               | Yiddish                     |              6895 |       0.969 |    0.823 | 0.877 |    5673 |   184 | 8441891 |  1222 |
|  48 | tuk               | Turkmen                     |              6729 |       0.991 |    0.403 | 0.572 |    2714 |    25 | 8442216 |  4015 |
|  49 | eus               | Basque                      |              6166 |       0.884 |    0.783 | 0.788 |    4830 |   635 | 8442169 |  1336 |
|  50 | yue               | Cantonese                   |              6134 |       0.985 |    0.645 | 0.775 |    3958 |    59 | 8442777 |  2176 |
|  51 | kat               | Georgian                    |              5732 |       0.990 |    0.987 | 0.984 |    5657 |    57 | 8443181 |    75 |
|  52 | oci               | Occitan                     |              5693 |       0.914 |    0.544 | 0.661 |    3095 |   291 | 8442986 |  2598 |
|  53 | aze               | Azerbaijani                 |              5348 |       0.924 |    0.725 | 0.786 |    3879 |   320 | 8443302 |  1469 |
|  54 | hrv               | Croatian                    |              5204 |       0.373 |    0.353 | 0.278 |    1839 |  3089 | 8440677 |  3365 |
|  55 | ben               | Bangla                      |              4714 |       0.804 |    0.996 | 0.802 |    4693 |  1145 | 8443111 |    21 |
|  56 | glg               | Galician                    |              4613 |       0.657 |    0.323 | 0.389 |    1492 |   780 | 8443577 |  3121 |
|  57 | wuu               | Wu Chinese                  |              4549 |       0.949 |    0.544 | 0.679 |    2474 |   134 | 8444287 |  2075 |
|  58 | mhr               | Eastern Mari                |              4300 |       0.972 |    0.721 | 0.818 |    3099 |    89 | 8444581 |  1201 |
|  59 | vol               | Volapük                     |              4132 |       0.932 |    0.460 | 0.603 |    1902 |   139 | 8444699 |  2230 |
|  60 | afr               | Afrikaans                   |              4031 |       0.798 |    0.627 | 0.645 |    2528 |   641 | 8444298 |  1503 |
|  61 | cor               | Cornish                     |              3925 |       0.962 |    0.769 | 0.841 |    3020 |   119 | 8444926 |   905 |
|  62 | kaz               | Kazakh                      |              3685 |       0.870 |    0.871 | 0.817 |    3210 |   481 | 8444804 |   475 |
|  63 | est               | Estonian                    |              3637 |       0.606 |    0.654 | 0.523 |    2380 |  1545 | 8443788 |  1257 |
|  64 | tha               | Thai                        |              3528 |       0.995 |    0.999 | 0.995 |    3524 |    17 | 8445425 |     4 |
|  65 | grn               | Guarani                     |              2961 |       0.935 |    0.223 | 0.355 |     659 |    46 | 8445963 |  2302 |
|  66 | asm               | Assamese                    |              2912 |       0.995 |    0.594 | 0.742 |    1729 |     9 | 8446049 |  1183 |
|  67 | frr               | Northern Frisian            |              2855 |       0.000 |    0.000 | 0.000 |       0 |     3 | 8446112 |  2855 |
|  68 | mon               | Mongolian                   |              2757 |       0.929 |    0.750 | 0.804 |    2069 |   159 | 8446054 |   688 |
|  69 | cbk               | Chavacano                   |              2621 |       0.844 |    0.204 | 0.319 |     534 |    99 | 8446250 |  2087 |
|  70 | sqi               | Albanian                    |              2526 |       0.930 |    0.835 | 0.852 |    2109 |   159 | 8446285 |   417 |
|  71 | ilo               | Iloko                       |              2455 |       0.880 |    0.600 | 0.680 |    1472 |   200 | 8446315 |   983 |
|  72 | gle               | Irish                       |              2389 |       0.890 |    0.684 | 0.738 |    1634 |   202 | 8446379 |   755 |
|  73 | hye               | Armenian                    |              2248 |       0.990 |    0.992 | 0.987 |    2231 |    22 | 8446700 |    17 |
|  74 | war               | Waray                       |              2025 |       0.752 |    0.420 | 0.495 |     850 |   280 | 8446665 |  1175 |
|  75 | urd               | Urdu                        |              2008 |       0.950 |    0.954 | 0.929 |    1915 |   100 | 8446862 |    93 |
|  76 | nno               | Norwegian Nynorsk           |              1576 |       0.568 |    0.414 | 0.405 |     653 |   497 | 8446897 |   923 |
|  77 | chv               | Chuvash                     |              1566 |       0.992 |    0.683 | 0.806 |    1070 |     9 | 8447395 |   496 |
|  78 | khm               | Khmer                       |              1511 |       0.965 |    0.981 | 0.957 |    1483 |    53 | 8447406 |    28 |
|  79 | pam               | Pampanga                    |              1482 |       0.923 |    0.333 | 0.479 |     493 |    41 | 8447447 |   989 |
|  80 | ceb               | Cebuano                     |              1478 |       0.364 |    0.415 | 0.290 |     613 |  1070 | 8446422 |   865 |
|  81 | hsb               | Upper Sorbian               |              1423 |       0.702 |    0.247 | 0.339 |     351 |   149 | 8447398 |  1072 |
|  82 | cym               | Welsh                       |              1344 |       0.649 |    0.541 | 0.509 |     727 |   394 | 8447232 |   617 |
|  83 | slv               | Slovenian                   |              1093 |       0.141 |    0.431 | 0.129 |     471 |  2878 | 8444999 |   622 |
|  84 | ckb               | Central Kurdish             |              1089 |       0.958 |    0.842 | 0.879 |     917 |    40 | 8447841 |   172 |
|  85 | gla               | Scottish Gaelic             |              1033 |       0.936 |    0.639 | 0.740 |     660 |    45 | 8447892 |   373 |
|  86 | dsb               | Lower Sorbian               |               991 |       0.909 |    0.222 | 0.351 |     220 |    22 | 8447957 |   771 |
|  87 | sah               | Sakha                       |               943 |       0.948 |    0.758 | 0.824 |     715 |    39 | 8447988 |   228 |
|  88 | xal               | Kalmyk                      |               870 |       0.956 |    0.249 | 0.392 |     217 |    10 | 8448090 |   653 |
|  89 | uzb               | Uzbek                       |               855 |       0.303 |    0.214 | 0.195 |     183 |   421 | 8447694 |   672 |
|  90 | mal               | Malayalam                   |               827 |       0.973 |    0.999 | 0.972 |     826 |    23 | 8448120 |     1 |
|  91 | pms               | Piedmontese                 |               823 |       0.744 |    0.469 | 0.523 |     386 |   133 | 8448014 |   437 |
|  92 | ltz               | Luxembourgish               |               805 |       0.666 |    0.366 | 0.423 |     295 |   148 | 8448017 |   510 |
|  93 | arz               | Egyptian Arabic             |               798 |       0.375 |    0.045 | 0.075 |      36 |    60 | 8448112 |   762 |
|  94 | jav               | Javanese                    |               615 |       0.532 |    0.333 | 0.347 |     205 |   180 | 8448175 |   410 |
|  95 | bos               | Bosnian                     |               567 |       0.012 |    0.016 | 0.009 |       9 |   756 | 8447647 |   558 |
|  96 | mya               | Burmese                     |               433 |       0.989 |    0.998 | 0.987 |     432 |     5 | 8448532 |     1 |
|  97 | que               | Quechua                     |               422 |       0.629 |    0.254 | 0.327 |     107 |    63 | 8448485 |   315 |
|  98 | ori               | Odia                        |               374 |       0.982 |    0.741 | 0.838 |     277 |     5 | 8448591 |    97 |
|  99 | fry               | Western Frisian             |               355 |       0.311 |    0.307 | 0.230 |     109 |   242 | 8448373 |   246 |
| 100 | tam               | Tamil                       |               334 |       0.968 |    1.000 | 0.968 |     334 |    11 | 8448625 |     0 |
| 101 | ast               | Asturian                    |               280 |       0.087 |    0.104 | 0.063 |      29 |   303 | 8448387 |   251 |
| 102 | kir               | Kyrgyz                      |               254 |       0.296 |    0.535 | 0.263 |     136 |   323 | 8448393 |   118 |
| 103 | tel               | Telugu                      |               254 |       0.962 |    1.000 | 0.962 |     254 |    10 | 8448706 |     0 |
| 104 | oss               | Ossetic                     |               236 |       0.936 |    0.686 | 0.771 |     162 |    11 | 8448723 |    74 |
| 105 | lao               | Lao                         |               219 |       0.962 |    0.817 | 0.869 |     179 |     7 | 8448744 |    40 |
| 106 | bak               | Bashkir                     |               215 |       0.399 |    0.688 | 0.366 |     148 |   223 | 8448532 |    67 |
| 107 | nah               | Nahuatl languages           |               212 |       0.292 |    0.033 | 0.055 |       7 |    17 | 8448741 |   205 |
| 108 | amh               | Amharic                     |               211 |       0.995 |    0.981 | 0.986 |     207 |     1 | 8448758 |     4 |
| 109 | mlt               | Maltese                     |               208 |       0.633 |    0.423 | 0.442 |      88 |    51 | 8448711 |   120 |
| 110 | bar               | Bavarian                    |               200 |       0.111 |    0.015 | 0.024 |       3 |    24 | 8448746 |   197 |
| 111 | pan               | Punjabi                     |               196 |       0.929 |    1.000 | 0.929 |     196 |    15 | 8448759 |     0 |
| 112 | vec               | Venetian                    |               190 |       0.641 |    0.132 | 0.206 |      25 |    14 | 8448766 |   165 |
| 113 | kan               | Kannada                     |               176 |       0.946 |    1.000 | 0.946 |     176 |    10 | 8448784 |     0 |
| 114 | guj               | Gujarati                    |               168 |       0.971 |    1.000 | 0.971 |     168 |     5 | 8448797 |     0 |
| 115 | san               | Sanskrit                    |               156 |       0.788 |    0.500 | 0.565 |      78 |    21 | 8448793 |    78 |
| 116 | krc               | Karachay-Balkar             |               148 |       0.613 |    0.128 | 0.199 |      19 |    12 | 8448810 |   129 |
| 117 | min               | Minangkabau                 |               121 |       0.160 |    0.033 | 0.048 |       4 |    21 | 8448828 |   117 |
| 118 | rue               | Rusyn                       |               116 |       0.000 |    0.000 | 0.000 |       0 |     2 | 8448852 |   116 |
| 119 | arg               | Aragonese                   |               103 |       0.074 |    0.019 | 0.026 |       2 |    25 | 8448842 |   101 |
| 120 | mrj               | Western Mari                |                83 |       0.711 |    0.325 | 0.409 |      27 |    11 | 8448876 |    56 |
| 121 | sco               | Scots                       |                82 |       0.286 |    0.073 | 0.102 |       6 |    15 | 8448873 |    76 |
| 122 | som               | Somali                      |                80 |       0.077 |    0.025 | 0.031 |       2 |    24 | 8448866 |    78 |
| 123 | hat               | Haitian Creole              |                64 |       0.036 |    0.016 | 0.017 |       1 |    27 | 8448879 |    63 |
| 124 | tgk               | Tajik                       |                63 |       0.475 |    0.603 | 0.411 |      38 |    42 | 8448865 |    25 |
| 125 | mlg               | Malagasy                    |                59 |       0.214 |    0.153 | 0.134 |       9 |    33 | 8448878 |    50 |
| 126 | xmf               | Mingrelian                  |                58 |       0.050 |    0.052 | 0.034 |       3 |    57 | 8448855 |    55 |
| 127 | wln               | Walloon                     |                53 |       0.245 |    0.226 | 0.173 |      12 |    37 | 8448880 |    41 |
| 128 | sin               | Sinhala                     |                45 |       0.763 |    1.000 | 0.763 |      45 |    14 | 8448911 |     0 |
| 129 | pus               | Pashto                      |                44 |       0.621 |    0.409 | 0.429 |      18 |    11 | 8448915 |    26 |
| 130 | bod               | Tibetan                     |                41 |       0.891 |    1.000 | 0.891 |      41 |     5 | 8448924 |     0 |
| 131 | yor               | Yoruba                      |                37 |       0.226 |    0.189 | 0.152 |       7 |    24 | 8448909 |    30 |
| 132 | scn               | Sicilian                    |                35 |       0.182 |    0.171 | 0.126 |       6 |    27 | 8448908 |    29 |
| 133 | pnb               | Western Panjabi             |                35 |       0.179 |    0.429 | 0.160 |      15 |    69 | 8448866 |    20 |
| 134 | hif               | Fiji Hindi                  |                34 |     nan     |    0.000 | 0.000 |       0 |     0 | 8448936 |    34 |
| 135 | lim               | Limburgish                  |                33 |       0.091 |    0.121 | 0.068 |       4 |    40 | 8448897 |    29 |
| 136 | glv               | Manx                        |                33 |       0.034 |    0.030 | 0.022 |       1 |    28 | 8448909 |    32 |
| 137 | sun               | Sundanese                   |                31 |       0.008 |    0.032 | 0.007 |       1 |   124 | 8448815 |    30 |
| 138 | lmo               | Lombard                     |                29 |       0.050 |    0.103 | 0.041 |       3 |    57 | 8448884 |    26 |
| 139 | che               | Chechen                     |                28 |       0.275 |    0.393 | 0.227 |      11 |    29 | 8448913 |    17 |
| 140 | div               | Divehi                      |                26 |       0.806 |    0.962 | 0.794 |      25 |     6 | 8448938 |     1 |
| 141 | myv               | Erzya                       |                26 |       0.000 |    0.000 | 0.000 |       0 |     3 | 8448941 |    26 |
| 142 | cos               | Corsican                    |                24 |       0.125 |    0.042 | 0.051 |       1 |     7 | 8448939 |    23 |
| 143 | mwl               | Mirandese                   |                22 |       0.059 |    0.045 | 0.036 |       1 |    16 | 8448932 |    21 |
| 144 | roh               | Romansh                     |                20 |       0.037 |    0.050 | 0.027 |       1 |    26 | 8448924 |    19 |
| 145 | tyv               | Tuvinian                    |                17 |       0.500 |    0.059 | 0.100 |       1 |     1 | 8448952 |    16 |
| 146 | new               | Newari                      |                17 |       0.023 |    0.059 | 0.020 |       1 |    42 | 8448911 |    16 |
| 147 | srd               | Sardinian                   |                15 |       0.000 |    0.000 | 0.000 |       0 |     7 | 8448948 |    15 |
| 148 | vep               | Veps                        |                13 |       0.000 |    0.000 | 0.000 |       0 |    18 | 8448939 |    13 |
| 149 | mai               | Maithili                    |                 8 |       0.200 |    0.125 | 0.118 |       1 |     4 | 8448958 |     7 |
| 150 | snd               | Sindhi                      |                 6 |       0.286 |    0.333 | 0.222 |       2 |     5 | 8448959 |     4 |
| 151 | diq               | Dimli (individual language) |                 6 |       0.000 |    0.000 | 0.000 |       0 |    12 | 8448952 |     6 |
| 152 | bcl               | Central Bikol               |                 5 |       0.000 |    0.000 | 0.000 |       0 |     9 | 8448956 |     5 |
| 153 | gom               | Goan Konkani                |                 4 |       0.000 |    0.000 | 0.000 |       0 |    53 | 8448913 |     4 |
| 154 | pfl               | Palatine German             |                 3 |       0.000 |    0.000 | 0.000 |       0 |    13 | 8448954 |     3 |