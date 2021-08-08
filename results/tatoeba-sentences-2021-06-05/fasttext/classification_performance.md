# Classification performance for fasttext on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 8448970 (87.64%)
- **Aggregated accuracy: 0.9826956421907049**

<h2 id="supported-languages">Supported languages (176)</h2>

afr (Afrikaans), als (Tosk Albanian), amh (Amharic), arg (Aragonese), ara (Arabic), arz (Egyptian Arabic), asm (Assamese), ast (Asturian), ava (Avaric), aze (Azerbaijani), azb (South Azerbaijani), bak (Bashkir), bar (Bavarian), bcl (Central Bikol), bel (Belarusian), bul (Bulgarian), bih (Bihari languages), ben (Bangla), bod (Tibetan), bpy (Bishnupriya), bre (Breton), bos (Bosnian), bxr (Russia Buriat), cat (Catalan), cbk (Chavacano), che (Chechen), ceb (Cebuano), ckb (Central Kurdish), cos (Corsican), ces (Czech), chv (Chuvash), cym (Welsh), dan (Danish), deu (German), diq (Dimli (individual language)), dsb (Lower Sorbian), dty (Dotyali), div (Divehi), ell (Greek), eml (Unknown language [eml]), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fra (French), frr (Northern Frisian), fry (Western Frisian), gle (Irish), gla (Scottish Gaelic), glg (Galician), grn (Guarani), gom (Goan Konkani), guj (Gujarati), glv (Manx), heb (Hebrew), hin (Hindi), hif (Fiji Hindi), hrv (Croatian), hsb (Upper Sorbian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ina (Interlingua), ind (Indonesian), ile (Interlingue), ilo (Iloko), ido (Ido), isl (Icelandic), ita (Italian), jpn (Japanese), jbo (Lojban), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), krc (Karachay-Balkar), kur (Kurdish), kom (Komi), cor (Cornish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lez (Lezghian), lim (Limburgish), lmo (Lombard), lao (Lao), lrc (Northern Luri), lit (Lithuanian), lav (Latvian), mai (Maithili), mlg (Malagasy), mhr (Eastern Mari), min (Minangkabau), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), mrj (Western Mari), msa (Malay), mlt (Maltese), mwl (Mirandese), mya (Burmese), myv (Erzya), mzn (Mazanderani), nah (Nahuatl languages), nap (Neapolitan), nds (Low German), nep (Nepali), new (Newari), nld (Dutch), nno (Norwegian Nynorsk), nob (Norwegian Bokmål), oci (Occitan), ori (Odia), oss (Ossetic), pan (Punjabi), pam (Pampanga), pfl (Palatine German), pol (Polish), pms (Piedmontese), pnb (Western Panjabi), pus (Pashto), por (Portuguese), que (Quechua), roh (Romansh), ron (Romanian), rus (Russian), rue (Rusyn), san (Sanskrit), sah (Sakha), srd (Sardinian), scn (Sicilian), sco (Scots), snd (Sindhi), srp (Serbian), sin (Sinhala), slk (Slovak), slv (Slovenian), som (Somali), sqi (Albanian), srp (Serbian), sun (Sundanese), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tgk (Tajik), tha (Thai), tuk (Turkmen), fil (Filipino), tur (Turkish), tat (Tatar), tyv (Tuvinian), uig (Uyghur), ukr (Ukrainian), urd (Urdu), uzb (Uzbek), vec (Venetian), vep (Veps), vie (Vietnamese), vls (West Flemish), vol (Volapük), wln (Walloon), war (Waray), wuu (Wu Chinese), xal (Kalmyk), xmf (Mingrelian), yid (Yiddish), yor (Yoruba), yue (Cantonese), zho (Chinese)

<h2 id="metrics-per-language">Stats per language</h2>

|     | language_alpha3   | language                    |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |   fn |
|----:|:------------------|:----------------------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|-----:|
|   1 | eng               | English                     |           1479733 |       0.991 |    0.999 | 0.991 | 1478395 | 13284 | 6955953 | 1338 |
|   2 | rus               | Russian                     |            849653 |       0.992 |    0.998 | 0.991 |  848237 |  7196 | 7592121 | 1416 |
|   3 | ita               | Italian                     |            787053 |       0.986 |    0.996 | 0.984 |  783712 | 11457 | 7650460 | 3341 |
|   4 | tur               | Turkish                     |            709573 |       0.994 |    0.998 | 0.993 |  707878 |  4273 | 7735124 | 1695 |
|   5 | epo               | Esperanto                   |            659632 |       0.991 |    0.997 | 0.990 |  657892 |  6019 | 7783319 | 1740 |
|   6 | deu               | German                      |            553727 |       0.992 |    0.997 | 0.991 |  552153 |  4248 | 7890995 | 1574 |
|   7 | fra               | French                      |            466192 |       0.988 |    0.994 | 0.985 |  463322 |  5778 | 7977000 | 2870 |
|   8 | por               | Portuguese                  |            385737 |       0.983 |    0.983 | 0.975 |  379214 |  6549 | 8056684 | 6523 |
|   9 | spa               | Spanish                     |            338781 |       0.954 |    0.987 | 0.948 |  334473 | 16093 | 8094096 | 4308 |
|  10 | hun               | Hungarian                   |            323048 |       0.993 |    0.993 | 0.990 |  320862 |  2148 | 8123774 | 2186 |
|  11 | jpn               | Japanese                    |            208761 |       1.000 |    1.000 | 0.999 |  208682 |    68 | 8240141 |   79 |
|  12 | heb               | Hebrew                      |            197226 |       0.998 |    1.000 | 0.998 |  197205 |   382 | 8251362 |   21 |
|  13 | ukr               | Ukrainian                   |            171674 |       0.991 |    0.978 | 0.980 |  167950 |  1569 | 8275727 | 3724 |
|  14 | nld               | Dutch                       |            144340 |       0.977 |    0.955 | 0.955 |  137902 |  3315 | 8301315 | 6438 |
|  15 | fin               | Finnish                     |            128011 |       0.990 |    0.981 | 0.980 |  125521 |  1308 | 8319651 | 2490 |
|  16 | pol               | Polish                      |            109662 |       0.979 |    0.992 | 0.976 |  108795 |  2291 | 8337017 |  867 |
|  17 | mkd               | Macedonian                  |             77938 |       0.942 |    0.986 | 0.936 |   76873 |  4710 | 8366322 | 1065 |
|  18 | mar               | Marathi                     |             64126 |       0.998 |    0.998 | 0.998 |   64016 |   103 | 8384741 |  110 |
|  19 | lit               | Lithuanian                  |             59659 |       0.992 |    0.960 | 0.972 |   57282 |   457 | 8388854 | 2377 |
|  20 | ces               | Czech                       |             57030 |       0.937 |    0.951 | 0.915 |   54248 |  3621 | 8388319 | 2782 |
|  21 | dan               | Danish                      |             49399 |       0.849 |    0.907 | 0.814 |   44828 |  7976 | 8391595 | 4571 |
|  22 | srp               | Serbian                     |             45176 |       0.889 |    0.790 | 0.795 |   35695 |  4463 | 8399331 | 9481 |
|  23 | swe               | Swedish                     |             41677 |       0.946 |    0.948 | 0.922 |   39504 |  2269 | 8405024 | 2173 |
|  24 | lat               | Latin                       |             39718 |       0.960 |    0.892 | 0.907 |   35434 |  1473 | 8407779 | 4284 |
|  25 | ara               | Arabic                      |             35991 |       0.985 |    0.993 | 0.982 |   35750 |   537 | 8412442 |  241 |
|  26 | ell               | Greek                       |             34071 |       0.999 |    1.000 | 0.999 |   34069 |    25 | 8414874 |    2 |
|  27 | ina               | Interlingua                 |             26680 |       0.951 |    0.725 | 0.806 |   19348 |  1004 | 8421286 | 7332 |
|  28 | ron               | Romanian                    |             24943 |       0.964 |    0.937 | 0.934 |   23375 |   864 | 8423163 | 1568 |
|  29 | bul               | Bulgarian                   |             24503 |       0.939 |    0.944 | 0.914 |   23127 |  1493 | 8422974 | 1376 |
|  30 | vie               | Vietnamese                  |             19234 |       0.991 |    0.997 | 0.989 |   19178 |   180 | 8429556 |   56 |
|  31 | nds               | Low German                  |             17921 |       0.917 |    0.872 | 0.859 |   15621 |  1416 | 8429633 | 2300 |
|  32 | fil               | Filipino                    |             16649 |       0.933 |    0.938 | 0.905 |   15621 |  1122 | 8431199 | 1028 |
|  33 | jbo               | Lojban                      |             15925 |       0.994 |    0.952 | 0.970 |   15167 |    94 | 8432951 |  758 |
|  34 | slk               | Slovak                      |             14660 |       0.923 |    0.627 | 0.724 |    9190 |   766 | 8433544 | 5470 |
|  35 | ind               | Indonesian                  |             14542 |       0.919 |    0.921 | 0.884 |   13398 |  1178 | 8433250 | 1144 |
|  36 | hin               | Hindi                       |             14230 |       0.993 |    0.989 | 0.988 |   14076 |   100 | 8434640 |  154 |
|  37 | nob               | Norwegian Bokmål            |             14223 |       0.635 |    0.422 | 0.442 |    5997 |  3451 | 8431296 | 8226 |
|  38 | tat               | Tatar                       |             13674 |       0.986 |    0.955 | 0.964 |   13063 |   186 | 8435110 |  611 |
|  39 | bel               | Belarusian                  |             12633 |       0.985 |    0.899 | 0.934 |   11357 |   171 | 8436166 | 1276 |
|  40 | isl               | Icelandic                   |             11091 |       0.982 |    0.957 | 0.960 |   10614 |   200 | 8437679 |  477 |
|  41 | cat               | Catalan                     |              7971 |       0.842 |    0.800 | 0.761 |    6377 |  1201 | 8439798 | 1594 |
|  42 | uig               | Uyghur                      |              7792 |       0.997 |    0.997 | 0.996 |    7772 |    22 | 8441156 |   20 |
|  43 | kor               | Korean                      |              7570 |       0.993 |    0.994 | 0.990 |    7525 |    53 | 8441347 |   45 |
|  44 | ido               | Ido                         |              7373 |       0.850 |    0.481 | 0.583 |    3544 |   623 | 8440974 | 3829 |
|  45 | ile               | Interlingue                 |              7352 |       0.899 |    0.500 | 0.620 |    3677 |   412 | 8441206 | 3675 |
|  46 | bre               | Breton                      |              7195 |       0.947 |    0.845 | 0.871 |    6077 |   343 | 8441432 | 1118 |
|  47 | yid               | Yiddish                     |              6895 |       0.997 |    0.940 | 0.967 |    6483 |    17 | 8442058 |  412 |
|  48 | tuk               | Turkmen                     |              6729 |       0.991 |    0.483 | 0.647 |    3250 |    30 | 8442211 | 3479 |
|  49 | eus               | Basque                      |              6166 |       0.925 |    0.890 | 0.874 |    5486 |   448 | 8442356 |  680 |
|  50 | yue               | Cantonese                   |              6134 |       0.998 |    0.894 | 0.942 |    5485 |    11 | 8442825 |  649 |
|  51 | kat               | Georgian                    |              5732 |       0.992 |    0.990 | 0.987 |    5672 |    46 | 8443192 |   60 |
|  52 | oci               | Occitan                     |              5693 |       0.943 |    0.720 | 0.797 |    4101 |   246 | 8443031 | 1592 |
|  53 | aze               | Azerbaijani                 |              5348 |       0.896 |    0.839 | 0.825 |    4489 |   520 | 8443102 |  859 |
|  54 | hrv               | Croatian                    |              5204 |       0.438 |    0.451 | 0.346 |    2349 |  3018 | 8440748 | 2855 |
|  55 | ben               | Bangla                      |              4714 |       0.845 |    0.999 | 0.844 |    4709 |   865 | 8443391 |    5 |
|  56 | glg               | Galician                    |              4613 |       0.743 |    0.483 | 0.531 |    2227 |   771 | 8443586 | 2386 |
|  57 | wuu               | Wu Chinese                  |              4549 |       0.995 |    0.854 | 0.917 |    3883 |    18 | 8444403 |  666 |
|  58 | mhr               | Eastern Mari                |              4300 |       0.985 |    0.960 | 0.965 |    4126 |    62 | 8444608 |  174 |
|  59 | vol               | Volapük                     |              4132 |       0.974 |    0.758 | 0.843 |    3133 |    82 | 8444756 |  999 |
|  60 | afr               | Afrikaans                   |              4031 |       0.813 |    0.700 | 0.693 |    2823 |   648 | 8444291 | 1208 |
|  61 | cor               | Cornish                     |              3925 |       0.981 |    0.862 | 0.910 |    3385 |    65 | 8444980 |  540 |
|  62 | kaz               | Kazakh                      |              3685 |       0.967 |    0.948 | 0.942 |    3494 |   121 | 8445164 |  191 |
|  63 | est               | Estonian                    |              3637 |       0.725 |    0.818 | 0.670 |    2975 |  1131 | 8444202 |  662 |
|  64 | tha               | Thai                        |              3528 |       0.999 |    1.000 | 0.999 |    3527 |     2 | 8445440 |    1 |
|  65 | grn               | Guarani                     |              2961 |       0.955 |    0.467 | 0.618 |    1383 |    65 | 8445944 | 1578 |
|  66 | asm               | Assamese                    |              2912 |       1.000 |    0.691 | 0.817 |    2011 |     1 | 8446057 |  901 |
|  67 | frr               | Northern Frisian            |              2855 |       0.455 |    0.002 | 0.003 |       5 |     6 | 8446109 | 2850 |
|  68 | mon               | Mongolian                   |              2757 |       0.976 |    0.917 | 0.935 |    2529 |    63 | 8446150 |  228 |
|  69 | cbk               | Chavacano                   |              2621 |       0.944 |    0.366 | 0.519 |     959 |    57 | 8446292 | 1662 |
|  70 | sqi               | Albanian                    |              2526 |       0.934 |    0.865 | 0.870 |    2184 |   155 | 8446289 |  342 |
|  71 | ilo               | Iloko                       |              2455 |       0.908 |    0.743 | 0.785 |    1824 |   185 | 8446330 |  631 |
|  72 | gle               | Irish                       |              2389 |       0.950 |    0.846 | 0.875 |    2021 |   106 | 8446475 |  368 |
|  73 | hye               | Armenian                    |              2248 |       0.987 |    1.000 | 0.987 |    2247 |    30 | 8446692 |    1 |
|  74 | war               | Waray                       |              2025 |       0.829 |    0.596 | 0.647 |    1207 |   249 | 8446696 |  818 |
|  75 | urd               | Urdu                        |              2008 |       0.944 |    0.982 | 0.935 |    1972 |   118 | 8446844 |   36 |
|  76 | nno               | Norwegian Nynorsk           |              1576 |       0.573 |    0.485 | 0.439 |     764 |   570 | 8446824 |  812 |
|  77 | chv               | Chuvash                     |              1566 |       0.990 |    0.938 | 0.959 |    1469 |    15 | 8447389 |   97 |
|  78 | khm               | Khmer                       |              1511 |       0.984 |    0.991 | 0.979 |    1498 |    25 | 8447434 |   13 |
|  79 | pam               | Pampanga                    |              1482 |       0.954 |    0.776 | 0.839 |    1150 |    55 | 8447433 |  332 |
|  80 | ceb               | Cebuano                     |              1478 |       0.581 |    0.641 | 0.500 |     947 |   683 | 8446809 |  531 |
|  81 | hsb               | Upper Sorbian               |              1423 |       0.851 |    0.435 | 0.548 |     619 |   108 | 8447439 |  804 |
|  82 | cym               | Welsh                       |              1344 |       0.792 |    0.721 | 0.687 |     969 |   255 | 8447371 |  375 |
|  83 | slv               | Slovenian                   |              1093 |       0.307 |    0.510 | 0.268 |     557 |  1256 | 8446621 |  536 |
|  84 | ckb               | Central Kurdish             |              1089 |       0.991 |    0.928 | 0.955 |    1011 |     9 | 8447872 |   78 |
|  85 | gla               | Scottish Gaelic             |              1033 |       0.950 |    0.809 | 0.854 |     836 |    44 | 8447893 |  197 |
|  86 | dsb               | Lower Sorbian               |               991 |       0.918 |    0.511 | 0.638 |     506 |    45 | 8447934 |  485 |
|  87 | sah               | Sakha                       |               943 |       0.972 |    0.962 | 0.954 |     907 |    26 | 8448001 |   36 |
|  88 | xal               | Kalmyk                      |               870 |       0.965 |    0.821 | 0.873 |     714 |    26 | 8448074 |  156 |
|  89 | uzb               | Uzbek                       |               855 |       0.502 |    0.535 | 0.412 |     457 |   453 | 8447662 |  398 |
|  90 | mal               | Malayalam                   |               827 |       0.978 |    1.000 | 0.978 |     827 |    19 | 8448124 |    0 |
|  91 | pms               | Piedmontese                 |               823 |       0.838 |    0.629 | 0.672 |     518 |   100 | 8448047 |  305 |
|  92 | ltz               | Luxembourgish               |               805 |       0.811 |    0.421 | 0.521 |     339 |    79 | 8448086 |  466 |
|  93 | arz               | Egyptian Arabic             |               798 |       0.768 |    0.370 | 0.464 |     295 |    89 | 8448083 |  503 |
|  94 | jav               | Javanese                    |               615 |       0.597 |    0.502 | 0.461 |     309 |   209 | 8448146 |  306 |
|  95 | bos               | Bosnian                     |               567 |       0.030 |    0.044 | 0.022 |      25 |   822 | 8447581 |  542 |
|  96 | mya               | Burmese                     |               433 |       0.991 |    0.998 | 0.990 |     432 |     4 | 8448533 |    1 |
|  97 | que               | Quechua                     |               422 |       0.631 |    0.438 | 0.450 |     185 |   108 | 8448440 |  237 |
|  98 | ori               | Odia                        |               374 |       0.990 |    0.794 | 0.877 |     297 |     3 | 8448593 |   77 |
|  99 | fry               | Western Frisian             |               355 |       0.453 |    0.403 | 0.339 |     143 |   173 | 8448442 |  212 |
| 100 | tam               | Tamil                       |               334 |       0.971 |    1.000 | 0.971 |     334 |    10 | 8448626 |    0 |
| 101 | ast               | Asturian                    |               280 |       0.128 |    0.154 | 0.095 |      43 |   293 | 8448397 |  237 |
| 102 | kir               | Kyrgyz                      |               254 |       0.683 |    0.772 | 0.620 |     196 |    91 | 8448625 |   58 |
| 103 | tel               | Telugu                      |               254 |       0.966 |    1.000 | 0.966 |     254 |     9 | 8448707 |    0 |
| 104 | oss               | Ossetic                     |               236 |       0.982 |    0.911 | 0.937 |     215 |     4 | 8448730 |   21 |
| 105 | lao               | Lao                         |               219 |       0.982 |    0.991 | 0.977 |     217 |     4 | 8448747 |    2 |
| 106 | bak               | Bashkir                     |               215 |       0.684 |    0.874 | 0.652 |     188 |    87 | 8448668 |   27 |
| 107 | nah               | Nahuatl languages           |               212 |       0.767 |    0.156 | 0.249 |      33 |    10 | 8448748 |  179 |
| 108 | amh               | Amharic                     |               211 |       0.991 |    0.995 | 0.988 |     210 |     2 | 8448757 |    1 |
| 109 | mlt               | Maltese                     |               208 |       0.640 |    0.683 | 0.557 |     142 |    80 | 8448682 |   66 |
| 110 | bar               | Bavarian                    |               200 |       0.179 |    0.025 | 0.040 |       5 |    23 | 8448747 |  195 |
| 111 | pan               | Punjabi                     |               196 |       0.995 |    1.000 | 0.995 |     196 |     1 | 8448773 |    0 |
| 112 | vec               | Venetian                    |               190 |       0.565 |    0.137 | 0.203 |      26 |    20 | 8448760 |  164 |
| 113 | kan               | Kannada                     |               176 |       0.898 |    1.000 | 0.898 |     176 |    20 | 8448774 |    0 |
| 114 | guj               | Gujarati                    |               168 |       0.977 |    1.000 | 0.977 |     168 |     4 | 8448798 |    0 |
| 115 | san               | Sanskrit                    |               156 |       0.966 |    0.923 | 0.929 |     144 |     5 | 8448809 |   12 |
| 116 | krc               | Karachay-Balkar             |               148 |       0.674 |    0.209 | 0.297 |      31 |    15 | 8448807 |  117 |
| 117 | min               | Minangkabau                 |               121 |       0.246 |    0.124 | 0.132 |      15 |    46 | 8448803 |  106 |
| 118 | rue               | Rusyn                       |               116 |       0.842 |    0.276 | 0.400 |      32 |     6 | 8448848 |   84 |
| 119 | arg               | Aragonese                   |               103 |       0.071 |    0.019 | 0.025 |       2 |    26 | 8448841 |  101 |
| 120 | mrj               | Western Mari                |                83 |       0.898 |    0.530 | 0.642 |      44 |     5 | 8448882 |   39 |
| 121 | sco               | Scots                       |                82 |       0.100 |    0.037 | 0.043 |       3 |    27 | 8448861 |   79 |
| 122 | som               | Somali                      |                80 |       0.341 |    0.175 | 0.189 |      14 |    27 | 8448863 |   66 |
| 123 | hat               | Haitian Creole              |                64 |       0.091 |    0.078 | 0.059 |       5 |    50 | 8448856 |   59 |
| 124 | tgk               | Tajik                       |                63 |       0.582 |    0.905 | 0.564 |      57 |    41 | 8448866 |    6 |
| 125 | mlg               | Malagasy                    |                59 |       0.410 |    0.271 | 0.264 |      16 |    23 | 8448888 |   43 |
| 126 | xmf               | Mingrelian                  |                58 |       0.267 |    0.276 | 0.198 |      16 |    44 | 8448868 |   42 |
| 127 | wln               | Walloon                     |                53 |       0.405 |    0.321 | 0.283 |      17 |    25 | 8448892 |   36 |
| 128 | sin               | Sinhala                     |                45 |       0.818 |    1.000 | 0.818 |      45 |    10 | 8448915 |    0 |
| 129 | pus               | Pashto                      |                44 |       0.667 |    0.727 | 0.593 |      32 |    16 | 8448910 |   12 |
| 130 | bod               | Tibetan                     |                41 |       0.911 |    1.000 | 0.911 |      41 |     4 | 8448925 |    0 |
| 131 | yor               | Yoruba                      |                37 |       0.595 |    0.676 | 0.521 |      25 |    17 | 8448916 |   12 |
| 132 | scn               | Sicilian                    |                35 |       0.182 |    0.171 | 0.126 |       6 |    27 | 8448908 |   29 |
| 133 | pnb               | Western Panjabi             |                35 |       0.440 |    0.629 | 0.389 |      22 |    28 | 8448907 |   13 |
| 134 | hif               | Fiji Hindi                  |                34 |       0.000 |    0.000 | 0.000 |       0 |     1 | 8448935 |   34 |
| 135 | lim               | Limburgish                  |                33 |       0.096 |    0.152 | 0.076 |       5 |    47 | 8448890 |   28 |
| 136 | glv               | Manx                        |                33 |       0.133 |    0.061 | 0.066 |       2 |    13 | 8448924 |   31 |
| 137 | sun               | Sundanese                   |                31 |       0.029 |    0.194 | 0.027 |       6 |   202 | 8448737 |   25 |
| 138 | lmo               | Lombard                     |                29 |       0.145 |    0.310 | 0.125 |       9 |    53 | 8448888 |   20 |
| 139 | che               | Chechen                     |                28 |       0.421 |    0.571 | 0.364 |      16 |    22 | 8448920 |   12 |
| 140 | div               | Divehi                      |                26 |       0.788 |    1.000 | 0.788 |      26 |     7 | 8448937 |    0 |
| 141 | myv               | Erzya                       |                26 |       0.222 |    0.154 | 0.138 |       4 |    14 | 8448930 |   22 |
| 142 | cos               | Corsican                    |                24 |       0.500 |    0.125 | 0.182 |       3 |     3 | 8448943 |   21 |
| 143 | mwl               | Mirandese                   |                22 |       0.056 |    0.045 | 0.035 |       1 |    17 | 8448931 |   21 |
| 144 | roh               | Romansh                     |                20 |       0.022 |    0.050 | 0.018 |       1 |    44 | 8448906 |   19 |
| 145 | tyv               | Tuvinian                    |                17 |       0.250 |    0.118 | 0.129 |       2 |     6 | 8448947 |   15 |
| 146 | new               | Newari                      |                17 |       0.000 |    0.000 | 0.000 |       0 |    12 | 8448941 |   17 |
| 147 | srd               | Sardinian                   |                15 |       0.167 |    0.133 | 0.108 |       2 |    10 | 8448945 |   13 |
| 148 | vep               | Veps                        |                13 |       0.000 |    0.000 | 0.000 |       0 |    21 | 8448936 |   13 |
| 149 | mai               | Maithili                    |                 8 |       0.214 |    0.375 | 0.182 |       3 |    11 | 8448951 |    5 |
| 150 | snd               | Sindhi                      |                 6 |       0.500 |    0.833 | 0.476 |       5 |     5 | 8448959 |    1 |
| 151 | diq               | Dimli (individual language) |                 6 |       0.000 |    0.000 | 0.000 |       0 |    17 | 8448947 |    6 |
| 152 | bcl               | Central Bikol               |                 5 |       0.000 |    0.000 | 0.000 |       0 |    17 | 8448948 |    5 |
| 153 | gom               | Goan Konkani                |                 4 |       0.032 |    0.500 | 0.032 |       2 |    60 | 8448906 |    2 |
| 154 | pfl               | Palatine German             |                 3 |       0.000 |    0.000 | 0.000 |       0 |    13 | 8448954 |    3 |