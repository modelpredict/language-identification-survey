# Classification performance for gcld3 on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 8261834 (85.70%)
- **Aggregated accuracy: 0.8711048902701265**

<h2 id="supported-languages">Supported languages (107)</h2>

afr (Afrikaans), amh (Amharic), ara (Arabic), bul (Bulgarian), bul (Bulgarian), ben (Bangla), bos (Bosnian), cat (Catalan), ceb (Cebuano), cos (Corsican), ces (Czech), cym (Welsh), dan (Danish), deu (German), ell (Greek), ell (Greek), eng (English), epo (Esperanto), spa (Spanish), est (Estonian), eus (Basque), fas (Persian), fin (Finnish), fil (Filipino), fra (French), fry (Western Frisian), gle (Irish), gla (Scottish Gaelic), glg (Galician), guj (Gujarati), hau (Hausa), haw (Hawaiian), hin (Hindi), hin (Hindi), hmn (Hmong), hrv (Croatian), hat (Haitian Creole), hun (Hungarian), hye (Armenian), ind (Indonesian), ibo (Igbo), isl (Icelandic), ita (Italian), heb (Hebrew), jpn (Japanese), jpn (Japanese), jav (Javanese), kat (Georgian), kaz (Kazakh), khm (Khmer), kan (Kannada), kor (Korean), kur (Kurdish), kir (Kyrgyz), lat (Latin), ltz (Luxembourgish), lao (Lao), lit (Lithuanian), lav (Latvian), mlg (Malagasy), mri (Maori), mkd (Macedonian), mal (Malayalam), mon (Mongolian), mar (Marathi), msa (Malay), mlt (Maltese), mya (Burmese), nep (Nepali), nld (Dutch), nob (Norwegian Bokmål), nya (Nyanja), pan (Punjabi), pol (Polish), pus (Pashto), por (Portuguese), ron (Romanian), rus (Russian), rus (Russian), snd (Sindhi), sin (Sinhala), slk (Slovak), slv (Slovenian), smo (Samoan), sna (Shona), som (Somali), sqi (Albanian), srp (Serbian), sot (Southern Sotho), sun (Sundanese), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tgk (Tajik), tha (Thai), tur (Turkish), ukr (Ukrainian), urd (Urdu), uzb (Uzbek), vie (Vietnamese), xho (Xhosa), yid (Yiddish), yor (Yoruba), zho (Chinese), zho (Chinese), zul (Zulu)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |     fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|--------:|------:|--------:|-------:|
|  1 | eng               | English          |           1479733 |       0.995 |    0.851 | 0.915 | 1258584 |  6819 | 6775282 | 221149 |
|  2 | rus               | Russian          |            849653 |       0.974 |    0.858 | 0.902 |  729212 | 19236 | 7392945 | 120441 |
|  3 | ita               | Italian          |            787053 |       0.970 |    0.821 | 0.877 |  646316 | 20005 | 7454776 | 140737 |
|  4 | tur               | Turkish          |            709573 |       0.993 |    0.894 | 0.938 |  634612 |  4617 | 7547644 |  74961 |
|  5 | epo               | Esperanto        |            659632 |       0.963 |    0.922 | 0.925 |  608152 | 23690 | 7578512 |  51480 |
|  6 | deu               | German           |            553727 |       0.977 |    0.933 | 0.944 |  516822 | 12347 | 7695760 |  36905 |
|  7 | fra               | French           |            466192 |       0.973 |    0.860 | 0.902 |  400941 | 11073 | 7784569 |  65251 |
|  8 | por               | Portuguese       |            385737 |       0.910 |    0.885 | 0.859 |  341427 | 33858 | 7842239 |  44310 |
|  9 | spa               | Spanish          |            338781 |       0.908 |    0.782 | 0.806 |  264941 | 26864 | 7896189 |  73840 |
| 10 | hun               | Hungarian        |            323048 |       0.968 |    0.895 | 0.916 |  289189 |  9667 | 7929119 |  33859 |
| 11 | jpn               | Japanese         |            208761 |       0.978 |    0.999 | 0.977 |  208552 |  4759 | 8048314 |    209 |
| 12 | heb               | Hebrew           |            197226 |       0.998 |    0.991 | 0.993 |  195374 |   409 | 8064199 |   1852 |
| 13 | ukr               | Ukrainian        |            171674 |       0.800 |    0.889 | 0.762 |  152579 | 38095 | 8052065 |  19095 |
| 14 | nld               | Dutch            |            144340 |       0.876 |    0.854 | 0.814 |  123199 | 17516 | 8099978 |  21141 |
| 15 | fin               | Finnish          |            128011 |       0.941 |    0.902 | 0.895 |  115404 |  7235 | 8126588 |  12607 |
| 16 | pol               | Polish           |            109662 |       0.915 |    0.931 | 0.885 |  102084 |  9477 | 8142695 |   7578 |
| 17 | mkd               | Macedonian       |             77938 |       0.862 |    0.741 | 0.749 |   57730 |  9232 | 8174664 |  20208 |
| 18 | mar               | Marathi          |             64126 |       0.989 |    0.911 | 0.943 |   58406 |   654 | 8197054 |   5720 |
| 19 | lit               | Lithuanian       |             59659 |       0.841 |    0.883 | 0.797 |   52661 |  9950 | 8192225 |   6998 |
| 20 | ces               | Czech            |             57030 |       0.881 |    0.813 | 0.799 |   46341 |  6282 | 8198522 |  10689 |
| 21 | dan               | Danish           |             49399 |       0.652 |    0.746 | 0.587 |   36848 | 19626 | 8192809 |  12551 |
| 22 | srp               | Serbian          |             45176 |       0.317 |    0.449 | 0.265 |   20304 | 43763 | 8172895 |  24872 |
| 23 | swe               | Swedish          |             41677 |       0.786 |    0.861 | 0.739 |   35870 |  9753 | 8210404 |   5807 |
| 24 | lat               | Latin            |             39718 |       0.500 |    0.729 | 0.457 |   28963 | 28998 | 8193118 |  10755 |
| 25 | ara               | Arabic           |             35991 |       0.999 |    0.911 | 0.952 |   32774 |    32 | 8225811 |   3217 |
| 26 | ell               | Greek            |             34071 |       0.730 |    1.000 | 0.730 |   34062 | 12617 | 8215146 |      9 |
| 27 | ron               | Romanian         |             24943 |       0.592 |    0.808 | 0.553 |   20164 | 13920 | 8222971 |   4779 |
| 28 | bul               | Bulgarian        |             24503 |       0.318 |    0.844 | 0.309 |   20688 | 44456 | 8192875 |   3815 |
| 29 | vie               | Vietnamese       |             19234 |       0.883 |    0.981 | 0.876 |   18870 |  2495 | 8240105 |    364 |
| 30 | fil               | Filipino         |             16649 |       0.733 |    0.780 | 0.664 |   12994 |  4735 | 8240450 |   3655 |
| 31 | slk               | Slovak           |             14660 |       0.411 |    0.727 | 0.381 |   10664 | 15304 | 8231870 |   3996 |
| 32 | ind               | Indonesian       |             14542 |       0.642 |    0.640 | 0.544 |    9304 |  5180 | 8242112 |   5238 |
| 33 | hin               | Hindi            |             14230 |       0.508 |    0.880 | 0.491 |   12527 | 12125 | 8235479 |   1703 |
| 34 | nob               | Norwegian Bokmål |             14223 |       0.285 |    0.829 | 0.277 |   11791 | 29626 | 8217985 |   2432 |
| 35 | isl               | Icelandic        |             11091 |       0.523 |    0.945 | 0.515 |   10484 |  9560 | 8241183 |    607 |
| 36 | cat               | Catalan          |              7971 |       0.176 |    0.818 | 0.173 |    6520 | 30461 | 8223402 |   1451 |
| 37 | kor               | Korean           |              7570 |       0.915 |    0.996 | 0.913 |    7536 |   703 | 8253561 |     34 |
| 38 | yid               | Yiddish          |              6895 |       0.790 |    0.944 | 0.772 |    6512 |  1728 | 8253211 |    383 |
| 39 | eus               | Basque           |              6166 |       0.439 |    0.861 | 0.424 |    5306 |  6789 | 8248879 |    860 |
| 40 | kat               | Georgian         |              5732 |       1.000 |    0.998 | 0.999 |    5720 |     2 | 8256100 |     12 |
| 41 | hrv               | Croatian         |              5204 |       0.139 |    0.447 | 0.128 |    2324 | 14392 | 8242238 |   2880 |
| 42 | ben               | Bangla           |              4714 |       1.000 |    0.998 | 0.999 |    4704 |     0 | 8257120 |     10 |
| 43 | glg               | Galician         |              4613 |       0.064 |    0.774 | 0.063 |    3569 | 52237 | 8204984 |   1044 |
| 44 | afr               | Afrikaans        |              4031 |       0.145 |    0.865 | 0.143 |    3485 | 20607 | 8237196 |    546 |
| 45 | kaz               | Kazakh           |              3685 |       0.404 |    0.932 | 0.398 |    3434 |  5063 | 8253086 |    251 |
| 46 | est               | Estonian         |              3637 |       0.165 |    0.796 | 0.162 |    2894 | 14623 | 8243574 |    743 |
| 47 | tha               | Thai             |              3528 |       0.995 |    0.998 | 0.994 |    3522 |    18 | 8258288 |      6 |
| 48 | mon               | Mongolian        |              2757 |       0.415 |    0.955 | 0.411 |    2633 |  3712 | 8255365 |    124 |
| 49 | sqi               | Albanian         |              2526 |       0.288 |    0.865 | 0.282 |    2184 |  5395 | 8253913 |    342 |
| 50 | gle               | Irish            |              2389 |       0.175 |    0.911 | 0.174 |    2177 | 10238 | 8249207 |    212 |
| 51 | hye               | Armenian         |              2248 |       0.994 |    0.998 | 0.993 |    2243 |    13 | 8259573 |      5 |
| 52 | urd               | Urdu             |              2008 |       0.882 |    0.961 | 0.867 |    1930 |   258 | 8259568 |     78 |
| 53 | khm               | Khmer            |              1511 |       1.000 |    0.985 | 0.993 |    1489 |     0 | 8260323 |     22 |
| 54 | ceb               | Cebuano          |              1478 |       0.148 |    0.571 | 0.141 |     844 |  4846 | 8255510 |    634 |
| 55 | cym               | Welsh            |              1344 |       0.103 |    0.824 | 0.102 |    1108 |  9667 | 8250823 |    236 |
| 56 | slv               | Slovenian        |              1093 |       0.048 |    0.724 | 0.047 |     791 | 15714 | 8245027 |    302 |
| 57 | gla               | Scottish Gaelic  |              1033 |       0.090 |    0.867 | 0.089 |     896 |  9060 | 8251741 |    137 |
| 58 | uzb               | Uzbek            |               855 |       0.091 |    0.581 | 0.088 |     497 |  4957 | 8256022 |    358 |
| 59 | mal               | Malayalam        |               827 |       1.000 |    1.000 | 1.000 |     827 |     0 | 8261007 |      0 |
| 60 | ltz               | Luxembourgish    |               805 |       0.031 |    0.867 | 0.031 |     698 | 21519 | 8239510 |    107 |
| 61 | jav               | Javanese         |               615 |       0.030 |    0.361 | 0.029 |     222 |  7128 | 8254091 |    393 |
| 62 | bos               | Bosnian          |               567 |       0.012 |    0.388 | 0.011 |     220 | 18770 | 8242497 |    347 |
| 63 | mya               | Burmese          |               433 |       1.000 |    1.000 | 1.000 |     433 |     0 | 8261401 |      0 |
| 64 | mri               | Maori            |               388 |       0.040 |    0.711 | 0.040 |     276 |  6622 | 8254824 |    112 |
| 65 | fry               | Western Frisian  |               355 |       0.012 |    0.738 | 0.012 |     262 | 21054 | 8240425 |     93 |
| 66 | tam               | Tamil            |               334 |       1.000 |    1.000 | 1.000 |     334 |     0 | 8261500 |      0 |
| 67 | tel               | Telugu           |               254 |       1.000 |    1.000 | 1.000 |     254 |     0 | 8261580 |      0 |
| 68 | kir               | Kyrgyz           |               254 |       0.027 |    0.878 | 0.027 |     223 |  7974 | 8253606 |     31 |
| 69 | xho               | Xhosa            |               252 |       0.039 |    0.683 | 0.039 |     172 |  4230 | 8257352 |     80 |
| 70 | lao               | Lao              |               219 |       1.000 |    1.000 | 1.000 |     219 |     0 | 8261615 |      0 |
| 71 | amh               | Amharic          |               211 |       1.000 |    0.991 | 0.995 |     209 |     0 | 8261623 |      2 |
| 72 | mlt               | Maltese          |               208 |       0.013 |    0.817 | 0.013 |     170 | 12489 | 8249137 |     38 |
| 73 | pan               | Punjabi          |               196 |       1.000 |    0.995 | 0.997 |     195 |     0 | 8261638 |      1 |
| 74 | kan               | Kannada          |               176 |       1.000 |    1.000 | 1.000 |     176 |     0 | 8261658 |      0 |
| 75 | guj               | Gujarati         |               168 |       1.000 |    0.982 | 0.991 |     165 |     0 | 8261666 |      3 |
| 76 | haw               | Hawaiian         |               155 |       0.010 |    0.839 | 0.010 |     130 | 12567 | 8249112 |     25 |
| 77 | som               | Somali           |                80 |       0.019 |    0.912 | 0.019 |      73 |  3674 | 8258080 |      7 |
| 78 | zul               | Zulu             |                77 |       0.007 |    0.753 | 0.007 |      58 |  7839 | 8253918 |     19 |
| 79 | smo               | Samoan           |                76 |       0.008 |    0.763 | 0.008 |      58 |  7277 | 8254481 |     18 |
| 80 | hat               | Haitian Creole   |                64 |       0.004 |    0.797 | 0.004 |      51 | 13257 | 8248513 |     13 |
| 81 | tgk               | Tajik            |                63 |       0.008 |    0.889 | 0.008 |      56 |  7343 | 8254428 |      7 |
| 82 | hau               | Hausa            |                60 |       0.006 |    0.800 | 0.006 |      48 |  7835 | 8253939 |     12 |
| 83 | mlg               | Malagasy         |                59 |       0.003 |    0.831 | 0.003 |      49 | 14975 | 8246800 |     10 |
| 84 | sin               | Sinhala          |                45 |       1.000 |    1.000 | 1.000 |      45 |     0 | 8261789 |      0 |
| 85 | pus               | Pashto           |                44 |       0.098 |    0.864 | 0.097 |      38 |   350 | 8261440 |      6 |
| 86 | sna               | Shona            |                42 |       0.006 |    0.667 | 0.005 |      28 |  5062 | 8256730 |     14 |
| 87 | yor               | Yoruba           |                37 |       0.001 |    0.108 | 0.001 |       4 |  3799 | 8257998 |     33 |
| 88 | ibo               | Igbo             |                32 |       0.002 |    0.688 | 0.002 |      22 | 10813 | 8250989 |     10 |
| 89 | sun               | Sundanese        |                31 |       0.003 |    0.548 | 0.003 |      17 |  5505 | 8256298 |     14 |
| 90 | nya               | Nyanja           |                24 |       0.010 |    0.833 | 0.010 |      20 |  2072 | 8259738 |      4 |
| 91 | cos               | Corsican         |                24 |       0.000 |    0.583 | 0.000 |      14 | 35270 | 8226540 |     10 |
| 92 | snd               | Sindhi           |                 6 |       0.003 |    0.833 | 0.003 |       5 |  1440 | 8260388 |      1 |
| 93 | sot               | Southern Sotho   |                 2 |       0.001 |    1.000 | 0.001 |       2 |  3240 | 8258592 |      0 |