# iStore Tech Dakar

Boutique en ligne d'une vraie boutique de Dakar. Site statique, dix pages, aucun serveur.

## L'essentiel

| | |
|---|---|
| **Marque** | iStore Tech (le logo dit iStore Tech, pas iStore Dakar) |
| **Métier** | Revendeur. Neuf scellé. L'occasion est l'exception, annoncée sur la fiche. |
| **Boutique** | Sacré-Cœur 3, Dakar. Lundi au samedi, 9h à 19h. |
| **WhatsApp** | +221 78 427 72 29 |
| **Livraison** | 24h partout au Sénégal |
| **Paiement** | Wave, Orange Money, espèces, à la réception |
| **Garantie** | 2 ans, portée par la boutique |

## Le postulat

Le marché de Dakar est plein de copies avec des boîtes parfaitement imitées. La première question de chaque acheteur, c'est : est-ce que c'est un vrai. La réponse d'iStore Tech n'est pas « on l'a ouvert et vérifié », c'est **« personne ne l'a ouvert avant toi »**. Le film d'origine est la preuve.

Les trois peurs des acheteurs, trouvées dans la recherche, et la réponse du site :

| La peur | La réponse |
|---|---|
| « C'est peut-être une copie » | Scellé, tu ouvres la boîte toi-même à la livraison |
| « Je ne veux pas payer d'avance » | Wave, Orange Money ou espèces, à la réception |
| « La livraison va traîner » | 24h, l'heure est confirmée avant que tu valides |

## La technique

HTML, CSS et JavaScript à la main. Pas de framework, pas d'étape de compilation, pas de dépendance à installer. Un dossier, des fichiers, ça marche.

```
project site apple/
├── catalogue.py          <- LA SOURCE. 62 produits, prix, couleurs, capacités.
├── build-pages.py        <- génère le catalogue JS et les 10 pages
├── serve.js              <- serveur d'aperçu local (node serve.js)
├── img/produits/         <- photos sources (jpg/png), hors livraison
└── istore-dakar/         <- LE SITE À METTRE EN LIGNE
    ├── index.html
    ├── iphone-apple.html · samsung-android.html · gaming.html
    ├── machines.html · audio.html · accessoires.html
    ├── produit.html · panier.html · favoris.html
    └── assets/
        ├── site.css      <- tout le style, partagé
        ├── site.js       <- comportements partagés
        ├── shop.js       <- panier, favoris, fiche produit
        ├── catalogue.js  <- généré, ne pas modifier à la main
        ├── frames/       <- 240 images du héros, le film du défilement
        ├── hero-poster.jpg · hero-ending.jpg
        └── produits/     <- photos en WebP
```

Une seule dépendance externe : **Lenis**, chargé depuis un CDN, qui adoucit le
défilement. Le site fonctionne entièrement sans lui ; il n'est même installé que
si l'animation du navigateur répond vraiment.

## Le héros

Le film de 10 secondes n'est pas une vidéo posée dans la page : il est découpé en
240 images et redessiné dans un canvas à chaque position de défilement. Une vidéo
qu'on déplace au scroll doit chercher son image, ce qui impose une file d'attente
et de la latence. Le canvas peint directement la bonne image.

Les six légendes sont calées sur les six paliers du film, trouvés par la mesure et
non à l'œil. Les valeurs sont dans `memory.md` : ne pas les réinventer.

Pour changer le film : remplacer les images de `assets/frames/`, remesurer les
paliers, puis ajuster les bornes `data-a` et `data-b` des bandes dans
`build-pages.py`.

## Modifier le catalogue

Un prix, une couleur, un produit : tout est dans `catalogue.py`. Ensuite :

```bash
python build-pages.py
```

Les dix pages se régénèrent. Ne jamais modifier `assets/catalogue.js` à la main, il est écrasé à chaque génération.

## Ajouter une photo

1. Déposer l'image dans `img/produits/`
2. La convertir en WebP, largeur maximale 900 px, qualité 82
3. Renseigner le nom du fichier dans la fiche du produit dans `catalogue.py`
4. Relancer `python build-pages.py`

La conversion divise le poids par dix environ. Sur de la data mobile à Dakar, c'est la différence entre un site qui s'ouvre et un site qu'on abandonne.

## Voir le site

```bash
node serve.js
```

Puis ouvrir `http://localhost:4173/` dans un navigateur.

## Le design

Noir et blanc, le blanc domine. Pas de troisième couleur. Le noir est l'accent : boutons, titres, repères. Le fond de page est `#FAFAF8`, un cheveu sous le blanc pur, parce qu'un grand aplat de blanc pur éblouit.

Les photos produit gardent leurs vraies couleurs : l'acheteur doit voir la couleur de ce qu'il commande.

- **Clash Display** 600/700 : titres
- **Satoshi** 400/500/700 : corps, boutons
- **JetBrains Mono** 400/500 : prix, références, badges

## Le parcours d'achat

1. **Tu choisis.** Couleur, capacité, quantité. Le prix se met à jour en direct.
2. **On confirme.** Le panier part sur WhatsApp, déjà rédigé.
3. **Tu paies à la réception.** Wave, Orange Money ou espèces.

Le panier et les favoris vivent dans le navigateur du visiteur (`localStorage`). Rien ne part sur un serveur, il n'y en a pas. La validation ouvre WhatsApp avec le détail de la commande.

## La règle de la copie

Zéro tiret cadratin. Zéro mot creux. Aucune promesse que la boutique ne peut pas tenir. Sur un site qui vend de la confiance, une phrase fausse coûte plus cher qu'une phrase moche.
