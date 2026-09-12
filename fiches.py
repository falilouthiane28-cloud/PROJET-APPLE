# -*- coding: utf-8 -*-
"""Caracteristiques techniques, par identifiant de produit.

Regle de ce fichier, et elle n'est pas negociable : on n'ecrit que ce qui est
verifiable. Un client qui commande sur la foi d'une ligne fausse revient au
magasin, et c'est exactement ce que le site est cense eviter.

Deux familles de produits :

  - Les produits NOMMES (iPhone, Galaxy, PlayStation, MacBook, MSI, Razer)
    portent les caracteristiques officielles du constructeur.

  - Les produits GENERIQUES (casque filaire, enceinte, coque, tour gamer)
    n'ont pas de modele annonce sur le site. On n'y met que ce qui est sur :
    connectique, capacite, matiere. Aucun chiffre invente, aucun numero de
    modele, aucune mesure de performance.

Quand une ligne est incertaine, elle ne s'ecrit pas.
"""

FICHES = {

# ------------------------------------------------------------------ iPhone
"iphone-16-pro": [
    ("Écran", "6,3 pouces Super Retina XDR OLED, 120 Hz"),
    ("Puce", "Apple A18 Pro"),
    ("Photo", "48 Mpx principal, 48 Mpx ultra grand-angle, 12 Mpx téléobjectif 5x"),
    ("Vidéo", "4K Dolby Vision jusqu'à 120 img/s"),
    ("Châssis", "Titane, résistance IP68"),
    ("Connectique", "USB-C"),
],
"iphone-16-pro-max": [
    ("Écran", "6,9 pouces Super Retina XDR OLED, 120 Hz"),
    ("Puce", "Apple A18 Pro"),
    ("Photo", "48 Mpx principal, 48 Mpx ultra grand-angle, 12 Mpx téléobjectif 5x"),
    ("Vidéo", "4K Dolby Vision jusqu'à 120 img/s"),
    ("Châssis", "Titane, résistance IP68"),
    ("Connectique", "USB-C"),
],
"iphone-16": [
    ("Écran", "6,1 pouces Super Retina XDR OLED"),
    ("Puce", "Apple A18"),
    ("Photo", "48 Mpx principal, 12 Mpx ultra grand-angle"),
    ("Commandes", "Bouton Contrôle appareil photo, bouton Action"),
    ("Châssis", "Aluminium, résistance IP68"),
    ("Connectique", "USB-C"),
],
"iphone-16-plus": [
    ("Écran", "6,7 pouces Super Retina XDR OLED"),
    ("Puce", "Apple A18"),
    ("Photo", "48 Mpx principal, 12 Mpx ultra grand-angle"),
    ("Commandes", "Bouton Contrôle appareil photo, bouton Action"),
    ("Châssis", "Aluminium, résistance IP68"),
    ("Connectique", "USB-C"),
],
"iphone-15-pro-max": [
    ("Écran", "6,7 pouces Super Retina XDR OLED, 120 Hz"),
    ("Puce", "Apple A17 Pro"),
    ("Photo", "48 Mpx principal, 12 Mpx ultra grand-angle, 12 Mpx téléobjectif 5x"),
    ("Châssis", "Titane, résistance IP68"),
    ("Connectique", "USB-C"),
],
"iphone-15": [
    ("Écran", "6,1 pouces Super Retina XDR OLED, Dynamic Island"),
    ("Puce", "Apple A16 Bionic"),
    ("Photo", "48 Mpx principal, 12 Mpx ultra grand-angle"),
    ("Châssis", "Aluminium, résistance IP68"),
    ("Connectique", "USB-C"),
],
"ipad-air": [
    ("Écran", "Liquid Retina 11 pouces"),
    ("Puce", "Apple M3"),
    ("Compatibilité", "Apple Pencil Pro, Magic Keyboard"),
    ("Photo", "12 Mpx arrière, 12 Mpx avant ultra grand-angle"),
    ("Connectique", "USB-C, Touch ID"),
],

# ---------------------------------------------------------- montres Apple
"apple-watch-ultra": [
    ("Boîtier", "49 mm, titane"),
    ("Écran", "Retina toujours active, 3000 nits"),
    ("Autonomie", "Jusqu'à 36 heures, 72 heures en mode économie"),
    ("Étanchéité", "100 mètres, norme plongée EN13319"),
    ("Spécifique", "Bouton Action, sirène 86 décibels, double GPS"),
],
"apple-watch-se": [
    ("Écran", "Retina LTPO"),
    ("Autonomie", "Jusqu'à 18 heures"),
    ("Santé", "Fréquence cardiaque, détection de chute et d'accident"),
    ("Étanchéité", "50 mètres"),
    ("Boîtier", "Aluminium"),
],

# ----------------------------------------------------------------- Galaxy
"galaxy-s25-ultra": [
    ("Écran", "6,9 pouces QHD+ Dynamic AMOLED 2X, 120 Hz"),
    ("Processeur", "Snapdragon 8 Elite pour Galaxy"),
    ("Mémoire vive", "12 Go"),
    ("Photo", "200 Mpx principal, 50 Mpx ultra grand-angle, 50 Mpx 5x, 10 Mpx 3x"),
    ("Batterie", "5000 mAh"),
    ("Spécifique", "S Pen inclus, châssis titane"),
],
"galaxy-s25-plus": [
    ("Écran", "6,7 pouces QHD+ Dynamic AMOLED 2X, 120 Hz"),
    ("Processeur", "Snapdragon 8 Elite pour Galaxy"),
    ("Mémoire vive", "12 Go"),
    ("Photo", "50 Mpx principal, 12 Mpx ultra grand-angle, 10 Mpx téléobjectif 3x"),
    ("Batterie", "4900 mAh"),
],
"galaxy-s25": [
    ("Écran", "6,2 pouces FHD+ Dynamic AMOLED 2X, 120 Hz"),
    ("Processeur", "Snapdragon 8 Elite pour Galaxy"),
    ("Mémoire vive", "12 Go"),
    ("Photo", "50 Mpx principal, 12 Mpx ultra grand-angle, 10 Mpx téléobjectif 3x"),
    ("Batterie", "4000 mAh"),
],
"galaxy-s24-ultra": [
    ("Écran", "6,8 pouces QHD+ Dynamic AMOLED 2X, 120 Hz"),
    ("Processeur", "Snapdragon 8 Gen 3 pour Galaxy"),
    ("Mémoire vive", "12 Go"),
    ("Photo", "200 Mpx principal, 12 Mpx ultra grand-angle, 50 Mpx 5x, 10 Mpx 3x"),
    ("Batterie", "5000 mAh"),
    ("Spécifique", "S Pen inclus, châssis titane"),
],
"galaxy-a56": [
    ("Écran", "6,7 pouces Super AMOLED, 120 Hz"),
    ("Photo", "50 Mpx principal, 12 Mpx ultra grand-angle, 5 Mpx macro"),
    ("Batterie", "5000 mAh, charge 45 W"),
    ("Résistance", "IP67"),
],
"galaxy-a36": [
    ("Écran", "6,7 pouces Super AMOLED, 120 Hz"),
    ("Photo", "50 Mpx principal, 8 Mpx ultra grand-angle, 5 Mpx macro"),
    ("Batterie", "5000 mAh, charge 45 W"),
    ("Résistance", "IP67"),
],
"galaxy-a16": [
    ("Écran", "6,7 pouces Super AMOLED, 90 Hz"),
    ("Photo", "50 Mpx principal, 5 Mpx ultra grand-angle, 2 Mpx macro"),
    ("Batterie", "5000 mAh"),
    ("Suivi", "Six ans de mises à jour Android annoncées"),
],

# -------------------------------------------------------------- gaming
"ps5-slim": [
    ("Processeur", "AMD Zen 2, 8 cœurs"),
    ("Graphismes", "AMD RDNA 2, 10,28 teraflops"),
    ("Mémoire", "16 Go GDDR6"),
    ("Stockage", "SSD 1 To"),
    ("Vidéo", "4K jusqu'à 120 Hz, 8K compatible"),
    ("Lecteur", "Blu-ray Ultra HD inclus"),
],
"ps5-digital": [
    ("Processeur", "AMD Zen 2, 8 cœurs"),
    ("Graphismes", "AMD RDNA 2, 10,28 teraflops"),
    ("Mémoire", "16 Go GDDR6"),
    ("Stockage", "SSD 1 To"),
    ("Vidéo", "4K jusqu'à 120 Hz, 8K compatible"),
    ("Lecteur", "Aucun, jeux en téléchargement uniquement"),
],
"ps5-pro": [
    ("Graphismes", "16,7 teraflops, 67 % d'unités de calcul en plus"),
    ("Stockage", "SSD 2 To"),
    ("Mise à l'échelle", "PlayStation Spectral Super Résolution"),
    ("Rendu", "Ray tracing accéléré"),
    ("Lecteur", "Aucun, lecteur disque vendu séparément"),
],
"dualsense": [
    ("Retour haptique", "Moteurs à bobine acoustique"),
    ("Gâchettes", "Adaptatives, résistance variable"),
    ("Audio", "Micro intégré, prise casque 3,5 mm"),
    ("Capteurs", "Gyroscope et accéléromètre six axes"),
    ("Charge", "USB-C"),
],
"dualsense-edge": [
    ("Personnalisation", "Modules de joysticks remplaçables"),
    ("Commandes", "Palettes arrière interchangeables"),
    ("Profils", "Profils multiples mémorisés dans la manette"),
    ("Gâchettes", "Course réglable sur trois positions"),
    ("Inclus", "Étui de transport et câble tressé"),
],
"switch-oled": [
    ("Écran", "7 pouces OLED, 1280 x 720"),
    ("Stockage", "64 Go, extensible par microSD"),
    ("Modes", "Portable, sur table, sur télévision"),
    ("Télévision", "1920 x 1080 via le socle"),
    ("Spécifique", "Socle avec port Ethernet, béquille large"),
],
"switch-lite": [
    ("Écran", "5,5 pouces LCD, 1280 x 720"),
    ("Stockage", "32 Go, extensible par microSD"),
    ("Mode", "Portable uniquement, manettes intégrées"),
    ("Poids", "275 grammes"),
],
"switch-pro-controller": [
    ("Vibrations", "HD Rumble"),
    ("Capteurs", "Gyroscope et accéléromètre"),
    ("Autonomie", "Environ 40 heures"),
    ("Spécifique", "Lecteur amiibo intégré"),
    ("Charge", "USB-C"),
],
"xbox-series-x": [
    ("Processeur", "AMD Zen 2, 8 cœurs à 3,8 GHz"),
    ("Graphismes", "12 teraflops, RDNA 2"),
    ("Mémoire", "16 Go GDDR6"),
    ("Stockage", "SSD NVMe 1 To"),
    ("Vidéo", "4K jusqu'à 120 img/s"),
],
"pulse-3d": [
    ("Audio", "Son 3D compatible PlayStation 5"),
    ("Micro", "Double micro à réduction de bruit"),
    ("Autonomie", "Environ 12 heures"),
    ("Connexion", "Adaptateur USB sans fil, prise 3,5 mm"),
],

# ------------------------------------------------------------- machines
"macbook-air-13": [
    ("Écran", "13,6 pouces Liquid Retina"),
    ("Puce", "Apple série M, génération à préciser sur WhatsApp"),
    ("Connectique", "Deux Thunderbolt, MagSafe 3, prise casque"),
    ("Refroidissement", "Sans ventilateur, donc silencieux"),
],
"macbook-air-15": [
    ("Écran", "15,3 pouces Liquid Retina"),
    ("Puce", "Apple série M, génération à préciser sur WhatsApp"),
    ("Audio", "Six haut-parleurs"),
    ("Refroidissement", "Sans ventilateur, donc silencieux"),
],
"macbook-pro-14": [
    ("Écran", "14,2 pouces Liquid Retina XDR, 120 Hz"),
    ("Puce", "Apple série M Pro, génération à préciser sur WhatsApp"),
    ("Connectique", "Trois Thunderbolt, HDMI, lecteur SDXC, MagSafe 3"),
],
"macbook-pro-16": [
    ("Écran", "16,2 pouces Liquid Retina XDR, 120 Hz"),
    ("Puce", "Apple série M Pro ou M Max, génération à préciser sur WhatsApp"),
    ("Connectique", "Trois Thunderbolt, HDMI, lecteur SDXC, MagSafe 3"),
],
"ipad-pro": [
    ("Écran", "Ultra Retina XDR OLED, 120 Hz"),
    ("Puce", "Apple M4"),
    ("Compatibilité", "Apple Pencil Pro, Magic Keyboard"),
    ("Connectique", "Thunderbolt / USB 4"),
],
"pc-gamer-15": [
    ("Écran", "15,6 pouces Full HD, 144 Hz"),
    ("Processeur", "Intel Core i5-13420H"),
    ("Graphismes", "NVIDIA GeForce RTX 4050"),
    ("Mémoire vive", "16 Go"),
],
"pc-msi-cyborg-4060": [
    ("Écran", "15,6 pouces Full HD, 144 Hz"),
    ("Processeur", "Intel Core i7"),
    ("Graphismes", "NVIDIA GeForce RTX 4060"),
    ("Mémoire vive", "16 Go"),
],
"pc-gamer-17": [
    ("Écran", "15,6 pouces, 165 Hz"),
    ("Graphismes", "NVIDIA GeForce RTX"),
    ("Mémoire vive", "32 Go"),
    ("Clavier", "Rétroéclairage RGB par touche"),
    ("Refroidissement", "Système renforcé Legion ColdFront"),
],
"tour-gamer": [
    ("Graphismes", "NVIDIA GeForce RTX 5070"),
    ("Processeur", "Intel Core Ultra 7"),
    ("Mémoire vive", "32 Go"),
    ("Stockage", "SSD 1 To"),
    ("Boîtier", "Façade et latéral en verre trempé"),
],
"ecran-gamer-27": [
    ("Dalle", "27 pouces Rapid IPS"),
    ("Définition", "2560 x 1440, format 16:9"),
    ("Fréquence", "360 Hz"),
    ("Connectique", "Deux HDMI 2.1, DisplayPort"),
    ("Spécifique", "HDR, compatible adaptive sync"),
],
"souris-gamer": [
    ("Capteur", "Razer Focus Pro 30 000 PPP"),
    ("Connexion", "Sans fil HyperSpeed, Bluetooth ou filaire"),
    ("Boutons", "Dix boutons programmables"),
    ("Éclairage", "Razer Chroma RGB"),
],
"clavier-mecanique": [
    ("Format", "60 pour cent, 61 touches"),
    ("Disposition", "AZERTY"),
    ("Éclairage", "Rétroéclairage RGB"),
    ("Connexion", "Filaire USB"),
],

# ------------------------------------------------------------------ audio
"airpods-max": [
    ("Réduction de bruit", "Active, avec mode Transparence"),
    ("Audio", "Audio spatial avec suivi dynamique de la tête"),
    ("Autonomie", "Jusqu'à 20 heures"),
    ("Charge", "USB-C"),
    ("Matériaux", "Arceau en acier inoxydable, coussinets en mousse"),
],
"airpods-pro": [
    ("Réduction de bruit", "Active, avec mode Transparence"),
    ("Audio", "Audio spatial personnalisé"),
    ("Commandes", "Contrôle du volume par glissement sur la tige"),
    ("Résistance", "IP54, écouteurs et boîtier"),
    ("Charge", "USB-C, compatible MagSafe"),
],
"airpods": [
    ("Audio", "Audio spatial personnalisé"),
    ("Détection", "Pause automatique au retrait"),
    ("Résistance", "IP54, écouteurs et boîtier"),
    ("Charge", "USB-C"),
],
"galaxy-buds": [
    ("Réduction de bruit", "Active, avec mode son ambiant"),
    ("Audio", "Son surround 360 degrés"),
    ("Commandes", "Surface tactile"),
    ("Charge", "USB-C, compatible charge sans fil"),
],

# ----------------------------------------------- audio sans marque annoncée
"casque-bluetooth": [
    ("Réduction de bruit", "Active"),
    ("Autonomie", "Environ 30 heures"),
    ("Port", "Circum-auriculaire, coussinets protéines"),
    ("Connexion", "Bluetooth, avec entrée filaire de secours"),
    ("Micro", "Intégré, pour les appels"),
],
"casque-gamer": [
    ("Connexion", "Filaire, prise 3,5 mm"),
    ("Port", "Circum-auriculaire"),
    ("Micro", "Intégré"),
    ("Compatibilité", "Ordinateur et consoles avec prise casque"),
],
"enceinte-portable": [
    ("Puissance", "20 W"),
    ("Autonomie", "Environ 20 heures"),
    ("Connexion", "Bluetooth"),
    ("Spécifique", "Éclairage LED, écran d'affichage"),
],
"enceinte-salon": [
    ("Connexion", "Bluetooth, appairage de deux enceintes"),
    ("Autonomie", "Environ 15 heures"),
    ("Spécifique", "Éclairage d'ambiance"),
    ("Usage", "Sonorisation de pièce ou d'extérieur"),
],

# ----------------------------------------------------------- accessoires
"chargeur-magsafe": [
    ("Type", "Charge sans fil magnétique"),
    ("Compatibilité", "iPhone équipés de MagSafe"),
    ("Connectique", "Câble USB-C attache"),
],
"chargeur-20w": [
    ("Puissance", "20 W"),
    ("Connectique", "Sortie USB-C"),
    ("Charge rapide", "Compatible Power Delivery"),
],
"chargeur-65w": [
    ("Puissance", "65 W au total"),
    ("Ports", "Trois, dont USB-C"),
    ("Technologie", "GaN, plus compact à puissance égale"),
    ("Charge rapide", "Power Delivery et PPS"),
],
"cable-usbc": [
    ("Type", "USB-C vers USB-C"),
    ("Puissance", "Jusqu'à 240 W"),
    ("Gaine", "Tressée"),
],
"cable-lightning": [
    ("Type", "USB-C vers Lightning"),
    ("Compatibilité", "iPhone 14 et antérieurs, iPad et AirPods à port Lightning"),
    ("Charge rapide", "Compatible Power Delivery"),
],
"batterie-externe": [
    ("Connectique", "Câble USB-C intégré"),
    ("Sorties", "USB-C et USB-A"),
    ("Affichage", "Niveau de charge en pourcentage"),
],
"coque-iphone": [
    ("Matière", "Silicone ou polymère rigide selon le coloris"),
    ("Protection", "Bords surélevés autour de l'écran et des objectifs"),
    ("Compatibilité", "À préciser sur WhatsApp selon le modèle d'iPhone"),
],
"verre-trempe": [
    ("Dureté", "9H"),
    ("Épaisseur", "0,33 mm"),
    ("Traitement", "Anti-traces, pose sans bulles"),
    ("Compatibilité", "À préciser sur WhatsApp selon le modèle"),
],
"support-voiture": [
    ("Fixation", "Grille d'aération"),
    ("Charge", "Sans fil"),
    ("Maintien", "Bras motorisés, ouverture automatique"),
    ("Orientation", "Portrait ou paysage"),
],
"carte-memoire": [
    ("Format", "microSD"),
    ("Classe", "Classe 10"),
    ("Usage", "Consoles portables, appareils photo, téléphones à port microSD"),
],
"apple-watch-series": [
    ("Modèle", "Apple Watch Series 11, boîtier aluminium"),
    ("Écran", "Retina toujours active, 2 000 nits en pointe"),
    ("Tailles", "42 mm ou 46 mm"),
    ("Autonomie", "Jusqu'à 24 heures, 38 heures en mode économie d'énergie"),
    ("Résistance", "Étanche à 50 m, verre Ion-X deux fois plus résistant aux rayures"),
    ("Santé", "Fréquence cardiaque, oxygène sanguin, ECG, score de sommeil"),
],
"galaxy-z-flip": [
    ("Format", "Pliant à clapet, se referme sur lui-même"),
    ("Écrans", "Un grand écran intérieur pliable, un écran de couverture à l'extérieur"),
    ("Système", "Android avec l'interface Samsung One UI"),
    ("Réseau", "5G"),
    ("Charge", "USB-C et charge sans fil"),
],
"galaxy-tab-s10": [
    ("Système", "Android avec l'interface Samsung One UI"),
    ("Stylet", "Compatible S Pen"),
    ("Réseau", "Wi-Fi"),
    ("Connectique", "USB-C"),
    ("Usage", "Lecture, cours, vidéo, prise de notes au stylet"),
],
"galaxy-watch": [
    ("Taille", "Boîtier 44 mm"),
    ("Système", "Wear OS, compatible téléphones Android"),
    ("Connectivité", "Bluetooth, ou LTE selon la version choisie"),
    ("Santé", "Fréquence cardiaque, suivi du sommeil, suivi d'activité"),
    ("Charge", "Sans fil, sur socle magnétique"),
],
"joycon": [
    ("Compatibilité", "Nintendo Switch 2"),
    ("Contenu", "Deux manettes, une gauche et une droite"),
    ("Fixation", "Aimantée sur la console, bouton de libération à l'arrière"),
    ("Mode souris", "Capteur optique sur la tranche, utilisable sur une table"),
    ("Vibrations", "HD Rumble 2"),
    ("Autres", "Gyroscope, lecteur NFC pour les amiibo"),
],
"station-charge": [
    ("Compatibilité", "Manettes DualSense, PlayStation 5"),
    ("Capacité", "Deux manettes en même temps"),
    ("Usage", "Recharge sans allumer la console"),
    ("Pose", "Manettes posées sur leurs contacts, sans câble à brancher"),
],
}
