from django.shortcuts import render
'''ulkeler = {
kodu:["AD","AE","AF","AG","AI","AL","AM","AO","AQ","AR","AS","AT","AU","AW",
"AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BL","BM","BN","BO","BR",
"BS","BT","BV","BW","BY","BZ","CA","CC","CD","CF","CG","CH","CI","CK","CL",
"CM","CN","CO","CR","CU","CV","CW","CX","CY","CZ","DE","DJ","DK","DM","DO",
"DZ","EC","EE","EG","EH","ER","ES","ET","FI","FJ","FK","FM","FO","FR","FX",
"GA","GB","GD","GE","GF","GG","GH","GI","GL","GM","GN","GP","GQ","GR","GS",
"GT","GU","GW","GY","HK","HM","HN","HR","HT","HU","ID","IE","IL","IM","IN",
"IO","IQ","IR","IS","IT","JE","JM","JO","JP","KE","KG","KH","KI","KM","KN",
"KP","KR","KW","KY","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV",
"LY","MA","MC","MD","ME","MF","MG","MH","MK","ML","MM","MN","MO","MP","MQ",
"MR","MS","MT","MU","MV","MW","MX","MY","MZ","NA","NC","NE","NF","NG","NI",
"NL","NO","NP","NR","NU","NZ","OM","PA","PE","PF","PG","PH","PK","PL","PM",
"PN","PR","PS","PS","PT","PW","PY","QA","RE","RO","RS","RU","RW","SA","SB",
"SC","SD","SE","SG","SH","SI","SJ","SK","SL","SM","SN","SO","SR","SS","ST",
"SV","SX","SY","SZ","TC","TD","TF","TG","TH","TJ","TK","TL","TM","TN","TO",
"TR","TT","TV","TW","TZ","UA","UG","UM","US","UY","UZ","VA","VC","VE","VG",
"VI","VN","VU","WF","WS","XK","YE","YT","ZA","ZM","ZW"],}'''

ulkeler = ["Andorra","Birleşik Arap Emirlikleri","Afganistan","Antigua ve Barbuda",
"Anguilla","Arnavutluk","Ermenistan","Angola","Antarktika","Arjantin",
"Amerikan Samoası","Avusturya","Avustralya","Aruba","Azerbaycan","Bosna-Hersek",
"Barbados","Bangladeş","Belçika","Burkina Faso","Bulgaristan","Bahreyn","Burundi",
"Benin","Saint Barthelemy","Bermuda","Brunei","Bolivya","Brezilya","Bahamalar",
"Bhutan","Bouvet Adası","Botsvana","Beyaz Rusya","Belize","Kanada","Cocos (Keyling) Adaları",
"Demokratik Kongo Cumhuriyeti","Orta Afrika Cumhuriyeti","Kongo Cumhuriyeti","İsviçre",
"Fildişi Sahili","Cook Adaları","Şili","Kamerun","Çin","Kolombiya","Kosta Rika",
"Küba","Yeşil Burun Adaları","Curaçao","Christmas Adası","Kıbrıs","Çek Cumhuriyeti",
"Almanya","Cibuti","Danimarka","Dominika","Dominik Cumhuriyeti","Cezayir","Ekvador",
"Estonya","Mısır","Batı Sahra","Eritre","İspanya","Etiyopya","Finlandiya","Fiji",
"Falkland Adaları (Islas Malvinas)","Mikronezya Federal Devletleri","Faroe Adaları",
"Fransa","Metropolitan Fransa","Gabon","Birleşik Krallık","Grenada","Gürcistan",
"Fransız Guyanası","Guernsey","Gana","Cebelitarık","Grönland","Gambiya","Gine",
"Guadeloupe","Ekvator Ginesi","Yunanistan","Güney Georgia ve Güney Sandwich Adaları",
"Guatemala","Guam","Gine-Bissau","Guyana","Hong Kong","Heard Adası ve McDonald Adaları",
"Honduras","Hırvatistan","Haiti","Macaristan","Endonezya","İrlanda","İsrail","Man Adası",
"Hindistan","Britanya Hint Okyanusu Toprakları","Irak","İran","İzlanda","İtalya","Jersey",
"Jamaika","Ürdün","Japonya","Kenya","Kırgızistan","Kamboçya","Kiribati","Komorlar",
"Saint Kitts ve Nevis","Kuzey Kore","Güney Kore","Kuveyt","Cayman Adaları","Kazakistan",
"Laos","Lübnan","Saint Lucia","Lihtenştayn","Sri Lanka","Liberya","Lesotho","Litvanya",
"Lüksemburg","Letonya","Libya","Fas","Monako","Moldova","Karadağ","Saint Martin",
"Madagaskar","Marshall Adaları","Makedonya","Mali","Burma","Moğolistan","Makao",
"Kuzey Mariana Adaları","Martinique","Moritanya","Montserrat","Malta","Mauritius",
"Maldivler","Malavi","Meksika","Malezya","Mozambik","Namibya","Yeni Kaledonya","Nijer",
"Norfolk Adası","Nijerya","Nikaragua","Hollanda","Norveç","Nepal","Nauru","Niue","Yeni Zelanda",
"Umman","Panama","Peru""Fransız Polinezyası","Papua Yeni Gine","Filipinler","Pakistan",
"Polonya","Saint Pierre ve Miquelon","Pitcairn Adaları","Porto Riko","Gazze","Batı Şeria",
"Portekiz","Palau","Paraguay","Katar","Reunion","Romanya","Sırbistan","Rusya","Ruanda",
"Suudi Arabistan","Solomon Adaları","Seyşeller","Sudan","İsveç","Singapur",
"Saint Helena, Ascension ve Tristan da Cunha","Slovenya","Svalbard""Slovakya","Sierra Leone",
"San Marino","Senegal","Somali","Surinam","Güney Sudan","Sao Tome ve Principe","El Salvador",
"Saint Martin","Suriye","Svaziland","Turks ve Caicos Adaları","Çad","Fransız Güney ve Antarktik Toprakları",
"Togo","Tayland","Tacikistan","Tokelau","Doğu Timor","Türkmenistan","Tunus","Tonga",
"Türkiye","Trinidad ve Tobago","Tuvalu","Tayvan","Tanzanya","Ukrayna","Uganda",
"Amerika Birleşik Devletleri Küçük Dış Adaları","Birleşik Devletler","Uruguay","Özbekistan",
"Vatikan","Saint Vincent ve Grenadinler","Venezuela","Britanya Virjin Adaları","Virjin Adaları",
"Vietnam","Vanuatu","Wallis ve Futuna","Samoa","Kosova","Yemen","Mayotte","Güney Afrika","Zambiya","Zimbabve"]

iller = ["Adana","Adıyaman","Afyonkarahisar","Ağrı","Aksaray","Amasya",\
"Ankara","Antalya","Ardahan","Artvin","Aydın","Balıkesir","Bartın",\
"Batman","Bayburt","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa",\
"Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Düzce","Edirne",\
"Elazığ","Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane",\
"Hakkari","Hatay","Iğdır","Isparta","İstanbul","İzmir","Kahramanmaraş",\
"Karabük","Karaman","Kars","Kastamonu","Kayseri","Kırıkkale","Kırklareli",\
"Kırşehir","Kilis","Kocaeli","Konya","Kütahya","Malatya","Manisa","Mardin",\
"Mersin","Muğla","Muş","Nevşehir","Niğde","Ordu","Osmaniye","Rize","Sakarya",\
"Samsun","Siirt","Sinop","Sivas","Şanlıurfa","Şırnak","Tekirdağ","Tokat",\
"Trabzon","Tunceli","Uşak","Van","Yalova","Yozgat","Zonguldak"]

Adana = ["Aladağ","Ceyhan","Çukurova","Feke","İmamoğlu","Karaisalı",\
"Karataş","Kozan","Pozantı","Saimbeyli","Sarıçam","Seyhan",\
"Tufanbeyli","Yumurtalık","Yüreğir"]

Adıyaman = ["Besni","Çelikhan","Gerger","Gölbaşı","Kahta",\
"Samsat","Sincik","Tut"]

Afyonkarahisar = ["Başmakçı","Bayat","Bolvadin","Çay","Çobanlar",\
"Dazkırı","Dinar","Emirdağ","Evciler","Hocalar","İhsaniye","İscehisar",\
"Kızılören","Sandıklı","Sinanpaşa","Sultandağı","Şuhut"]

Ağrı = ["Diyadin","Doğubeyazıt","Eleşkirt","Hamur","Patnos","Taşlıçay","Tutak"]

Aksaray = ["Ağaçören","Eskil","Gülağaç","Güzelyurt","Ortaköy","Sarıyahşi"]

Amasya = ["Göynücek","Gümüşhacıköy","Hamamözü","Merzifon","Suluova","Taşova"]

Ankara = ["Akyurt","Altındağ","Ayaş","Bala","Beypazarı","Çamlıdere",\
"Çankaya","Çubuk","Elmadağ","Etimesgut","Evren","Gölbaşı","Güdül",\
"Haymana","Kalecik","Kazan","Keçiören","Kızılcahamam","Mamak","Nallıhan",\
"Polatlı","Pursaklar","Sincan","Şereflikoçhisar","Yenimahalle"]

Antalya = ["Akseki","Aksu","Alanya","Döşemealtı","Elmalı","Finike",\
"Gazipaşa","Gündoğmuş","İbradi","Kale","Kaş","Kemer","Kepez","Konyaaltı",\
"Korkuteli","Kumluca","Manavgat","Muratpaşa","Serik"]

Ardahan = ["Çıldır","Damal","Göle","Hanak","Posof"]

Artvin = ["Ardanuç","Arhavi","Borçka","Hopa","Murgul","Şavşat","Yusufeli"]

Aydın = ["Bozdoğan","Buharkent","Çine","Didim","Germencik","İncirliova",\
"Karacasu","Karpuzlu","Koçarlı","Köşk","Kuşadası","Kuyucak","Nazilli",\
"Söke","Sultanhisar","Yenipazar"]

Balıkesir = ["Ayvalık","Balya","Bandırma","Bigadiç","Burhaniye","Dursunbey",\
"Edremit","Erdek","Gömeç","Gönen","Havran","İvrindi","Kepsut","Manyas",\
"Marmara","Savaştepe","Sındırgı","Susurluk"]

Bartın = ["Amasra","Kurucaşile","Ulus"]

Batman = ["Beşiri","Gercüş","Hasankeyf","Kozluk","Sason"]

Bayburt = ["Aydıntepe","Demirözü"]

Bilecik = ["Bozüyük","Gölpazarı","İnhisar","Osmaneli","Pazaryeri","Söğüt","Yenipazar"]

Bingöl = ["Adaklı","Genç","Karlıova","Kiğı","Solhan","Yayladere","Yedisu"]

Bitlis = ["Adilcevaz","Ahlat","Güroymak","Hizan","Mutki","Tatvan"]

Bolu = ["Dörtdivan","Gerede","Göynük","Kıbrıscık","Mengen","Mudurnu","Seben","Yeniçağa"]

Burdur = ["Ağlasun","Altınyayla","Bucak","Çavdır","Çeltikçi","Gölhisar",\
"Karamanlı","Kemer","Tefenni","Yeşilova"]

Bursa = ["Büyükorhan","Gemlik","Gürsu","Harmancık","İnegöl","İznik",\
"Karacabey","Keles","Kestel","Mudanya","Mustafakemalpaşa","Nilüfer",\
"Orhaneli","Orhangazi","Osmangazi""Yenişehir","Yıldırım"]

Çanakkale = ["Ayvacık","Bayramiç","Biga","Bozcaada","Çan","Eceabat",\
"Ezine","Gelibolu","Gökçeada","Lapseki","Yenice"]

Çankırı = ["Atkaracalar","Bayramören","Çerkeş","Eldivan","Ilgaz"\
"Kızılırmak","Korgun","Kurşunlu","Orta","Şabanözü","Yapraklı"]

Çorum = ["Alaca","Bayat","Boğazkale","Dodurga","İskilip","Kargı","Laçin",\
"Mecitözü","Oğuzlar","Ortaköy","Osmancık","Sungurlu","Uğurludağ"]

Denizli = ["Acıpayam","Akköy","Babadağ","Baklan","Bekilli","Beyağaç","Bozkurt",\
"Buldan","Çal","Çameli","Çardak","Çivril","Güney","Honaz","Kale","Sarayköy",\
"Serinhisar","Tavas"]

Diyarbakır = ["Bağlar","Bismil","Çermik","Çınar","Çüngüş","Dicle","Eğil","Ergani",\
"Hani","Hazro","Kayapınar","Kocaköy","Kulp","Lice","Silvan","Sur","Yenişehir"]

Düzce = ["Akçakoca","Cumayeri","Çilimli","Gölyaka","Gümüşova","Kaynaşlı","Yığılca"]

Edirne = ["Enez","Havsa","İpsala","Keşan","Lalapaşa","Meriç","Süloğlu","Uzunköprü"]

Elazığ = ["Ağın","Alacakaya","Arıcak","Baskil","Karakoçan","Keban","Kovancılar",\
"Maden","Palu","Sivrice"]

Erzincan = ["Çayırlı","İliç","Kemah","Kemaliye","Otlukbeli","Refahiye","Tercan","Üzümlü"]

Erzurum = ["Aşkale","Aziziye","Çat","Hınıs","Horasan","İspir","Karaçoban",\
"Karayazı","Köprüköy","Narman","Oltu","Olur","Palandöken","Pasinler",\
"Pazaryolu","Şenkaya","Tekman","Tortum","Uzundere","Yakutiye"]

Eskişehir = ["Alpu","Beylikova","Çifteler","Günyüzü","Han","İnönü","Mahmudiye",\
"Mihalgazi","Mihalıççık","Odunpazarı","Sarıcakaya","Seyitgazi","Sivrihisar","Tepebaşı"]

Gaziantep = ["Araban","İslahiye","Karkamış","Nizip","Nurdağı","Oğuzeli",\
"Şahinbey","Şehitkamil","Yavuzeli"]

Giresun = ["Alucra","Bulancak","Çamoluk","Çanakçı","Dereli","Doğankent",\
"Espiye","Eynesil","Görele","Güce","Keşap","Piraziz","Şebinkarahisar",\
"Tirebolu","Yağlıdere"]

Gümüşhane = ["Kelkit","Köse","Kürtün","Şiran","Torul"]

Hakkâri = ["Çukurca","Şemdinli","Yüksekova"]

Hatay = ["Altınözü","Antakya","Belen","Dörtyol","Erzin","Hassa","İskenderun",\
"Kırıkhan","Kumlu","Reyhanlı","Samandağ","Yayladağı"]

Iğdır = ["Aralık","Karakoyunlu","Tuzluca"]

Isparta = ["Aksu","Atabey","Eğirdir","Gelendost","Gönen","Keçiborlu",\
"Senirkent","Sütçüler","Şarkikaraağaç","Uluborlu","Yalvaç","Yenişarbademli"]

İstanbul = ["Adalar","Arnavutköy","Ataşehir","Avcılar","Bağcılar","Bahçelievler",\
"Bakırköy","Başakşehir","Bayrampaşa","Beşiktaş","Beykoz","Beylikdüzü",\
"Beyoğlu","Büyükçekmece","Çatalca","Çekmeköy","Esenler","Esenyurt","Eyüp",\
"Fatih","Gaziosmanpaşa","Güngören","Kadıköy","Kağıthane","Kartal","Küçükçekmece",\
"Maltepe","Pendik","Sancaktepe","Sarıyer","Silivri","Sultanbeyli","Sultangazi",\
"Şile","Şişli","Tuzla","Ümraniye","Üsküdar","Zeytinburnu"]

İzmir = ["Aliağa","Balçova","Bayındır","Bayraklı","Bergama","Beydağ","Bornova",\
"Buca","Çeşme","Çiğli","Dikili","Foça","Gaziemir","Güzelbahçe","Karabağlar",\
"Karaburun","Karşıyaka","Kemalpaşa","Kınık","Kiraz","Konak","Menderes",\
"Menemen","Narlıdere","Ödemiş","Seferihisar","Selçuk","Tire","Torbalı","Urla"]

Kahramanmaraş = ["Afşin","Andırın","Çağlayancerit","Ekinözü","Elbistan","Göksun",\
"Nurhak","Pazarcık","Türkoğlu"]

Karabük = ["Eflani","Eskipazar","Ovacık","Safranbolu","Yenice"]

Karaman = ["Ayrancı","Başyayla","Ermenek","Kazımkarabekir","Sarıveliler"]

Kars = ["Akyaka","Arpaçay","Digor","Kağızman","Sarıkamış","Selim","Susuz"]

Kastamonu = ["Abana","Ağlı","Araç","Azdavay","Bozkurt","Cide","Çatalzeytin",\
"Daday","Devrekani","Doğanyurt","Hanönü","İhsangazi","İnebolu","Küre","Pınarbaşı",\
"Seydiler","Şenpazar","Taşköprü","Tosya"]

Kayseri = ["Akkışla","Bünyan","Develi","Felahiye","Hacılar","İncesu","Kocasinan",\
"Melikgazi","Özvatan","Pınarbaşı","Sarıoğlan","Sarız","Talas","Tomarza","Yahyalı","Yeşilhisar"]

Kırıkkale = ["Bahşılı","Balışeyh","Çelebi","Delice","Karakeçili","Keskin",\
"Sulakyurt","Yahşihan"]

Kırklareli = ["Babaeski","Demirköy","Kofçaz","Lüleburgaz","Pehlivanköy",\
"Pınarhisar","Vize"]

Kırşehir = ["Akçakent","Akpınar","Boztepe","Çiçekdağı","Kaman","Mucur"]

Kilis = ["Elbeyli","Musabeyli","Polateli"]

Kocaeli = ["Başiskele","Çayırova","Darıca","Derince","Dilovası","Gebze",\
"Gölcük","İzmit","Kandıra","Karamürsel","Kartepe","Körfez"]

Konya = ["Ahırlı","Akören","Akşehir","Altınekin","Beyşehir","Bozkır",\
"Cihanbeyli","Çeltik","Çumra","Derbent","Derebucak","Doğanhisar","Emirgazi",
"Ereğli","Güneysınır","Hadım","Halkapınar","Hüyük","Ilgın","Kadınhanı",
"Karapınar","Karatay","Kulu","Meram","Sarayönü","Selçuklu","Seydişehir",
"Taşkent","Tuzlukçu","Yalıhüyük","Yeniceoba","Yunak"]

Kütahya = ["Altıntaş","Aslanapa","Çavdarhisar","Domaniç","Dumlupınar","Emet","Gediz",\
"Hisarcık","Pazarlar","Şaphane","Simav","Tavşanlı"]

Malatya = ["Akçadağ","Arapgir","Arguvan","Battalgazi","Darende","Doğanşehir",
"Doğanyol","Hekimhan","Kale","Kuluncak","Pütürge","Yazıhan","Yeşilyurt","Gürün"]

Manisa = ["Ahmetli","Akhisar","Alaşehir","Demirci","Gölmarmara","Gördes",\
"Kırkağaç","Köprübaşı","Kula","Salihli","Sarıgöl","Saruhanlı","Selendi",\
"Soma","Turgutlu"]

Mardin = ["Dargeçit","Derik","Kızıltepe","Mazıdağı","Midyat","Nusaybin",\
"Ömerli","Savur","Yeşilli"]

Mersin = ["Akdeniz","Anamur","Aydıncık","Bozyazı","Çamlıyayla","Erdemli",\
"Gülnar","Mezitli","Mut","Silifke","Tarsus","Toroslar","Yenişehir"]

Muğla = ["Bodrum","Dalaman","Datça","Fethiye","Kavaklıdere","Köyceğiz",
"Marmaris","Milas","Ortaca","Ula","Yatağan"]

Muş = ["Bulanık","Hasköy","Korkut","Malazgirt","Varto"]

Nevşehir = ["Acıgöl","Avanos","Derinkuyu","Gülşehir","Hacıbektaş",\
"Kozaklı","Ürgüp"]

Niğde = ["Altunhisar","Bor","Çamardı","Çiftlik","Ulukışla"]

Ordu = ["Akkuş","Aybastı","Çamaş","Çatalpınar","Çaybaşı","Fatsa","Gölköy",\
"Gülyalı","Gürgentepe","İkizce","Kabadüz","Kabataş","Korgan","Kumru","Mesudiye",\
"Perşembe","Ulubey","Ünye"]

Osmaniye = ["Bahçe","Düziçi","Hasanbeyli","Kadirli","Sumbas","Toprakkale"]

Rize = ["Ardeşen","Çamlıhemşin","Çayeli","Derepazarı","Fındıklı","Güneysu",\
"Hemşin","İkizdere","İyidere","Kalkandere","Pazar"]

Sakarya = ["Adapazarı","Akyazı","Arifiye","Erenler","Ferizli","Geyve",\
"Hendek","Karapürçek","Karasu","Kaynarca","Kocaali","Pamukova","Sapanca",\
"Serdivan","Söğütlü","Taraklı"]

Samsun = ["Alaçam","Asarcık","Atakum","Ayvacık","Bafra","Canik","Çarşamba",\
"Havza","İlkadım","Kavak","Ladik","Ondokuzmayıs","Salıpazarı","Tekkeköy",\
"Terme","Vezirköprü","Yakakent"]

Siirt = ["Aydınlar","Baykan","Eruh","Kurtalan","Pervari","Şirvan"]

Sinop = ["Ayancık","Boyabat","Dikmen","Durağan","Erfelek","Gerze",\
"Saraydüzü","Türkeli"]

Sivas = ["Akıncılar","Altınyayla","Divriği","Doğanşar","Gemerek","Gölova",\
"Hafik","İmranlı","Kangal","Koyulhisar","Suşehri","Şarkışla","Ulaş",\
"Yıldızeli","Zara","Gürün"]

Şanlıurfa = ["Akçakale","Birecik","Bozova","Ceylanpınar","Halfeti","Harran",\
"Hilvan","Siverek","Suruç","Viranşehir"]

Şırnak = ["Beytüşşebap","Cizre","Güçlükonak","İdil","Silopi","Uludere"]

Tekirdağ = ["Çerkezköy","Çorlu","Hayrabolu","Malkara","Marmara Ereğlisi",\
"Muratlı","Saray","Şarköy"]

Tokat = ["Almus","Artova","Başçiftlik","Erbaa","Niksar","Pazar","Reşadiye",\
"Sulusaray","Turhal","Yeşilyurt","Zile"]

Trabzon = ["Akçaabat","Araklı","Arsin","Beşikdüzü","Çarşıbaşı","Çaykara",\
"Dernekpazarı","Düzköy","Hayrat","Köprübaşı","Maçka","Of","Sürmene","Şalpazarı",\
"Tonya","Trabzon","Vakfıkebir","Yomra"]

Tunceli = ["Çemişgezek","Hozat","Mazgirt","Nazimiye","Ovacık","Pertek","Pülümür"]

Uşak = ["Banaz","Eşme","Karahallı","Sivaslı","Ulubey"]

Van = ["Bahçesaray","Başkale","Çaldıran","Çatak""Edremit","Erciş","Gevaş",\
"Gürpınar","Muradiye","Özalp","Saray"]

Yalova = ["Altınova","Armutlu","Çınarcık","Çiftlikköy","Termal"]

Yozgat = ["Akdağmadeni","Aydıncık","Boğazlıyan","Çandır","Çayıralan","Çekerek",
"Kadışehri","Saraykent","Sarıkaya","Sorgun","Şefaatli","Yenifakılı","Yerköy"]

Zonguldak = ["Alaplı","Çaycuma","Devrek","Gökçebey","Kilimli","Kozlu","Karadeniz Ereğli"]