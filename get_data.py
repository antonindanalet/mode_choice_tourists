import pandas as pd
import pyreadstat
from pathlib import Path


def get_data():
    path_to_folder = Path('C:\\Users\\u239412\\Documents\\Tourismusverkehr\\data\\TMS\\')
    df, meta = pyreadstat.read_sav(path_to_folder / '26_TMS_final SBB_Datenlieferung_Februar2023.sav')
    tot_nb_obs = len(df)
    # print(meta.variable_value_labels)
    # {'Q48': {1.0: '16 ? 20',
    #          2.0: '21 ? 25',
    #          3.0: '26 ? 30',
    #          4.0: '31 ? 35',
    #          5.0: '36 ? 40',
    #          6.0: '41 ? 45',
    #          7.0: '46 ? 50',
    #          8.0: '51 ? 55',
    #          9.0: '56 ? 60',
    #          10.0: '61 ? 65',
    #          11.0: '66 ? 70',
    #          12.0: '71 ? 75',
    #          13.0: '76 ? 80',
    #          14.0: '81 ? 85',
    #          15.0: '86 ? 90',
    #          16.0: '91 ? 95',
    #          17.0: '96 ? 100'},
    #  'Q47': {1.0: 'male', 2.0: 'female'},
    #  'Q19_gruppiert_final': {1.0: '1', 2.0: '2', 3.0: '3', 4.0: '4', 5.0: '5', 6.0: '6-9', 7.0: '10-19', 8.0: '20-49',
    #                          9.0: '50+'}, 'Q8_Kleinkind': {0.0: 'no', 1.0: 'yes'},
    #  'Q8_Schulkind': {0.0: 'no', 1.0: 'yes'}, 'Q8_Teenager': {0.0: 'no', 1.0: 'yes'},
    dict_code2commune = {0.0: 'Others', 1.0: 'Aarau', 2.0: 'Adelboden', 3.0: 'Adliswil', 4.0: 'Aeschi bei Spiez',
                         5.0: 'Affoltern am Albis', 6.0: 'Airolo', 7.0: 'Albula/Alvra', 8.0: 'Alpnach',
                         9.0: 'Alt St. Johann', 10.0: 'Altdorf (UR)', 11.0: 'Amden', 12.0: 'Andeer', 13.0: 'Andermatt',
                         14.0: 'Anniviers', 15.0: 'Appenzell', 16.0: 'Arbon', 17.0: 'Ardez', 18.0: 'Arlesheim',
                         19.0: 'Arosa', 20.0: 'Ascona', 21.0: 'Attinghausen', 22.0: 'Avenches', 23.0: 'Ayent',
                         24.0: 'Baar', 25.0: 'Bad Ragaz', 26.0: 'Bad Zurzach', 27.0: 'Baden', 28.0: 'Bagnes',
                         29.0: 'Balsthal', 30.0: 'Basel', 31.0: 'Bassersdorf', 32.0: 'Bauen', 33.0: 'Beatenberg',
                         34.0: 'Beckenried', 35.0: 'Bellevue', 36.0: 'Bellinzona', 37.0: 'Bellwald',
                         38.0: 'Bergün/Bravuogn', 39.0: 'Bern', 40.0: 'Bettlach', 41.0: 'Bettmeralp', 42.0: 'Bever',
                         43.0: 'Bex', 44.0: 'Biasca', 45.0: 'Biel/Bienne', 46.0: 'Birsfelden', 47.0: 'Bissone',
                         48.0: 'Bivio', 49.0: 'Blatten', 50.0: 'Bönigen', 51.0: 'Bourg-en-Lavaux', 52.0: 'Braunwald',
                         53.0: 'Bregaglia', 54.0: 'Breil/Brigels', 55.0: 'Brienz (BE)', 56.0: 'Brig-Glis',
                         57.0: 'Brissago', 58.0: 'Brugg', 59.0: 'Brusino Arsizio', 60.0: 'Bubendorf',
                         61.0: 'Buchs (SG)', 62.0: 'Bulle', 63.0: 'Bullet', 64.0: 'Buochs', 65.0: 'Burgdorf',
                         66.0: 'Bürglen (UR)', 67.0: 'Bussigny', 68.0: 'Bütschwil-Ganterschwil', 69.0: 'Cademario',
                         70.0: 'Celerina/Schlarigna', 71.0: 'Cham', 72.0: 'Champéry', 73.0: 'Chardonne',
                         74.0: "Château-d'Oex", 75.0: 'Chavannes-de-Bogis', 76.0: 'Chermignon', 77.0: 'Chexbres',
                         78.0: 'Chiasso', 79.0: 'Chur', 80.0: 'Churwalden', 81.0: "Collina d'Oro",
                         82.0: 'Crans-Montana', 83.0: 'Crissier', 84.0: 'Dällikon', 85.0: 'Davos', 86.0: 'Degersheim',
                         87.0: 'Delémont', 88.0: 'Diepoldsau', 89.0: 'Dietikon', 90.0: 'Disentis/Mustér',
                         91.0: 'Dornach', 92.0: 'Dübendorf', 93.0: 'Duggingen', 94.0: 'Ebnat-Kappel',
                         95.0: 'Ecublens (VD)', 96.0: 'Egerkingen', 97.0: 'Eich', 98.0: 'Einsiedeln', 99.0: 'Elm',
                         100.0: 'Emmen', 101.0: 'Emmetten', 102.0: 'Enetschwil', 103.0: 'Engelberg', 104.0: 'Erstfeld',
                         105.0: 'Estavayer-le-Lac', 106.0: 'Evolène', 107.0: 'Falera', 108.0: 'Feusisberg',
                         109.0: 'Fiesch', 110.0: 'Fischingen', 111.0: 'Flims', 112.0: 'Flüelen', 113.0: 'Flühli',
                         114.0: 'Flums', 115.0: 'Frauenfeld', 116.0: 'Freienbach', 117.0: 'Fribourg', 118.0: 'Frutigen',
                         119.0: 'Ftan', 120.0: 'Gais', 121.0: 'Gaiserwald', 122.0: 'Gambarogno', 123.0: 'Genève',
                         124.0: 'Geroldswil', 125.0: 'Gersau', 126.0: 'Giswil', 127.0: 'Givisiez', 128.0: 'Glarus',
                         129.0: 'Göschenen', 130.0: 'Gottlieben', 131.0: 'Grächen', 132.0: 'Granges-Paccot',
                         133.0: 'Grenchen', 134.0: 'Grindelwald', 135.0: 'Grüsch', 136.0: 'Gruyères', 137.0: 'Gstaad',
                         138.0: 'Guarda', 139.0: 'Gurtnellen', 140.0: 'Guttannen', 141.0: 'Güttingen',
                         142.0: 'Hasliberg', 143.0: 'Heiden', 144.0: 'Hemberg', 145.0: 'Hergiswil (NW)',
                         146.0: 'Herisau', 147.0: 'Hilterfingen', 148.0: 'Horgen', 149.0: 'Höri', 150.0: 'Horn',
                         151.0: 'Horw', 152.0: 'Hospental', 153.0: 'Ingenbohl', 154.0: 'Innertkirchen',
                         155.0: 'Interlaken', 156.0: 'Ipsach', 157.0: 'Iseltwald', 158.0: 'Isenthal', 159.0: 'Ittigen',
                         160.0: 'Kandersteg', 161.0: 'Kappel am Albis', 162.0: 'Kerns', 163.0: 'Kirchberg',
                         164.0: 'Klosters-Serneus', 165.0: 'Kloten', 166.0: 'Köniz', 167.0: 'Konolfingen',
                         168.0: 'Kreuzlingen', 169.0: 'Kriens', 170.0: 'Küblis', 171.0: 'Küsnacht (ZH)',
                         172.0: 'Küssnacht (SZ)', 173.0: 'La Chaux-de-Fonds', 174.0: 'La Punt-Chamues-ch',
                         175.0: 'La Tène', 176.0: 'La Tour-de-Peilz', 177.0: 'Laax', 178.0: 'Lancy',
                         179.0: 'Langenthal', 180.0: 'Lausanne', 181.0: 'Lauterbrunnen', 182.0: 'Lavey-Morcles',
                         183.0: 'Lavin', 184.0: 'Le Chenit', 185.0: 'Le Grand-Saconnex', 186.0: 'Leissigen',
                         187.0: 'Lenk', 188.0: 'Lens', 189.0: 'Lenzburg', 190.0: 'Lenzerheide', 191.0: 'Leukerbad',
                         192.0: 'Leysin', 193.0: 'Leytron', 194.0: 'Lichtensteig', 195.0: 'Liestal', 196.0: 'Linthal',
                         197.0: 'Locarno', 198.0: 'Losone', 199.0: 'Lugano', 200.0: 'Lungern', 201.0: 'Lütisburg',
                         202.0: 'Lützelflüh', 203.0: 'Luzern', 204.0: 'Lyss', 205.0: 'Madulain', 206.0: 'Maienfeld',
                         207.0: 'Maloja', 208.0: 'Männedorf', 209.0: 'Martigny', 210.0: 'Matten bei Interlaken',
                         211.0: 'Meggen', 212.0: 'Meiringen', 213.0: 'Meisterschwanden', 214.0: 'Melide',
                         215.0: 'Mendrisio', 216.0: 'Meyrin', 217.0: 'Minusio', 218.0: 'Montagny-près-Yverdon',
                         219.0: 'Montana', 220.0: 'Monte Carasso', 221.0: 'Montreux', 222.0: 'Mörel-Filet',
                         223.0: 'Morges', 224.0: 'Möriken-Wildegg', 225.0: 'Morschach', 226.0: 'Mosnang',
                         227.0: 'Münsterlingen', 228.0: 'Muralto', 229.0: 'Muri bei Bern', 230.0: 'Mürren',
                         231.0: 'Murten', 232.0: 'Muttenz', 233.0: 'Näfels', 234.0: 'Naters', 235.0: 'Neckertal',
                         236.0: 'Nendaz', 237.0: 'Nesslau', 238.0: 'Neuchâtel', 239.0: 'Nottwil', 240.0: 'Nyon',
                         241.0: 'Oberägeri', 242.0: 'Oberentfelden', 243.0: 'Obergoms', 244.0: 'Oberhelfenschwil',
                         245.0: 'Oberhofen am Thunersee', 246.0: 'Oberkirch', 247.0: 'Ollon', 248.0: 'Olten',
                         249.0: 'Opfikon', 250.0: 'Ormont-Dessous', 251.0: 'Ormont-Dessus', 252.0: 'Orselina',
                         253.0: 'Orsières', 254.0: 'Paradiso', 255.0: 'Plaffeien', 256.0: 'Ponte Tresa',
                         257.0: 'Pontresina', 258.0: 'Poschiavo', 259.0: 'Prangins', 260.0: 'Pratteln', 261.0: 'Pura',
                         262.0: 'Quarten', 263.0: 'Quinto', 264.0: 'Ramosch', 265.0: 'Randogne',
                         266.0: 'Rapperswil-Jona', 267.0: 'Raron', 268.0: 'Realp', 269.0: 'Reckingen-Gluringen',
                         270.0: 'Regensdorf', 271.0: 'Reichenbach im Kandertal', 272.0: 'Rheinfelden',
                         273.0: 'Riederalp', 274.0: 'Ringgenberg (BE)', 275.0: 'Risch', 276.0: 'Ronco sopra Ascona',
                         277.0: 'Rorschacherberg', 278.0: 'Rothenburg', 279.0: 'Rothrist', 280.0: 'Rovio',
                         281.0: 'Rümlang', 282.0: 'Rüschlikon', 283.0: 'Rüte', 284.0: 'S-chanf', 285.0: 'S-charf',
                         286.0: 'Saanen', 287.0: 'Saas-Almagell', 288.0: 'Saas-Fee', 289.0: 'Saas-Grund',
                         290.0: 'Sachseln', 291.0: 'Saignelégier', 292.0: 'Saillon', 293.0: 'Saint-Maurice',
                         294.0: 'Saint-Sulpice (VD)', 295.0: 'Samedan', 296.0: 'Samnaun', 297.0: 'Sarnen',
                         298.0: 'Savognin', 299.0: 'Schaffhausen', 300.0: 'Schangnau', 301.0: 'Schattdorf',
                         302.0: 'Schlieren', 303.0: 'Schwanden', 304.0: 'Schwarzenberg', 305.0: 'Schwende',
                         306.0: 'Schwyz', 307.0: 'Scuol', 308.0: 'Seedorf (UR)', 309.0: 'Seelisberg',
                         310.0: 'Seewis im Prättigau', 311.0: 'Sent', 312.0: 'Sierre', 313.0: 'Sigriswil',
                         314.0: 'Silenen', 315.0: 'Sils im Engadin/Segl', 316.0: 'Silvaplana', 317.0: 'Sins',
                         318.0: 'Sion', 319.0: 'Sisikon', 320.0: 'Solothurn', 321.0: 'Spiez', 322.0: 'Spiringen',
                         323.0: 'Splügen', 324.0: 'Spreitenbach', 325.0: 'St. Antönien', 326.0: 'St. Gallen',
                         327.0: 'St. Moritz', 328.0: 'Stallikon', 329.0: 'Stans', 330.0: 'Stansstad',
                         331.0: 'Steckborn', 332.0: 'Stein am Rhein', 333.0: 'Studen (BE)', 334.0: 'Sur En',
                         335.0: 'Sursee', 336.0: 'Susch', 337.0: 'Tarasp', 338.0: 'Täsch', 339.0: 'Terre di Pedemonte',
                         340.0: 'Teufen (AR)', 341.0: 'Thalwil', 342.0: 'Thun', 343.0: 'Thusis', 344.0: 'Tschlin',
                         345.0: 'Tujetsch', 346.0: 'Twann-Tüscherz', 347.0: 'Unterägeri', 348.0: 'Unterschächen',
                         349.0: 'Unterseen', 350.0: 'Unterwasser', 351.0: 'Uster', 352.0: 'Uzwil', 353.0: 'Val Müstair',
                         354.0: "Val-d'Illiez", 355.0: 'Val-de-Charmey', 356.0: 'Val-de-Ruz', 357.0: 'Vals',
                         358.0: 'Vaz/Obervaz', 359.0: 'Verbier', 360.0: 'Versoix', 361.0: 'Vevey', 362.0: 'Veysonnaz',
                         363.0: 'Vezia', 364.0: 'Vico Morcote', 365.0: 'Villigen', 366.0: 'Villmergen',
                         367.0: 'Vilters-Wangs', 368.0: 'Visp', 369.0: 'Vitznau', 370.0: 'Vnà', 371.0: 'Vulpera',
                         372.0: 'Wädenswil', 373.0: 'Walchwil', 374.0: 'Wäldi', 375.0: 'Walenstadt',
                         376.0: 'Waltensburg/Vuorz', 377.0: 'Walzenhausen', 378.0: 'Warth-Weiningen', 379.0: 'Wassen',
                         380.0: 'Wattwil', 381.0: 'Weggis', 382.0: 'Weinfelden', 383.0: 'Wengen',
                         384.0: 'Wetzikon (ZH)', 385.0: 'Widnau', 386.0: 'Wiedlisbach', 387.0: 'Wil (SG)',
                         388.0: 'Wilderswil', 389.0: 'Wildhaus', 390.0: 'Wildhaus-Alt St. Johann', 391.0: 'Winterthur',
                         392.0: 'Wolfenschiessen', 393.0: 'Yverdon-les-Bains', 394.0: 'Zermatt', 395.0: 'Zernez',
                         396.0: 'Zofingen', 397.0: 'Zug', 398.0: 'Zuoz', 399.0: 'Zürich', 400.0: 'Zweisimmen',
                         401.0: 'Zinal', 402.0: 'Zuzwil (SG)', 403.0: 'Bad Zurzach', 404.0: 'Zillis-Reischen',
                         405.0: 'Yvonand', 406.0: 'Yens', 407.0: 'Lantsch/Lenz', 408.0: 'Wimmis', 409.0: 'Wichtrach',
                         410.0: 'Weissbad', 411.0: 'Weingarten', 412.0: 'Wasserauen Ebenalp', 413.0: 'Walkringen',
                         414.0: 'Waldstatt', 415.0: 'Vrin', 416.0: 'Volketswil', 417.0: 'Vogorno', 418.0: 'Vissoie',
                         419.0: 'Vira (Gambarogno)', 420.0: 'Villarzel', 421.0: 'Villars-sur-Ollon', 422.0: 'Vercorin',
                         423.0: 'Versegères', 424.0: 'Vernayaz', 425.0: 'Vella', 426.0: 'Vaulruz', 427.0: 'Vattiz',
                         428.0: 'Vallorbe', 429.0: 'Valbella', 430.0: 'Sent', 431.0: 'La Flouly', 432.0: 'Grimentz',
                         433.0: 'La Tzoumaz', 434.0: 'Les Diablerets', 435.0: 'Lucens', 436.0: 'Melchsee-Frutt',
                         437.0: 'Ovronnaz', 438.0: 'Anzère', 439.0: 'Chandolin', 441.0: 'Vairano', 442.0: 'Vaduz',
                         443.0: 'Uznach', 444.0: 'Unterterzen', 445.0: 'Unteriberg', 446.0: 'Unterbach',
                         447.0: 'Ulrichen', 448.0: 'Tschuggen Blatten b. Naters', 449.0: 'Tschiertschen-Praden',
                         450.0: 'Trun', 451.0: 'Trub', 452.0: 'Troinex', 453.0: 'Torgon', 454.0: 'Tiefencastel',
                         455.0: 'Les Collons Thyon', 456.0: 'Salvan', 457.0: "Château-d'Oex", 458.0: 'Les Breuleux',
                         459.0: 'Le Bouveret', 460.0: "L'Abbaye", 461.0: 'Thayngen', 462.0: 'Tesseret',
                         463.0: 'Tennwil', 464.0: 'Tenero-Contra', 465.0: 'Agno', 466.0: 'Susten', 467.0: 'Sumvitg',
                         468.0: 'Suhr', 469.0: 'Strengelbach', 470.0: 'Stoos', 471.0: 'Steinhausen', 472.0: 'Stein SG',
                         473.0: 'Stäfa', 474.0: 'Staad', 475.0: 'St. Ursanne', 476.0: 'St. Stephan',
                         477.0: 'Saint-Aubin (FR)', 478.0: 'St. Luc', 479.0: 'St. Jean', 480.0: 'Sainte-Croix',
                         481.0: 'Soubey', 482.0: 'Sessa', 483.0: 'Sempach', 484.0: 'Seengen', 485.0: 'Sedrun',
                         486.0: 'Sonogno', 487.0: 'Sutz-Lattrigen', 488.0: 'Sirnach', 489.0: 'Schwerzenbach',
                         490.0: 'Schwellbrunn', 491.0: 'Schwarzsee', 492.0: 'Schwarzenburg', 493.0: 'Säntis-Schwägalp',
                         494.0: 'Schüpfheim', 495.0: 'Schmitten (FR)', 496.0: 'Schluein', 497.0: 'Scheid', 498.0: 'Sax',
                         499.0: 'Savièse', 500.0: 'Sattel', 501.0: 'Sargans', 502.0: 'San Nazzaro', 505.0: 'Sauges',
                         506.0: 'Saas-Balen', 507.0: 'Ruswil', 508.0: 'Rougemont', 509.0: 'Rothenbrunnen',
                         510.0: 'Termen', 511.0: 'Rossinière', 512.0: 'Maggia', 513.0: 'Tinizong-Rona',
                         514.0: 'Romanshorn', 515.0: 'Rodels', 516.0: 'Riom-Parsonz', 517.0: 'Rigi', 518.0: 'Ried-Brig',
                         519.0: 'Riddes', 520.0: 'Ricken', 521.0: 'Reinach (AG)', 522.0: 'Rehetobel', 523.0: 'Rebstein',
                         524.0: 'Ranzo', 525.0: 'Randa', 526.0: 'Rafz', 527.0: 'Promontogno', 528.0: 'Gondo',
                         529.0: 'Prez-vers-Siviriez', 530.0: 'Porrentruy', 531.0: 'Ambri-Piotta', 532.0: 'Piazzogna',
                         533.0: 'St. Niklaus', 534.0: 'Payerne', 535.0: 'Luzein', 536.0: 'St. Peter-Pagig',
                         537.0: 'Otelfingen', 538.0: 'Orbe', 539.0: 'Olivone', 540.0: 'Oberwald', 541.0: 'Urmein',
                         542.0: 'Obersaxen Mundaun', 543.0: 'Oberrieden', 544.0: 'Oberried am Brienzersee',
                         545.0: 'Oberiberg', 546.0: 'Oberglatt', 547.0: 'Obergesteln', 548.0: 'Oberwil ZH',
                         549.0: 'Niederwald', 550.0: 'Niederstocken', 551.0: 'Oberdorf NW', 552.0: 'Niedermuhlern',
                         553.0: 'Niedergösgen', 554.0: 'Niederbip', 555.0: 'Nidau', 556.0: 'Neuheim',
                         557.0: 'Neuhausen am Rheinfall', 558.0: 'Neuenhof', 559.0: 'Nebikon', 560.0: 'Nax',
                         561.0: 'Muzzano', 562.0: 'Ernen', 563.0: 'Münsingen', 564.0: 'Mülenen', 565.0: 'Mosen',
                         566.0: 'Leuk', 567.0: 'Lourtier', 568.0: 'Lütschental', 569.0: 'Magadino', 570.0: 'Magliaso',
                         571.0: 'Faido', 572.0: 'Malters', 573.0: 'Moutier', 574.0: 'Morgins', 575.0: 'Montfaucon',
                         576.0: 'Montezillon', 577.0: 'Möhlin', 578.0: 'Miège', 579.0: 'Mels', 580.0: 'Meilen',
                         581.0: 'Medeglia', 582.0: 'Mase', 583.0: 'Marbach SG', 584.0: 'Mammern', 585.0: 'Lignières',
                         586.0: 'Hérémence', 587.0: 'Vex', 588.0: 'Acquarossa', 589.0: 'Le Bémont (JU)', 590.0: 'Lax',
                         591.0: 'Lavertezzo', 592.0: 'Laufenburg', 593.0: 'Lauenen', 594.0: 'Langenbruck',
                         595.0: 'Landquart', 596.0: 'Ilanz/Glion', 597.0: 'Lachen', 598.0: 'Champex-Lac',
                         599.0: 'La Praz', 600.0: 'Krattigen', 601.0: 'Kradolf-Schönenberg', 602.0: 'Böttstein',
                         603.0: 'Kippel', 604.0: 'Kiental', 605.0: 'Bürchen', 606.0: 'Kaltbrunn', 607.0: 'Jaun',
                         608.0: 'Intragna', 609.0: 'Huttwil', 610.0: 'Hünenberg', 611.0: 'Neuenkirch',
                         612.0: 'Hasle (LU)', 613.0: 'Habkern', 614.0: 'Gwatt', 615.0: 'Gubrü', 616.0: 'Gunten',
                         617.0: 'Gsteigwiler', 618.0: 'Gryon', 619.0: 'Grimisuat', 620.0: 'Greppen', 621.0: 'Grengiols',
                         622.0: 'Granges-Marnand', 623.0: 'Gorgier', 624.0: 'Gorduno', 625.0: 'Gordola',
                         626.0: 'Gordevio', 627.0: 'Arth-Goldau', 628.0: 'Giumaglio', 629.0: 'Gilly', 630.0: 'Pfäfers',
                         631.0: 'Gebertingen', 632.0: 'Gams', 633.0: 'Gadmen', 634.0: 'Fusio', 635.0: 'Furna',
                         636.0: 'Fully', 637.0: 'Founex', 638.0: 'Flurlingen', 639.0: 'Flawil', 640.0: 'Fionnay',
                         641.0: 'Filisur', 642.0: 'Gsteig', 644.0: 'Feldis / Veulden', 645.0: 'Eschenz', 646.0: 'Ernen',
                         647.0: 'Erlenbach BE', 648.0: 'Erlach', 649.0: 'Eriswil', 650.0: 'Ergisch', 651.0: 'Entlebuch',
                         652.0: 'Ennetbürgen', 653.0: 'Ehrendingen', 654.0: 'Egnach', 655.0: 'Eggberge',
                         656.0: 'Echallens', 657.0: 'Ebikon', 658.0: 'Valendas', 659.0: 'Duillier', 660.0: 'Dätwil',
                         661.0: 'Därligen', 662.0: 'Däniken', 663.0: 'Cully', 664.0: 'Cugnasco', 665.0: 'Cudrefin',
                         666.0: 'Intragna', 667.0: 'Commugny', 668.0: 'Collombey-Muraz', 669.0: 'Claro',
                         670.0: 'Cinuos-chel', 671.0: 'Chevenez', 672.0: 'Chernex', 673.0: 'Vollèges',
                         674.0: 'Châtel-Saint-Denis', 675.0: 'Chasseral', 676.0: 'Champoussin', 677.0: 'Champfèr',
                         678.0: 'Chamoson', 679.0: 'Chalais', 680.0: 'Cevio', 681.0: 'Cavigliano', 682.0: 'Veytaux',
                         683.0: 'Casti-Wergenstein', 684.0: 'Caslano', 685.0: 'Carona', 686.0: 'Capolago',
                         687.0: 'Buttisholz', 688.0: 'Bülach', 689.0: 'Buch SH', 690.0: 'Brunnen', 691.0: 'Bristen',
                         692.0: 'Brione', 693.0: 'Brigerbad', 694.0: 'Bondo', 695.0: 'Blonay', 696.0: 'Blitzingen',
                         697.0: 'Birr', 698.0: 'Binningen', 699.0: 'Binn', 700.0: 'Agra', 701.0: 'Biel-Kinzig',
                         702.0: 'Grafschaft', 703.0: 'Betschwanden', 704.0: 'Berneck', 705.0: 'Belp', 706.0: 'Bellikon',
                         707.0: 'Belfaux', 708.0: 'Bavois', 710.0: 'Alvaneu Bad', 711.0: 'Avers', 712.0: 'Avegno',
                         713.0: 'Aurigeno', 714.0: 'Aubonne', 715.0: 'Arvigo', 716.0: 'Arolla', 717.0: 'Ardez',
                         718.0: 'Arbaz', 719.0: 'Albinen', 720.0: 'Aigle', 721.0: 'Affoltern im Emmental',
                         722.0: 'Aesch LU', 723.0: 'Adligenswil', 724.0: 'Aarwangen', 725.0: 'Aadorf',
                         726.0: 'Münster-Geschinen', 727.0: 'Rochefort', 728.0: 'Arth', 729.0: 'Calanca',
                         730.0: 'Avegno Gordevio', 731.0: 'Glarus Süd', 732.0: 'Surses', 733.0: 'Nods',
                         734.0: 'Haute-Ajoie', 735.0: 'Cugnasco-Gerra', 736.0: 'Gommiswald', 737.0: 'Domleschg',
                         738.0: 'Lavizzara', 739.0: 'Zwischbergen', 740.0: 'Centovalli', 741.0: 'Port-Valais',
                         742.0: 'Mont-Noble', 743.0: 'Monteceneri', 744.0: 'Troistorrents', 745.0: 'Hitzkirch',
                         746.0: 'Blenio', 747.0: 'Sivierez', 748.0: 'Valsot', 749.0: 'Saint-Aubin-Sauges',
                         750.0: 'Sennwald', 751.0: 'Clos du Doubs', 752.0: 'Thal', 753.0: 'Capriasca', 754.0: 'Vionnaz',
                         755.0: 'Safiental', 756.0: 'Lumnezia', 757.0: 'Glarus Nord', 758.0: 'Escholzmatt-Marbach',
                         759.0: 'Lengnau (BE)', 760.0: 'Langnau im Emmental', 761.0: 'Hofstetten bei Brienz',
                         762.0: 'Gossau SG', 763.0: 'Kandergrund', 764.0: 'Müllheim', 765.0: 'Wald (AR)',
                         766.0: 'Villeneuve (VD)', 767.0: 'Trin', 768.0: 'Seewen', 769.0: 'Romont (FR)',
                         770.0: 'Rüti (ZH)', 771.0: 'Pfäffikon', 772.0: 'Oberriet (SG)', 773.0: 'Lindau',
                         774.0: 'Courrendlin', 775.0: 'Tschappina', 776.0: 'Speicher', 777.0: 'Diemtigen',
                         778.0: 'Arogno', 779.0: 'Eptingen', 780.0: 'Valbroye', 781.0: 'Nürensdorf', 99999996.0: '-99'}
    #  'Q54_01': {1.0: 'Swiss Travel Pass', 2.0: 'Interrail', 3.0: 'Eurail Pass', 4.0: 'one-way/round trip ticket',
    #             5.0: 'group ticket', 6.0: 'half-fare pass', 7.0: 'day pass', 8.0: 'general travel pass',
    #             9.0: 'route pass/regional pass', 10.0: 'other:'},
    #  'Q54_02': {1.0: 'Swiss Travel Pass', 2.0: 'Interrail', 3.0: 'Eurail Pass', 4.0: 'one-way/round trip ticket',
    #             5.0: 'group ticket', 6.0: 'half-fare pass', 7.0: 'day pass', 8.0: 'general travel pass',
    #             9.0: 'route pass/regional pass', 10.0: 'other:'},
    #  'Q54_03': {1.0: 'Swiss Travel Pass', 2.0: 'Interrail', 3.0: 'Eurail Pass', 4.0: 'one-way/round trip ticket',
    #             5.0: 'group ticket', 6.0: 'half-fare pass', 7.0: 'day pass', 8.0: 'general travel pass',
    #             9.0: 'route pass/regional pass', 10.0: 'other:'},
    #  'Q54_04': {1.0: 'Swiss Travel Pass', 2.0: 'Interrail', 3.0: 'Eurail Pass', 4.0: 'one-way/round trip ticket',
    #             5.0: 'group ticket', 6.0: 'half-fare pass', 7.0: 'day pass', 8.0: 'general travel pass',
    #             9.0: 'route pass/regional pass', 10.0: 'other:'},
    #  'Q54_05': {1.0: 'Swiss Travel Pass', 2.0: 'Interrail', 3.0: 'Eurail Pass', 4.0: 'one-way/round trip ticket',
    #             5.0: 'group ticket', 6.0: 'half-fare pass', 7.0: 'day pass', 8.0: 'general travel pass',
    #             9.0: 'route pass/regional pass', 10.0: 'other:'},
    #  'Q54_06': {1.0: 'Swiss Travel Pass', 2.0: 'Interrail', 3.0: 'Eurail Pass', 4.0: 'one-way/round trip ticket',
    #             5.0: 'group ticket', 6.0: 'half-fare pass', 7.0: 'day pass', 8.0: 'general travel pass',
    #             9.0: 'route pass/regional pass', 10.0: 'other:'},
    #  'Q54_07': {1.0: 'Swiss Travel Pass', 2.0: 'Interrail', 3.0: 'Eurail Pass', 4.0: 'one-way/round trip ticket',
    #             5.0: 'group ticket', 6.0: 'half-fare pass', 7.0: 'day pass', 8.0: 'general travel pass',
    #             9.0: 'route pass/regional pass', 10.0: 'other:'},
    #  'Q54_08': {1.0: 'Swiss Travel Pass', 2.0: 'Interrail', 3.0: 'Eurail Pass', 4.0: 'one-way/round trip ticket',
    #             5.0: 'group ticket', 6.0: 'half-fare pass', 7.0: 'day pass', 8.0: 'general travel pass',
    #             9.0: 'route pass/regional pass', 10.0: 'other:'},
    #  'Q54_09': {1.0: 'Swiss Travel Pass', 2.0: 'Interrail', 3.0: 'Eurail Pass', 4.0: 'one-way/round trip ticket',
    #             5.0: 'group ticket', 6.0: 'half-fare pass', 7.0: 'day pass', 8.0: 'general travel pass',
    #             9.0: 'route pass/regional pass', 10.0: 'other:'},
    #  'Q54_10': {1.0: 'Swiss Travel Pass', 2.0: 'Interrail', 3.0: 'Eurail Pass', 4.0: 'one-way/round trip ticket',
    #             5.0: 'group ticket', 6.0: 'half-fare pass', 7.0: 'day pass', 8.0: 'general travel pass',
    #             9.0: 'route pass/regional pass', 10.0: 'other:'},
    #  'Q3_touring_3cat': {1.0: 'Non-touring', 2.0: 'Touring in CH', 3.0: 'Touring only in Europe'},
    #  'Q18': {1.0: 'yes, a group travel package', 2.0: 'yes, an independent travel package', 3.0: 'no'}}

    # print('Total number of observations:', tot_nb_obs)
    df = df.loc[df.Q2B_ST_markets_detail_new2 != 4, :]
    # nb_foreigners = len(df)
    # print('Number of foreigners in the dataset:', nb_foreigners, '(' +
    #       str(100 * round(nb_foreigners / tot_nb_obs, 3)) + '%)')
    df = df.loc[~df.Q9_bereinigt_gruppiert_final.isnull(), :]
    # nb_obs = len(df)
    # print('Number of observations with main mode choice:', nb_obs, '(' +
    #       str(100 * round(nb_obs / nb_foreigners, 3)) + '%)')
    df.drop('Gewichtung', axis=1, inplace=True)
    df = df.rename(columns={'Q9_bereinigt_gruppiert_final': 'transport_mode',
                            'Q48': 'age',
                            'Q2B_ST_markets_detail_new2': 'country',
                            'Q17': 'stars',
                            'Q16_bereinigt_final_aggregiert': 'accommodation_type',
                            'Q1_BFS_final': 'commune'})
    df.commune = df.commune.map(dict_code2commune)  # Transforms code from dataset into name of the commune
    df = add_urban_rural_typology(df)
    df = add_regions(df)
    df = df.drop(['Gemeindename', 'commune'], axis=1)
    df.country = df.country.astype(int)
    df['stars'] = df['stars'].map({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})  # Removing codings 7, 8 & 9
    # Grouping motorcycle and car together; camper as other
    df.transport_mode = df.transport_mode.astype(int)
    df['transport_mode'] = df['transport_mode'].map({1: 1, 2: 2, 3: 3, 4: 9, 5: 3, 6: 6, 7: 7, 8: 8, 9: 9})

    df.fillna(-99, inplace=True)

    # Uncomment, if visual checks are needed:
    # df.to_csv('output/dataset_TMS.csv', index=False)

    return df


def add_regions(df):
    # Read FSO data
    path_to_regions = Path('data/input/Raumgliederungen_AMR2018.xlsx')
    regions = pd.read_excel(path_to_regions, skiprows=[0, 2])
    regions = regions.drop(['BFS Gde-nummer', 'Kantons-nummer', 'Kanton', 'Bezirks-nummer', 'Bezirksname',
                            'Arbeitsmarktregionen 2018'], axis=1)
    regions = regions.rename(columns={'Arbeitsmarktgrossregionen 2018': 'region'})
    df.loc[df.commune == 'Filisur', 'commune'] = 'Bergün Filisur'
    df.loc[df.commune == 'Bergün/Bravuogn', 'commune'] = 'Bergün Filisur'
    df.loc[df.commune == 'Waltensburg/Vuorz', 'commune'] = 'Breil/Brigels'
    df.loc[df.commune == 'Gorgier', 'commune'] = 'La Grande-Béroche'
    df.loc[df.commune == 'Saint-Aubin-Sauges', 'commune'] = 'La Grande-Béroche'
    df = df.merge(regions, how='left', left_on='commune', right_on='Gemeindename')
    df['urban_rural_typology'] = df['urban_rural_typology'].fillna(value=-99)
    return df


def add_urban_rural_typology(df):
    # Read FSO data
    path_to_urban_rural_typology = Path('data/input/Raumgliederungen_StadtLand2017.xlsx')
    urban_rural_typology = pd.read_excel(path_to_urban_rural_typology, skiprows=[0, 2])
    urban_rural_typology = urban_rural_typology.drop(['BFS Gde-nummer', 'Kantons-nummer', 'Kanton', 'Bezirks-nummer',
                                                      'Bezirksname', 'Gemeindetypologie 2012 (9 Typen)',
                                                      'Gemeindetypologie 2012 (25 Typen)'], axis=1)
    urban_rural_typology = urban_rural_typology.rename(columns={'Städtische / Ländliche Gebiete':
                                                                'urban_rural_typology'})
    df.loc[df.commune == 'Aesch LU', 'commune'] = 'Aesch (LU)'
    df.loc[df.commune == 'Oberdorf NW', 'commune'] = 'Oberdorf (NW)'
    df.loc[df.commune == 'Sivierez', 'commune'] = 'Siviriez'
    df.loc[df.commune == 'Niederbip', 'commune'] = 'Niederbipp'
    df.loc[df.commune == 'Blitzingen', 'commune'] = 'Goms'
    df.loc[df.commune == 'Reckingen-Gluringen', 'commune'] = 'Goms'
    df.loc[df.commune == 'Estavayer-le-Lac', 'commune'] = 'Estavayer'
    df.loc[df.commune == 'Gossau SG', 'commune'] = 'Gossau (SG)'
    df.loc[df.commune == 'Säntis-Schwägalp', 'commune'] = 'Hundwil'
    df.loc[df.commune == 'Niederstocken', 'commune'] = 'Stocken-Höfen'
    df.loc[df.commune == 'Marbach SG', 'commune'] = 'Marbach (SG)'
    df.loc[df.commune == 'Buch SH', 'commune'] = 'Buch (SH)'
    df = df.merge(urban_rural_typology, how='left', left_on='commune', right_on='Gemeindename')
    df['urban_rural_typology'] = df['urban_rural_typology'].fillna(value=-99)
    df = df.drop('Gemeindename', axis=1)
    return df
