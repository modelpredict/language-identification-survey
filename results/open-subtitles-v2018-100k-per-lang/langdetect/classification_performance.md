# Classification performance for langdetect on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 4236418 (100.00%)
- **Aggregated accuracy: 0.794824542809515**

<h2 id="supported-languages">Supported languages (55)</h2>

afr (Afrikaans), ara (Arabic), bul (Bulgarian), ben (Bangla), cat (Catalan), ces (Czech), cym (Welsh), dan (Danish), deu (German), ell (Greek), eng (English), spa (Spanish), est (Estonian), fas (Persian), fin (Finnish), fra (French), guj (Gujarati), heb (Hebrew), hin (Hindi), hrv (Croatian), hun (Hungarian), ind (Indonesian), ita (Italian), jpn (Japanese), kan (Kannada), kor (Korean), lit (Lithuanian), lav (Latvian), mkd (Macedonian), mal (Malayalam), mar (Marathi), nep (Nepali), nld (Dutch), nob (Norwegian Bokmål), pan (Punjabi), pol (Polish), por (Portuguese), ron (Romanian), rus (Russian), slk (Slovak), slv (Slovenian), som (Somali), sqi (Albanian), swe (Swedish), swa (Swahili), tam (Tamil), tel (Telugu), tha (Thai), fil (Filipino), tur (Turkish), ukr (Ukrainian), urd (Urdu), vie (Vietnamese), zho (Chinese), zho (Chinese)

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language         |   sentences_count |   precision |   recall |    f1 |    tp |    fp |      tn |    fn |
|---:|:------------------|:-----------------|------------------:|------------:|---------:|------:|------:|------:|--------:|------:|
|  1 | ell               | Greek            |            100000 |       1.000 |    0.996 | 0.998 | 99615 |     0 | 4136418 |   385 |
|  2 | swe               | Swedish          |            100000 |       0.853 |    0.734 | 0.739 | 73427 | 12668 | 4123750 | 26573 |
|  3 | mkd               | Macedonian       |            100000 |       0.732 |    0.831 | 0.682 | 83087 | 30346 | 4106072 | 16913 |
|  4 | tha               | Thai             |            100000 |       1.000 |    0.959 | 0.979 | 95853 |     0 | 4136418 |  4147 |
|  5 | cat               | Catalan          |            100000 |       0.790 |    0.649 | 0.651 | 64878 | 17269 | 4119149 | 35122 |
|  6 | bul               | Bulgarian        |            100000 |       0.718 |    0.694 | 0.620 | 69446 | 27311 | 4109107 | 30554 |
|  7 | fin               | Finnish          |            100000 |       0.828 |    0.883 | 0.785 | 88258 | 18356 | 4118062 | 11742 |
|  8 | dan               | Danish           |            100000 |       0.681 |    0.589 | 0.550 | 58899 | 27614 | 4108804 | 41101 |
|  9 | hun               | Hungarian        |            100000 |       0.915 |    0.823 | 0.833 | 82309 |  7622 | 4128796 | 17691 |
| 10 | kor               | Korean           |            100000 |       0.774 |    0.962 | 0.763 | 96150 | 28018 | 4108400 |  3850 |
| 11 | spa               | Spanish          |            100000 |       0.791 |    0.707 | 0.680 | 70674 | 18621 | 4117797 | 29326 |
| 12 | zho               | Chinese          |            100000 |       0.983 |    0.593 | 0.734 | 59251 |  1047 | 4135371 | 40749 |
| 13 | slk               | Slovak           |            100000 |       0.766 |    0.628 | 0.624 | 62796 | 19226 | 4117192 | 37204 |
| 14 | ron               | Romanian         |            100000 |       0.862 |    0.774 | 0.766 | 77434 | 12373 | 4124045 | 22566 |
| 15 | ind               | Indonesian       |            100000 |       0.705 |    0.783 | 0.643 | 78346 | 32709 | 4103709 | 21654 |
| 16 | est               | Estonian         |            100000 |       0.814 |    0.777 | 0.729 | 77744 | 17757 | 4118661 | 22256 |
| 17 | por               | Portuguese       |            100000 |       0.676 |    0.751 | 0.608 | 75080 | 35971 | 4100447 | 24920 |
| 18 | hrv               | Croatian         |            100000 |       0.670 |    0.652 | 0.568 | 65173 | 32078 | 4104340 | 34827 |
| 19 | heb               | Hebrew           |            100000 |       1.000 |    0.990 | 0.995 | 98997 |     0 | 4136418 |  1003 |
| 20 | ita               | Italian          |            100000 |       0.734 |    0.780 | 0.666 | 78012 | 28203 | 4108215 | 21988 |
| 21 | slv               | Slovenian        |            100000 |       0.657 |    0.653 | 0.559 | 65297 | 34095 | 4102323 | 34703 |
| 22 | ces               | Czech            |            100000 |       0.825 |    0.706 | 0.704 | 70563 | 14998 | 4121420 | 29437 |
| 23 | mal               | Malayalam        |            100000 |       1.000 |    0.976 | 0.988 | 97615 |     0 | 4136418 |  2385 |
| 24 | lit               | Lithuanian       |            100000 |       0.873 |    0.770 | 0.772 | 77002 | 11212 | 4125206 | 22998 |
| 25 | ukr               | Ukrainian        |            100000 |       0.851 |    0.545 | 0.628 | 54530 |  9511 | 4126907 | 45470 |
| 26 | pol               | Polish           |            100000 |       0.902 |    0.867 | 0.844 | 86670 |  9390 | 4127028 | 13330 |
| 27 | fas               | Persian          |            100000 |       0.959 |    0.829 | 0.872 | 82872 |  3550 | 4132868 | 17128 |
| 28 | jpn               | Japanese         |            100000 |       0.999 |    0.944 | 0.971 | 94447 |    59 | 4136359 |  5553 |
| 29 | hin               | Hindi            |            100000 |       1.000 |    0.819 | 0.901 | 81904 |     0 | 4136418 | 18096 |
| 30 | eng               | English          |            100000 |       0.593 |    0.749 | 0.539 | 74888 | 51451 | 4084967 | 25112 |
| 31 | sqi               | Albanian         |            100000 |       0.932 |    0.808 | 0.839 | 80757 |  5914 | 4130504 | 19243 |
| 32 | rus               | Russian          |            100000 |       0.648 |    0.793 | 0.597 | 79285 | 43117 | 4093301 | 20715 |
| 33 | fra               | French           |            100000 |       0.757 |    0.776 | 0.682 | 77581 | 24894 | 4111524 | 22419 |
| 34 | lav               | Latvian          |            100000 |       0.920 |    0.811 | 0.831 | 81127 |  7057 | 4129361 | 18873 |
| 35 | deu               | German           |            100000 |       0.670 |    0.841 | 0.630 | 84127 | 41422 | 4094996 | 15873 |
| 36 | tur               | Turkish          |            100000 |       0.895 |    0.851 | 0.829 | 85053 | 10012 | 4126406 | 14947 |
| 37 | ara               | Arabic           |            100000 |       0.895 |    0.936 | 0.868 | 93567 | 11010 | 4125408 |  6433 |
| 38 | vie               | Vietnamese       |            100000 |       0.927 |    0.917 | 0.890 | 91653 |  7171 | 4129247 |  8347 |
| 39 | nob               | Norwegian Bokmål |            100000 |       0.635 |    0.647 | 0.541 | 64662 | 37243 | 4099175 | 35338 |
| 40 | ben               | Bangla           |            100000 |       1.000 |    0.971 | 0.985 | 97127 |     0 | 4136418 |  2873 |
| 41 | nld               | Dutch            |            100000 |       0.774 |    0.687 | 0.658 | 68682 | 20042 | 4116376 | 31318 |
| 42 | urd               | Urdu             |             46523 |       0.880 |    0.884 | 0.832 | 41104 |  5590 | 4184305 |  5419 |
| 43 | tam               | Tamil            |             40165 |       1.000 |    0.952 | 0.975 | 38236 |     2 | 4196251 |  1929 |
| 44 | tel               | Telugu           |             30416 |       1.000 |    0.941 | 0.970 | 28630 |     0 | 4206002 |  1786 |
| 45 | fil               | Filipino         |             19314 |       0.378 |    0.746 | 0.356 | 14401 | 23647 | 4193457 |  4913 |