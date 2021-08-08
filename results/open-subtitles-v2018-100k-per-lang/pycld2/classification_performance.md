# Classification performance for pycld2 on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 4236418 (100.00%)
- **Aggregated accuracy: 0.6840554921634268**

<h2 id="supported-languages">Supported languages (83)</h2>

afr (Afrikaans), sqi (Albanian), ara (Arabic), hye (Armenian), aze (Azerbaijani), eus (Basque), bel (Belarusian), ben (Bangla), bih (Bihari languages), bul (Bulgarian), cat (Catalan), ceb (Cebuano), chr (Cherokee), hrv (Croatian), ces (Czech), zho (Chinese), dan (Danish), div (Divehi), nld (Dutch), eng (English), est (Estonian), fin (Finnish), fra (French), glg (Galician), lug (Ganda), kat (Georgian), deu (German), ell (Greek), guj (Gujarati), hat (Haitian Creole), heb (Hebrew), hin (Hindi), hmn (Hmong), hun (Hungarian), isl (Icelandic), ind (Indonesian), iku (Inuktitut), gle (Irish), ita (Italian), jav (Javanese), jpn (Japanese), kan (Kannada), khm (Khmer), kin (Kinyarwanda), kor (Korean), lao (Lao), lav (Latvian), lif (Limbu), lit (Lithuanian), mkd (Macedonian), msa (Malay), mal (Malayalam), mlt (Maltese), mar (Marathi), nep (Nepali), nob (Norwegian Bokmål), ori (Odia), fas (Persian), pol (Polish), por (Portuguese), pan (Punjabi), ron (Romanian), rus (Russian), gla (Scottish Gaelic), srp (Serbian), sin (Sinhala), slk (Slovak), slv (Slovenian), spa (Spanish), swa (Swahili), swe (Swedish), syr (Syriac), fil (Filipino), tam (Tamil), tel (Telugu), tha (Thai), tur (Turkish), ukr (Ukrainian), urd (Urdu), vie (Vietnamese), cym (Welsh), yid (Yiddish), zho (Chinese)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |    tp |    fp |      tn |    fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|------:|------:|--------:|------:|
|  1 | ell               | Greek            |            100000 |       1.000 |    0.997 | 0.998 | 99664 |    26 | 4136392 |   336 |
|  2 | swe               | Swedish          |            100000 |       0.995 |    0.632 | 0.771 | 63168 |   297 | 4136121 | 36832 |
|  3 | mkd               | Macedonian       |            100000 |       0.973 |    0.452 | 0.612 | 45227 |  1246 | 4135172 | 54773 |
|  4 | tha               | Thai             |            100000 |       1.000 |    0.961 | 0.980 | 96100 |     0 | 4136418 |  3900 |
|  5 | cat               | Catalan          |            100000 |       0.991 |    0.484 | 0.648 | 48417 |   464 | 4135954 | 51583 |
|  6 | bul               | Bulgarian        |            100000 |       0.969 |    0.570 | 0.710 | 57021 |  1805 | 4134613 | 42979 |
|  7 | fin               | Finnish          |            100000 |       0.996 |    0.747 | 0.852 | 74729 |   300 | 4136118 | 25271 |
|  8 | dan               | Danish           |            100000 |       0.873 |    0.573 | 0.659 | 57328 |  8331 | 4128087 | 42672 |
|  9 | hun               | Hungarian        |            100000 |       0.999 |    0.764 | 0.865 | 76416 |   109 | 4136309 | 23584 |
| 10 | kor               | Korean           |            100000 |       1.000 |    0.891 | 0.942 | 89101 |     0 | 4136418 | 10899 |
| 11 | spa               | Spanish          |            100000 |       0.971 |    0.648 | 0.769 | 64824 |  1918 | 4134500 | 35176 |
| 12 | zho               | Chinese          |            100000 |       0.999 |    0.684 | 0.812 | 68435 |    35 | 4136383 | 31565 |
| 13 | slk               | Slovak           |            100000 |       0.904 |    0.658 | 0.732 | 65838 |  7024 | 4129394 | 34162 |
| 14 | ron               | Romanian         |            100000 |       0.995 |    0.666 | 0.796 | 66604 |   367 | 4136051 | 33396 |
| 15 | ind               | Indonesian       |            100000 |       0.970 |    0.626 | 0.752 | 62612 |  1912 | 4134506 | 37388 |
| 16 | est               | Estonian         |            100000 |       0.993 |    0.668 | 0.797 | 66835 |   448 | 4135970 | 33165 |
| 17 | por               | Portuguese       |            100000 |       0.938 |    0.667 | 0.760 | 66656 |  4394 | 4132024 | 33344 |
| 18 | hrv               | Croatian         |            100000 |       0.968 |    0.468 | 0.625 | 46827 |  1560 | 4134858 | 53173 |
| 19 | heb               | Hebrew           |            100000 |       1.000 |    0.619 | 0.765 | 61882 |     1 | 4136417 | 38118 |
| 20 | ita               | Italian          |            100000 |       0.992 |    0.504 | 0.667 | 50426 |   396 | 4136022 | 49574 |
| 21 | slv               | Slovenian        |            100000 |       0.991 |    0.444 | 0.612 | 44391 |   384 | 4136034 | 55609 |
| 22 | ces               | Czech            |            100000 |       0.895 |    0.716 | 0.760 | 71587 |  8361 | 4128057 | 28413 |
| 23 | mal               | Malayalam        |            100000 |       1.000 |    0.977 | 0.988 | 97651 |     0 | 4136418 |  2349 |
| 24 | lit               | Lithuanian       |            100000 |       0.995 |    0.659 | 0.791 | 65892 |   340 | 4136078 | 34108 |
| 25 | ukr               | Ukrainian        |            100000 |       0.989 |    0.456 | 0.622 | 45595 |   484 | 4135934 | 54405 |
| 26 | pol               | Polish           |            100000 |       0.997 |    0.729 | 0.841 | 72937 |   221 | 4136197 | 27063 |
| 27 | fas               | Persian          |            100000 |       0.998 |    0.604 | 0.752 | 60362 |   119 | 4136299 | 39638 |
| 28 | jpn               | Japanese         |            100000 |       0.988 |    0.911 | 0.942 | 91104 |  1114 | 4135304 |  8896 |
| 29 | hin               | Hindi            |            100000 |       1.000 |    0.847 | 0.917 | 84721 |     0 | 4136418 | 15279 |
| 30 | eng               | English          |            100000 |       0.620 |    0.744 | 0.560 | 74428 | 45610 | 4090808 | 25572 |
| 31 | sqi               | Albanian         |            100000 |       0.999 |    0.708 | 0.828 | 70830 |    97 | 4136321 | 29170 |
| 32 | rus               | Russian          |            100000 |       0.821 |    0.638 | 0.666 | 63789 | 13928 | 4122490 | 36211 |
| 33 | fra               | French           |            100000 |       0.990 |    0.644 | 0.777 | 64405 |   654 | 4135764 | 35595 |
| 34 | lav               | Latvian          |            100000 |       0.995 |    0.674 | 0.802 | 67436 |   321 | 4136097 | 32564 |
| 35 | deu               | German           |            100000 |       0.991 |    0.733 | 0.840 | 73344 |   634 | 4135784 | 26656 |
| 36 | tur               | Turkish          |            100000 |       0.999 |    0.747 | 0.854 | 74678 |    92 | 4136326 | 25322 |
| 37 | ara               | Arabic           |            100000 |       0.986 |    0.653 | 0.781 | 65309 |   935 | 4135483 | 34691 |
| 38 | vie               | Vietnamese       |            100000 |       0.999 |    0.773 | 0.871 | 77288 |    59 | 4136359 | 22712 |
| 39 | nob               | Norwegian Bokmål |            100000 |       0.802 |    0.634 | 0.652 | 63433 | 15634 | 4120784 | 36567 |
| 40 | ben               | Bangla           |            100000 |       1.000 |    0.639 | 0.780 | 63868 |     0 | 4136418 | 36132 |
| 41 | nld               | Dutch            |            100000 |       0.996 |    0.676 | 0.804 | 67614 |   251 | 4136167 | 32386 |
| 42 | urd               | Urdu             |             46523 |       0.998 |    0.677 | 0.806 | 31508 |    57 | 4189838 | 15015 |
| 43 | tam               | Tamil            |             40165 |       1.000 |    0.954 | 0.976 | 38307 |     2 | 4196251 |  1858 |
| 44 | tel               | Telugu           |             30416 |       1.000 |    0.945 | 0.972 | 28732 |     0 | 4206002 |  1684 |
| 45 | fil               | Filipino         |             19314 |       0.996 |    0.550 | 0.708 | 10626 |    43 | 4217061 |  8688 |