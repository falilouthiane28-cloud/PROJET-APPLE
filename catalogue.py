# -*- coding: utf-8 -*-
"""Source unique du catalogue iStore Tech.
Modifier ici, puis relancer :  python build-pages.py
Prix en FCFA, indicatifs, a confirmer par la boutique.
"""

WA = "221784277229"

# Options de stockage reutilisables : (libelle, supplement en FCFA)
ST_IPHONE   = [("128 Go", 0), ("256 Go", 45000), ("512 Go", 120000), ("1 To", 210000)]
ST_IPHONE_P = [("256 Go", 0), ("512 Go", 105000), ("1 To", 195000)]
ST_MAC      = [("256 Go", 0), ("512 Go", 95000), ("1 To", 190000)]
ST_ANDROID  = [("128 Go", 0), ("256 Go", 40000), ("512 Go", 105000)]
# Les modeles Ultra n'existent pas en 128 Go : les proposer, c'est vendre une
# configuration que le client ne recevra jamais. Verifie chez Samsung.
ST_ULTRA    = [("256 Go", 0), ("512 Go", 65000), ("1 To", 150000)]

CATS = [
 ("iphone",  "iPhone & Apple",     "iphone-apple.html"),
 ("android", "Samsung & Android",  "samsung-android.html"),
 ("gaming",  "Gaming",             "gaming.html"),
 ("machines","Machines",           "machines.html"),
 ("audio",   "Audio",              "audio.html"),
 ("acc",     "Accessoires",        "accessoires.html"),
]

# id, nom, categorie, sous-titre, prix de base, badge, image (ou None), silhouette,
# couleurs, stockages, etat, argument
def P(id, nom, cat, sub, prix, badge, img=None, sil="acc",
      couleurs=None, stockages=None, etat="Neuf scellé", note=None, top=False,
      images=None):
    """images : {couleur: fichier} pour que la photo suive le coloris choisi."""
    return dict(id=id, nom=nom, cat=cat, sub=sub, prix=prix, badge=badge, img=img, sil=sil,
                couleurs=couleurs or [], stockages=stockages or [], etat=etat, note=note,
                top=top, images=images or {})

PRODUITS = [
 # ---------------------------------------------------------------- iPhone
 P("iphone-16-pro","iPhone 16 Pro","iphone","6,3 pouces",420000,"En stock",
   "iphone-16-pro-finish-select-202409-6-3inch-blacktitanium.webp","phone",
   ["Titane noir","Titane naturel","Titane blanc","Titane désert"], ST_IPHONE_P,
   note="Puce A18 Pro, écran 120 Hz, châssis titane.", top=True,
   images={"Titane noir":"iphone-16-pro-finish-select-202409-6-3inch-blacktitanium.webp",
           "Titane naturel":"iphone-16-pro-finish-select-202409-6-3inch-naturaltitanium.webp"}),
 P("iphone-16-pro-max","iPhone 16 Pro Max","iphone","6,9 pouces",520000,"En stock",
   "iphone-16-pro-finish-select-202409-6-9inch-blacktitanium.webp","phone",
   ["Titane noir","Titane naturel","Titane blanc","Titane désert"], ST_IPHONE_P,
   note="Le plus grand écran, la plus grosse autonomie de la gamme.", top=True,
   images={"Titane noir":"iphone-16-pro-finish-select-202409-6-9inch-blacktitanium.webp",
           "Titane naturel":"iphone-16-pro-finish-select-202409-6-9inch-naturaltitanium.webp",
           "Titane blanc":"iphone-16-pro-finish-select-202409-6-9inch-whitetitanium.webp"}),
 P("iphone-16-plus","iPhone 16 Plus","iphone","6,7 pouces",395000,"En stock",
   "iphone-16-finish-select-202409-6-7inch-teal.webp","phone",
   ["Sarcelle","Noir","Blanc","Rose","Outremer"], ST_IPHONE,
   note="Grand écran, prix contenu, autonomie confortable.", top=True),
 P("iphone-16","iPhone 16","iphone","6,1 pouces",345000,"En stock","iphone-16.webp","phone",
   ["Noir","Blanc","Sarcelle","Rose","Outremer"], ST_IPHONE,
   note="Le format qui tient dans la main, la puce de la génération."),
 P("iphone-15-pro-max","iPhone 15 Pro Max","iphone","6,7 pouces",390000,"Sur commande","iphone-15-pro-max.webp","phone",
   ["Titane noir","Titane blanc","Titane bleu","Titane naturel"], ST_IPHONE_P,
   note="La génération précédente, encore très à l'aise."),
 P("iphone-15","iPhone 15","iphone","6,1 pouces",290000,"Sur commande","iphone-15.webp","phone",
   ["Noir","Bleu","Vert","Jaune","Rose"], ST_IPHONE),
 # Le fichier image du catalogue est l'asset Apple "watch-compare-s11" : c'est
 # donc une Series 11, qui existe en 42 et 46 mm et non en 41 et 45. Les coloris
 # aluminium sont ceux de cette generation.
 P("apple-watch-series","Apple Watch Series 11","iphone","Aluminium",285000,"Nouveau",
   "watch-compare-s11-202509.webp","watch",["Noir intense","Or rose","Argent","Gris sidéral"],
   [("42 mm",0),("46 mm",25000)], note="Suivi d'activité, appels, notifications au poignet.", top=True),
 P("apple-watch-ultra","Apple Watch Ultra","iphone","Titane",550000,"En stock",
   "watch-compare-ultra3-202509.webp","watch",["Titane naturel","Titane noir"],
   [("49 mm",0)], note="Batterie longue durée, résistance extrême.", top=True),
 P("apple-watch-se","Apple Watch SE","iphone","Aluminium",165000,"Livraison 24h",
   "watch-compare-se-202509.webp","watch",["Minuit","Lumière stellaire"],
   [("40 mm",0),("44 mm",20000)]),
 P("ipad-air","iPad Air","iphone","11 pouces",390000,"Sur commande","ipad-air.webp","tablet",
   ["Gris sidéral","Bleu","Mauve","Lumière stellaire"],[("128 Go",0),("256 Go",55000),("512 Go",140000)]),

 # ---------------------------------------------------------------- Android
 P("galaxy-s25-ultra","Galaxy S25 Ultra","android","6,9 pouces",565000,"En stock","galaxy-s25-ultra.webp","phone",
   ["Titane noir","Titane gris","Titane blanc argenté","Titane bleu argenté"], ST_ULTRA,
   note="Stylet intégré, zoom optique, écran très lumineux.", top=True),
 P("galaxy-s25-plus","Galaxy S25+","android","6,7 pouces",465000,"En stock","galaxy-s25-plus.webp","phone",
   ["Bleu marine","Bleu glacé","Menthe","Argent ombré"], ST_ANDROID),
 P("galaxy-s25","Galaxy S25","android","6,2 pouces",385000,"En stock","galaxy-s25.webp","phone",
   ["Bleu marine","Bleu glacé","Menthe","Argent ombré"], ST_ANDROID, top=True),
 P("galaxy-s24-ultra","Galaxy S24 Ultra","android","6,8 pouces",470000,"En stock","galaxy-s24-ultra.webp","phone",
   ["Titane noir","Titane gris","Titane violet"], ST_ULTRA),
 P("galaxy-z-flip","Galaxy Z Flip","android","Pliant",540000,"Sur commande","galaxy-z-flip.webp","phone",
   ["Noir","Bleu","Menthe"],[("256 Go",0),("512 Go",95000)],
   note="Se plie en deux, tient dans une poche de chemise."),
 P("galaxy-a56","Galaxy A56","android","6,6 pouces",165000,"En stock","galaxy-a56.webp","phone",
   ["Graphite","Gris clair","Olive","Rose"],[("128 Go",0),("256 Go",30000)], top=True),
 P("galaxy-a36","Galaxy A36","android","6,6 pouces",135000,"En stock","galaxy-a36.webp","phone",
   ["Noir","Blanc","Lavande"],[("128 Go",0),("256 Go",28000)]),
 P("galaxy-a16","Galaxy A16","android","6,7 pouces",95000,"En stock","galaxy-a16.webp","phone",
   ["Noir","Bleu","Vert"],[("128 Go",0),("256 Go",25000)]),
 P("galaxy-tab-s10","Galaxy Tab S10","android","11 pouces",345000,"Sur commande","galaxy-tab-s10.webp","tablet",
   ["Gris","Argent"],[("128 Go",0),("256 Go",50000)]),
 P("galaxy-watch","Galaxy Watch","android","44 mm",145000,"Livraison 24h","galaxy-watch.webp","watch",
   ["Noir","Argent"],[("Bluetooth",0),("LTE",35000)]),

 # ---------------------------------------------------------------- Gaming
 P("ps5-slim","PlayStation 5 Slim","gaming","Lecteur disque",440000,"En stock",
   "ps5-slim.webp","console",["Blanc"],[("1 To",0)],
   note="La version avec lecteur, pour les jeux en boîte.", top=True),
 P("ps5-digital","PlayStation 5 Digital","gaming","Sans lecteur",390000,"En stock",
   "ps5-digital.webp","console",["Blanc"],[("1 To",0)],
   note="Tout en téléchargement, moins chère à l'achat.", top=True),
 P("ps5-pro","PlayStation 5 Pro","gaming","Haut de gamme",690000,"Sur commande",
   "ps5-pro.webp","console",
   ["Blanc"],[("2 To",0)], note="Pour ceux qui veulent le maximum d'images par seconde."),
 P("dualsense","Manette DualSense","gaming","Sans fil · PS5",55000,"En stock",
   "dualsense.webp","pad",["Blanc","Noir","Rouge","Bleu","Gris camouflage"],[], top=True),
 P("dualsense-edge","Manette DualSense Edge","gaming","Pro · PS5",145000,"Sur commande",
   "dualsense-edge.webp","pad",["Blanc"],[],
   note="Palettes arrière, sticks remplaçables, profils personnalisés."),
 P("switch-oled","Nintendo Switch OLED","gaming","Écran 7 pouces",265000,"En stock",
   "switch-oled.webp","switch",["Blanc","Néon rouge et bleu"],[("64 Go",0)], top=True),
 P("switch-lite","Nintendo Switch Lite","gaming","Portable",165000,"En stock",
   "switch-lite.webp","switch",["Bleu","Corail","Turquoise","Gris","Jaune"],[("32 Go",0)],
   note="Uniquement portable, plus légère et moins chère."),
 P("joycon","Manettes Joy-Con","gaming","La paire · Switch 2",62000,"En stock",
   "joycon.webp","pad",
   ["Néon rouge et bleu"],[], note="Pack de deux manettes Joy-Con, dans leur boîte d'origine."),
 P("switch-pro-controller","Manette Pro Controller","gaming","Sans fil · Switch",58000,"Livraison 24h",
   "switch-pro-controller.webp","pad",["Noir"],[]),
 P("xbox-series-x","Xbox Series X","gaming","1 To",430000,"Sur commande",
   "xbox-series-x.webp","console",["Noir"],[("1 To",0)]),
 P("pulse-3d","Casque PULSE 3D","gaming","Sans fil · PS5",85000,"En stock",
   "pulse-3d.webp","audio",
   ["Blanc"],[], note="Le casque officiel PS5, son 3D, micro intégré."),
 P("station-charge","Station de charge","gaming","Deux manettes · PS5",28000,"En stock",
   "station-charge.webp","acc",["Blanc"],[]),

 # ---------------------------------------------------------------- Machines
 P("macbook-air-13",'MacBook Air 13"',"machines","Puce M",550000,"En stock",
   "mba13-midnight-select-202402.webp","laptop",["Minuit","Lumière stellaire","Argent","Gris sidéral"],
   ST_MAC, note="Silencieux, léger, une journée entière d'autonomie.", top=True),
 P("macbook-air-15",'MacBook Air 15"',"machines","Puce M",650000,"En stock",
   "mba15-midnight-select-202306.webp","laptop",["Minuit","Lumière stellaire","Argent"], ST_MAC, top=True),
 P("macbook-pro-14",'MacBook Pro 14"',"machines","Puce Pro",1150000,"Sur commande",
   "mbp14-spacegray-select-202310.webp","laptop",["Gris sidéral","Argent","Noir sidéral"],
   [("512 Go",0),("1 To",130000),("2 To",320000)], note="Pour le montage, la 3D, le développement."),
 P("macbook-pro-16",'MacBook Pro 16"',"machines","Puce Pro",1550000,"Sur commande",
   "mbp16-spaceblack-select-202310.webp","laptop",["Noir sidéral","Argent"],
   [("512 Go",0),("1 To",130000),("2 To",320000)]),
 P("pc-gamer-15","MSI Cyborg 15","machines","RTX 4050 · 16 Go",690000,"En stock",
   "pc-msi-cyborg-4050.webp","laptop",
   ["Noir"],[("SSD 512 Go",0),("SSD 1 To",65000)],
   note="15,6 pouces 144 Hz, Core i5, clavier rétroéclairé."),
 P("pc-msi-cyborg-4060","MSI Cyborg 15 RTX 4060","machines","RTX 4060 · 16 Go",790000,"Sur commande",
   "pc-msi-cyborg-4060.webp","laptop",
   ["Noir"],[("SSD 512 Go",0),("SSD 1 To",65000)],
   note="La même machine, avec la carte au-dessus."),
 P("pc-gamer-17","Lenovo Legion","machines","RTX · 32 Go",950000,"Sur commande",
   "pc-lenovo-legion.webp","laptop",
   ["Noir"],[("SSD 1 To",0),("SSD 2 To",110000)],
   note="15,6 pouces, clavier RGB par touche, refroidissement renforcé."),
 P("tour-gamer","Tour gamer","machines","RTX · 32 Go",1250000,"Sur commande","tour-gamer.webp","screen",
   ["Noir","Blanc"],[("SSD 1 To",0),("SSD 2 To",120000)]),
 P("ecran-gamer-27","Écran MSI MPG 272QRF","machines","27 pouces · 360 Hz",185000,"En stock",
   "ecran-msi-272qrf.webp","screen",
   ["Noir"],[], note="WQHD 2560x1440, dalle Rapid IPS, 0,5 ms, G-SYNC."),
 P("clavier-mecanique","Clavier mécanique 60%","machines","AZERTY · RGB",45000,"En stock",
   "clavier-60.webp","keyboard",
   ["Noir et blanc"],[], note="Format compact 61 touches, filaire, rétroéclairage RGB."),
 P("souris-gamer","Souris Razer Cobra Pro","machines","Sans fil · RGB",38000,"En stock",
   "souris-razer-cobra.webp","mouse",
   ["Noir"],[], note="Sans fil, capteur haute précision, éclairage réglable."),
 P("ipad-pro","iPad Pro M4","machines","11 pouces",620000,"Sur commande",
   "ipad-pro-m4.webp","tablet",
   ["Noir sidéral","Argent"],[("256 Go",0),("512 Go",120000),("1 To",250000)],
   note="Puce M4, écran Ultra Retina XDR, compatible Apple Pencil.", top=True),

 # ---------------------------------------------------------------- Audio
 P("airpods-max","AirPods Max","audio","Réduction de bruit",385000,"En stock",
   "airpods-max-select-202409-midnight.webp","audio",["Minuit","Lumière stellaire","Bleu","Mauve","Orange"],
   [], note="Casque fermé, son large, finition métal.", top=True),
 P("airpods-pro","AirPods Pro","audio","Réduction de bruit",165000,"En stock","airpods-pro.webp","audio",
   ["Blanc"],[], top=True),
 P("airpods","AirPods","audio","Boîtier de charge",110000,"En stock","airpods.webp","audio",["Blanc"],[]),
 P("galaxy-buds","Galaxy Buds","audio","Réduction de bruit",78000,"En stock","galaxy-buds.webp","audio",
   ["Blanc","Noir","Argent"],[]),
 P("casque-gamer","Casque gamer filaire","audio","Micro détachable",42000,"En stock","casque-gamer.webp","audio",
   ["Noir","Blanc"],[]),
 P("casque-bluetooth","Casque Bluetooth","audio","Autonomie 40h",65000,"Livraison 24h","casque-bluetooth.webp","audio",
   ["Noir","Blanc","Beige"],[]),
 P("enceinte-portable","Enceinte portable","audio","Étanche",55000,"En stock","enceinte-portable.webp","acc",
   ["Noir","Bleu","Rouge"],[]),
 P("enceinte-salon","Enceinte de salon","audio","Sans fil",140000,"Sur commande","enceinte-salon.webp","acc",
   ["Noir","Blanc"],[]),

 # ---------------------------------------------------------------- Accessoires
 P("chargeur-magsafe","Chargeur MagSafe","acc","Sans fil",35000,"En stock",
   "MHXH3.webp","acc",["Blanc"],[], top=True),
 P("chargeur-20w","Chargeur secteur 20W","acc","USB-C",18000,"En stock","chargeur-20w.webp","acc",["Blanc"],[]),
 P("chargeur-65w","Chargeur secteur 65W","acc","USB-C · deux ports",32000,"En stock","chargeur-65w.webp","acc",
   ["Blanc","Noir"],[]),
 P("cable-usbc","Câble USB-C","acc","Tressé",9000,"En stock","cable-usbc.webp","acc",
   ["Blanc","Noir"],[("1 m",0),("2 m",3000)]),
 P("cable-lightning","Câble USB-C vers Lightning","acc","Certifié",14000,"En stock","cable-lightning.webp","acc",
   ["Blanc"],[("1 m",0),("2 m",4000)]),
 P("batterie-externe","Batterie externe","acc","10 000 mAh",28000,"En stock","batterie-externe.webp","acc",
   ["Noir","Blanc"],[("10 000 mAh",0),("20 000 mAh",14000)]),
 P("coque-iphone","Coque iPhone","acc","Silicone",12000,"En stock","coque-iphone.webp","phone",
   ["Noir","Blanc","Bleu","Rouge","Transparent"],[]),
 P("verre-trempe","Verre trempé","acc","Pose offerte en boutique",6000,"En stock","verre-trempe.webp","phone",
   ["Transparent"],[]),
 P("support-voiture","Support voiture","acc","Aimanté",15000,"En stock","support-voiture.webp","acc",["Noir"],[]),
 P("carte-memoire","Carte mémoire","acc","Switch",32000,"Livraison 24h","carte-memoire.webp","acc",
   ["Blanc"],[("128 Go",0),("256 Go",14000),("512 Go",38000)]),
]

def par_cat(c):
    return [p for p in PRODUITS if p["cat"] == c]

def par_id(i):
    for p in PRODUITS:
        if p["id"] == i: return p
    return None
