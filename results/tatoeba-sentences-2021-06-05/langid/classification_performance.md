# Classification performance for langid on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 8298609 (86.08%)
- **Aggregated accuracy: 0.8899956607185614**

<h2 id="supported-languages">Supported languages (97)</h2>

afr (Afrikaans), amh (Amharic), arg (Aragonese), ara (Arabic), asm (Assamese), aze (Azerbaijani), bel (Belarusian), bul (Bulgarian), ben (Bangla), bre (Breton), bos (Bosnian), cat (Catalan), ces (Czech), cym (Welsh), dan (Danish), deu (German), dzo (Dzongkha), ell (Greek), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fao (Faroese), fra (French), gle (Irish), glg (Galician), guj (Gujarati), heb (Hebrew), hin (Hindi), hrv (Croatian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ind (Indonesian), isl (Icelandic), ita (Italian), jpn (Japanese), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), kur (Kurdish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lao (Lao), lit (Lithuanian), lav (Latvian), mlg (Malagasy), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), msa (Malay), mlt (Maltese), nob (Norwegian Bokmål), nep (Nepali), nld (Dutch), nno (Norwegian Nynorsk), nob (Norwegian Bokmål), oci (Occitan), ori (Odia), pan (Punjabi), pol (Polish), pus (Pashto), por (Portuguese), que (Quechua), ron (Romanian), rus (Russian), kin (Kinyarwanda), sme (Northern Sami), sin (Sinhala), slk (Slovak), slv (Slovenian), sqi (Albanian), srp (Serbian), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tha (Thai), fil (Filipino), tur (Turkish), uig (Uyghur), ukr (Ukrainian), urd (Urdu), vie (Vietnamese), vol (Volapük), wln (Walloon), xho (Xhosa), zho (Chinese), zul (Zulu)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |     fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|-------:|
|  1 | eng               | English           |           1479733 |       0.953 |    0.973 | 0.941 | 1439789 | 70832 | 6748044 |  39944 |
|  2 | rus               | Russian           |            849653 |       0.966 |    0.823 | 0.875 |  699008 | 24596 | 7424360 | 150645 |
|  3 | ita               | Italian           |            787053 |       0.954 |    0.885 | 0.898 |  696690 | 33674 | 7477882 |  90363 |
|  4 | tur               | Turkish           |            709573 |       0.995 |    0.919 | 0.953 |  652061 |  3202 | 7585834 |  57512 |
|  5 | epo               | Esperanto         |            659632 |       0.983 |    0.854 | 0.907 |  563174 |  9712 | 7629265 |  96458 |
|  6 | deu               | German            |            553727 |       0.950 |    0.974 | 0.938 |  539237 | 28349 | 7716533 |  14490 |
|  7 | fra               | French            |            466192 |       0.897 |    0.935 | 0.870 |  436032 | 49971 | 7782446 |  30160 |
|  8 | por               | Portuguese        |            385737 |       0.915 |    0.822 | 0.832 |  317068 | 29566 | 7883306 |  68669 |
|  9 | spa               | Spanish           |            338781 |       0.784 |    0.837 | 0.728 |  283448 | 78313 | 7881515 |  55333 |
| 10 | hun               | Hungarian         |            323048 |       0.977 |    0.929 | 0.942 |  300114 |  7043 | 7968518 |  22934 |
| 11 | jpn               | Japanese          |            208761 |       0.997 |    1.000 | 0.997 |  208702 |   585 | 8089263 |     59 |
| 12 | heb               | Hebrew            |            197226 |       1.000 |    0.999 | 1.000 |  197110 |    14 | 8101369 |    116 |
| 13 | ukr               | Ukrainian         |            171674 |       0.748 |    0.774 | 0.675 |  132961 | 44688 | 8082247 |  38713 |
| 14 | nld               | Dutch             |            144340 |       0.869 |    0.901 | 0.830 |  130115 | 19610 | 8134659 |  14225 |
| 15 | fin               | Finnish           |            128011 |       0.941 |    0.931 | 0.909 |  119175 |  7527 | 8163071 |   8836 |
| 16 | pol               | Polish            |            109662 |       0.944 |    0.977 | 0.933 |  107088 |  6349 | 8182598 |   2574 |
| 17 | mkd               | Macedonian        |             77938 |       0.582 |    0.482 | 0.443 |   37554 | 27012 | 8193659 |  40384 |
| 18 | mar               | Marathi           |             64126 |       0.988 |    0.700 | 0.815 |   44902 |   563 | 8233920 |  19224 |
| 19 | lit               | Lithuanian        |             59659 |       0.774 |    0.915 | 0.747 |   54565 | 15938 | 8223012 |   5094 |
| 20 | ces               | Czech             |             57030 |       0.879 |    0.837 | 0.809 |   47732 |  6594 | 8234985 |   9298 |
| 21 | dan               | Danish            |             49399 |       0.739 |    0.602 | 0.594 |   29753 | 10483 | 8238727 |  19646 |
| 22 | srp               | Serbian           |             45176 |       0.214 |    0.392 | 0.184 |   17727 | 64947 | 8188486 |  27449 |
| 23 | swe               | Swedish           |             41677 |       0.782 |    0.802 | 0.713 |   33438 |  9345 | 8247587 |   8239 |
| 24 | lat               | Latin             |             39718 |       0.939 |    0.196 | 0.322 |    7803 |   509 | 8258382 |  31915 |
| 25 | ara               | Arabic            |             35991 |       0.999 |    0.950 | 0.973 |   34184 |    46 | 8262572 |   1807 |
| 26 | ell               | Greek             |             34071 |       1.000 |    1.000 | 1.000 |   34071 |    15 | 8264523 |      0 |
| 27 | ron               | Romanian          |             24943 |       0.637 |    0.906 | 0.617 |   22605 | 12867 | 8260799 |   2338 |
| 28 | bul               | Bulgarian         |             24503 |       0.209 |    0.624 | 0.197 |   15278 | 57734 | 8216372 |   9225 |
| 29 | vie               | Vietnamese        |             19234 |       0.956 |    0.998 | 0.955 |   19192 |   886 | 8278489 |     42 |
| 30 | fil               | Filipino          |             16649 |       0.876 |    0.792 | 0.786 |   13181 |  1860 | 8280100 |   3468 |
| 31 | slk               | Slovak            |             14660 |       0.525 |    0.690 | 0.470 |   10119 |  9140 | 8274809 |   4541 |
| 32 | ind               | Indonesian        |             14542 |       0.528 |    0.731 | 0.481 |   10632 |  9494 | 8274573 |   3910 |
| 33 | hin               | Hindi             |             14230 |       0.420 |    0.901 | 0.410 |   12825 | 17727 | 8266652 |   1405 |
| 34 | nob               | Norwegian Bokmål  |             14223 |       0.305 |    0.770 | 0.292 |   10958 | 24918 | 8259468 |   3265 |
| 35 | bel               | Belarusian        |             12633 |       0.437 |    0.879 | 0.424 |   11106 | 14321 | 8271655 |   1527 |
| 36 | isl               | Icelandic         |             11091 |       0.874 |    0.929 | 0.846 |   10300 |  1484 | 8286034 |    791 |
| 37 | cat               | Catalan           |              7971 |       0.200 |    0.720 | 0.193 |    5739 | 22950 | 8267688 |   2232 |
| 38 | uig               | Uyghur            |              7792 |       0.961 |    0.989 | 0.956 |    7707 |   316 | 8290501 |     85 |
| 39 | kor               | Korean            |              7570 |       0.989 |    1.000 | 0.989 |    7568 |    83 | 8290956 |      2 |
| 40 | bre               | Breton            |              7195 |       0.423 |    0.630 | 0.377 |    4535 |  6179 | 8285235 |   2660 |
| 41 | eus               | Basque            |              6166 |       0.324 |    0.866 | 0.316 |    5338 | 11150 | 8281293 |    828 |
| 42 | kat               | Georgian          |              5732 |       0.997 |    0.996 | 0.995 |    5710 |    19 | 8292858 |     22 |
| 43 | oci               | Occitan           |              5693 |       0.341 |    0.505 | 0.292 |    2873 |  5547 | 8287369 |   2820 |
| 44 | aze               | Azerbaijani       |              5348 |       0.233 |    0.756 | 0.224 |    4044 | 13343 | 8279918 |   1304 |
| 45 | hrv               | Croatian          |              5204 |       0.155 |    0.650 | 0.149 |    3384 | 18473 | 8274932 |   1820 |
| 46 | ben               | Bangla            |              4714 |       0.659 |    0.977 | 0.654 |    4605 |  2380 | 8291515 |    109 |
| 47 | glg               | Galician          |              4613 |       0.066 |    0.520 | 0.064 |    2400 | 33789 | 8260207 |   2213 |
| 48 | vol               | Volapük           |              4132 |       0.554 |    0.265 | 0.313 |    1093 |   880 | 8293597 |   3039 |
| 49 | afr               | Afrikaans         |              4031 |       0.300 |    0.462 | 0.255 |    1861 |  4338 | 8290240 |   2170 |
| 50 | kaz               | Kazakh            |              3685 |       0.368 |    0.943 | 0.364 |    3476 |  5968 | 8288956 |    209 |
| 51 | est               | Estonian          |              3637 |       0.226 |    0.689 | 0.215 |    2505 |  8560 | 8286412 |   1132 |
| 52 | tha               | Thai              |              3528 |       0.998 |    1.000 | 0.998 |    3528 |     7 | 8295074 |      0 |
| 53 | asm               | Assamese          |              2912 |       0.853 |    0.227 | 0.348 |     662 |   114 | 8295583 |   2250 |
| 54 | mon               | Mongolian         |              2757 |       0.288 |    0.950 | 0.286 |    2618 |  6463 | 8289389 |    139 |
| 55 | sqi               | Albanian          |              2526 |       0.764 |    0.905 | 0.735 |    2285 |   704 | 8295379 |    241 |
| 56 | gle               | Irish             |              2389 |       0.392 |    0.840 | 0.378 |    2007 |  3108 | 8293112 |    382 |
| 57 | hye               | Armenian          |              2248 |       0.992 |    0.911 | 0.946 |    2048 |    17 | 8296344 |    200 |
| 58 | urd               | Urdu              |              2008 |       0.853 |    0.947 | 0.833 |    1901 |   328 | 8296273 |    107 |
| 59 | nno               | Norwegian Nynorsk |              1576 |       0.144 |    0.501 | 0.134 |     789 |  4696 | 8292337 |    787 |
| 60 | khm               | Khmer             |              1511 |       0.997 |    0.975 | 0.985 |    1473 |     4 | 8297094 |     38 |
| 61 | cym               | Welsh             |              1344 |       0.300 |    0.682 | 0.281 |     916 |  2133 | 8295132 |    428 |
| 62 | slv               | Slovenian         |              1093 |       0.044 |    0.681 | 0.044 |     744 | 16127 | 8281389 |    349 |
| 63 | mal               | Malayalam         |               827 |       1.000 |    1.000 | 1.000 |     827 |     0 | 8297782 |      0 |
| 64 | ltz               | Luxembourgish     |               805 |       0.383 |    0.343 | 0.280 |     276 |   444 | 8297360 |    529 |
| 65 | jav               | Javanese          |               615 |       0.105 |    0.486 | 0.100 |     299 |  2542 | 8295452 |    316 |
| 66 | bos               | Bosnian           |               567 |       0.011 |    0.053 | 0.010 |      30 |  2722 | 8295320 |    537 |
| 67 | que               | Quechua           |               422 |       0.549 |    0.382 | 0.380 |     161 |   132 | 8298055 |    261 |
| 68 | fao               | Faroese           |               402 |       0.253 |    0.281 | 0.191 |     113 |   333 | 8297874 |    289 |
| 69 | ori               | Odia              |               374 |       1.000 |    0.992 | 0.996 |     371 |     0 | 8298235 |      3 |
| 70 | tam               | Tamil             |               334 |       0.988 |    1.000 | 0.988 |     334 |     4 | 8298271 |      0 |
| 71 | tel               | Telugu            |               254 |       0.996 |    1.000 | 0.996 |     254 |     1 | 8298354 |      0 |
| 72 | kir               | Kyrgyz            |               254 |       0.049 |    0.118 | 0.041 |      30 |   588 | 8297767 |    224 |
| 73 | xho               | Xhosa             |               252 |       0.110 |    0.575 | 0.106 |     145 |  1174 | 8297183 |    107 |
| 74 | lao               | Lao               |               219 |       0.952 |    1.000 | 0.952 |     219 |    11 | 8298379 |      0 |
| 75 | amh               | Amharic           |               211 |       0.770 |    1.000 | 0.770 |     211 |    63 | 8298335 |      0 |
| 76 | mlt               | Maltese           |               208 |       0.034 |    0.817 | 0.034 |     170 |  4791 | 8293610 |     38 |
| 77 | pan               | Punjabi           |               196 |       0.985 |    1.000 | 0.985 |     196 |     3 | 8298410 |      0 |
| 78 | sme               | Northern Sami     |               181 |       0.190 |    0.320 | 0.158 |      58 |   248 | 8298180 |    123 |
| 79 | kan               | Kannada           |               176 |       1.000 |    1.000 | 1.000 |     176 |     0 | 8298433 |      0 |
| 80 | guj               | Gujarati          |               168 |       0.966 |    1.000 | 0.966 |     168 |     6 | 8298435 |      0 |
| 81 | arg               | Aragonese         |               103 |       0.002 |    0.029 | 0.002 |       3 |  1529 | 8296977 |    100 |
| 82 | zul               | Zulu              |                77 |       0.054 |    0.286 | 0.051 |      22 |   383 | 8298149 |     55 |
| 83 | hat               | Haitian Creole    |                64 |       0.008 |    0.406 | 0.008 |      26 |  3176 | 8295369 |     38 |
| 84 | mlg               | Malagasy          |                59 |       0.017 |    0.559 | 0.017 |      33 |  1949 | 8296601 |     26 |
| 85 | wln               | Walloon           |                53 |       0.015 |    0.528 | 0.015 |      28 |  1847 | 8296709 |     25 |
| 86 | sin               | Sinhala           |                45 |       0.738 |    1.000 | 0.738 |      45 |    16 | 8298548 |      0 |
| 87 | pus               | Pashto            |                44 |       0.178 |    0.432 | 0.159 |      19 |    88 | 8298477 |     25 |
| 88 | kin               | Kinyarwanda       |                28 |       0.005 |    0.214 | 0.005 |       6 |  1135 | 8297446 |     22 |