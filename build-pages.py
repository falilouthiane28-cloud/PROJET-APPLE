# -*- coding: utf-8 -*-
"""Genere le catalogue JS et les pages d'iStore Tech depuis catalogue.py.
   python build-pages.py
"""
import io, os, json
import catalogue as C

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "istore-dakar")

# ---------------------------------------------------------------- silhouettes
SIL = {
"phone": '<svg viewBox="0 0 120 160" aria-hidden="true"><rect x="34" y="10" width="52" height="140" rx="9" class="sl-a"/><rect x="41" y="20" width="38" height="118" rx="4" class="sl-b"/><rect x="52" y="13" width="16" height="4" rx="2" class="sl-c"/><rect x="42" y="24" width="22" height="22" rx="5" class="sl-b"/><circle cx="49" cy="31" r="4" class="sl-b"/><circle cx="57" cy="39" r="4" class="sl-b"/></svg>',
"console": '<svg viewBox="0 0 120 160" aria-hidden="true"><rect x="30" y="24" width="60" height="112" rx="8" class="sl-a"/><rect x="38" y="24" width="12" height="112" class="sl-b"/><path d="M30 74h60" class="sl-b"/><rect x="62" y="112" width="20" height="4" rx="2" class="sl-c"/><circle cx="72" cy="96" r="3" class="sl-c"/></svg>',
"pad": '<svg viewBox="0 0 120 160" aria-hidden="true"><path d="M28 62c-8 14-12 34-6 44 6 10 16 4 22-6h32c6 10 16 16 22 6 6-10 2-30-6-44-6-10-18-12-32-12s-26 2-32 12z" class="sl-a"/><circle cx="44" cy="80" r="8" class="sl-b"/><path d="M44 74v12M38 80h12" class="sl-c"/><circle cx="78" cy="76" r="3.4" class="sl-b"/><circle cx="86" cy="84" r="3.4" class="sl-b"/><circle cx="70" cy="84" r="3.4" class="sl-b"/><circle cx="78" cy="92" r="3.4" class="sl-b"/><circle cx="52" cy="100" r="6" class="sl-b"/><circle cx="70" cy="100" r="6" class="sl-b"/></svg>',
"switch": '<svg viewBox="0 0 120 160" aria-hidden="true"><rect x="38" y="44" width="44" height="72" rx="4" class="sl-a"/><path d="M38 52c-8 0-12 4-12 12v40c0 8 4 12 12 12z" class="sl-a"/><path d="M82 52c8 0 12 4 12 12v40c0 8-4 12-12 12z" class="sl-a"/><circle cx="32" cy="70" r="4" class="sl-b"/><circle cx="88" cy="70" r="4" class="sl-b"/><path d="M88 92v6M85 95h6" class="sl-c"/><rect x="44" y="52" width="32" height="56" rx="2" class="sl-b"/></svg>',
"laptop": '<svg viewBox="0 0 160 120" aria-hidden="true"><rect x="30" y="24" width="100" height="62" rx="5" class="sl-a"/><rect x="37" y="31" width="86" height="48" rx="2" class="sl-b"/><path d="M14 96h132l-8 8H22z" class="sl-a"/><path d="M66 96h28" class="sl-c"/></svg>',
"audio": '<svg viewBox="0 0 120 160" aria-hidden="true"><path d="M30 92V74a30 30 0 0 1 60 0v18" class="sl-a"/><rect x="20" y="86" width="20" height="38" rx="9" class="sl-a"/><rect x="80" y="86" width="20" height="38" rx="9" class="sl-a"/><rect x="25" y="94" width="10" height="22" rx="5" class="sl-b"/><rect x="85" y="94" width="10" height="22" rx="5" class="sl-b"/></svg>',
"tablet": '<svg viewBox="0 0 120 160" aria-hidden="true"><rect x="24" y="18" width="72" height="124" rx="8" class="sl-a"/><rect x="31" y="26" width="58" height="108" rx="3" class="sl-b"/><circle cx="60" cy="22" r="1.6" class="sl-c"/></svg>',
"watch": '<svg viewBox="0 0 120 160" aria-hidden="true"><rect x="38" y="52" width="44" height="56" rx="12" class="sl-a"/><rect x="45" y="59" width="30" height="42" rx="7" class="sl-b"/><path d="M46 52V34a8 8 0 0 1 8-8h12a8 8 0 0 1 8 8v18M46 108v18a8 8 0 0 0 8 8h12a8 8 0 0 0 8-8v-18" class="sl-a"/><rect x="82" y="68" width="5" height="12" rx="2.5" class="sl-c"/></svg>',
"acc": '<svg viewBox="0 0 120 160" aria-hidden="true"><circle cx="60" cy="80" r="30" class="sl-a"/><circle cx="60" cy="80" r="18" class="sl-b"/><path d="M60 110v26" class="sl-a"/><path d="M54 136h12" class="sl-c"/></svg>',
"screen": '<svg viewBox="0 0 160 120" aria-hidden="true"><rect x="18" y="16" width="124" height="72" rx="5" class="sl-a"/><rect x="25" y="23" width="110" height="58" rx="2" class="sl-b"/><path d="M80 88v14M58 102h44" class="sl-a"/></svg>',
"keyboard": '<svg viewBox="0 0 160 120" aria-hidden="true"><rect x="16" y="38" width="128" height="46" rx="6" class="sl-a"/><g class="sl-b"><rect x="26" y="46" width="12" height="10" rx="2"/><rect x="42" y="46" width="12" height="10" rx="2"/><rect x="58" y="46" width="12" height="10" rx="2"/><rect x="74" y="46" width="12" height="10" rx="2"/><rect x="90" y="46" width="12" height="10" rx="2"/><rect x="106" y="46" width="12" height="10" rx="2"/><rect x="122" y="46" width="12" height="10" rx="2"/><rect x="26" y="62" width="28" height="10" rx="2"/><rect x="58" y="62" width="44" height="10" rx="2"/><rect x="106" y="62" width="28" height="10" rx="2"/></g></svg>',
"mouse": '<svg viewBox="0 0 120 160" aria-hidden="true"><rect x="38" y="42" width="44" height="76" rx="22" class="sl-a"/><path d="M60 42v22" class="sl-b"/><rect x="56" y="52" width="8" height="14" rx="4" class="sl-c"/></svg>',
}

PAGES_META = {
 "iphone":  dict(fichier="iphone-apple.html", kicker="Catalogue · 01",
   h1="iPhone, et tout ce qui va avec.",
   lede="Neufs, sous film, jamais ouverts. Tu choisis la couleur et la capacité, on confirme le stock sur WhatsApp.",
   meta="iPhone 16, 16 Pro, 16 Pro Max, Apple Watch et iPad à Dakar. Neufs et scellés, paiement à la réception, livraison 24h."),
 "android": dict(fichier="samsung-android.html", kicker="Catalogue · 02",
   h1="Galaxy, et tout l'Android sérieux.",
   lede="La gamme S pour le haut du panier, la gamme A pour ce qui dure. Tous scellés, tous garantis deux ans.",
   meta="Samsung Galaxy S25, S24, gamme A et tablettes à Dakar. Neufs et scellés, paiement à la réception, livraison 24h."),
 "gaming":  dict(fichier="gaming.html", kicker="Catalogue · 03",
   h1="PlayStation, Switch, et tout le reste.",
   lede="Consoles, manettes et accessoires, dans leur emballage d'origine. On confirme le stock avant que tu bouges.",
   meta="PlayStation 5, Nintendo Switch, Xbox, manettes et accessoires à Dakar. Neufs et scellés, livraison 24h, paiement à la réception."),
 "machines":dict(fichier="machines.html", kicker="Catalogue · 04",
   h1="Les machines qui travaillent, et celles qui jouent.",
   lede="MacBook pour produire, PC gamer pour encaisser les images par seconde. Scellés, garantis deux ans.",
   meta="MacBook Air, MacBook Pro, PC gamer, écrans et périphériques à Dakar. Neufs et scellés, livraison 24h au Sénégal."),
 "audio":   dict(fichier="audio.html", kicker="Catalogue · 05",
   h1="Ce qui se juge à l'oreille.",
   lede="Écouteurs, casques et enceintes d'origine, sous blister. Le faux AirPods se repère au son : ici la question ne se pose pas.",
   meta="AirPods, casques et enceintes à Dakar. Produits d'origine scellés, garantie 2 ans, livraison 24h."),
 "acc":     dict(fichier="accessoires.html", kicker="Catalogue · 06",
   h1="Les petites pièces qui cassent tout.",
   lede="Un mauvais chargeur tue une batterie en six mois. Un mauvais câble tue un port. Ici, que du certifié.",
   meta="Chargeurs, câbles, coques, batteries et accessoires certifiés à Dakar. Livraison 24h partout au Sénégal."),
}

NAV = [("index.html","Accueil")] + [(u,n.split(" &")[0]) for k,n,u in C.CATS]

def esc(t):
    return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def nav_html(active):
    return "".join('\n      <a href="%s"%s>%s</a>' % (u, ' class="on" aria-current="page"' if u==active else "", esc(l))
                   for u,l in NAV)

def menu_html(active):
    """Les memes liens que la barre, mais en pleine largeur pour le doigt."""
    return "".join('\n      <a href="%s"%s>%s</a>'
                   % (u, ' class="on" aria-current="page"' if u == active else "", esc(l))
                   for u, l in NAV)

def fmt(n):
    s = str(n); out=""
    while len(s)>3: out = " "+s[-3:]+out; s = s[:-3]
    return (s+out).strip()+" F"

_DIMS = {}
def dims(nom):
    """Dimensions reelles de l'image, lues une fois. Sans width et height sur la
       balise, le navigateur ne reserve pas la place et la page saute quand
       l'image arrive : c'est la cause la plus frequente d'un decalage de mise
       en page au chargement."""
    if nom in _DIMS: return _DIMS[nom]
    try:
        from PIL import Image
        with Image.open(os.path.join(OUT, "assets", "produits", nom)) as im:
            _DIMS[nom] = im.size
    except Exception:
        _DIMS[nom] = (None, None)
    return _DIMS[nom]

def carte(p):
    if p["img"]:
        w, h = dims(p["img"])
        taille = ' width="%d" height="%d"' % (w, h) if w else ''
        vis = '<img src="assets/produits/%s" alt="%s, %s."%s loading="lazy" decoding="async">' % (
              p["img"], esc(p["nom"]), esc(p["sub"]), taille)
    else:
        vis = '<span class="sil" role="img" aria-label="%s, illustration technique en attendant la photo">%s</span>' % (esc(p["nom"]), SIL.get(p["sil"], SIL["acc"]))
    return '''        <article class="card">
          <a class="pic" href="produit.html?id=%s">%s</a>
          <span class="badge">%s</span>
          <h3><a href="produit.html?id=%s">%s</a></h3>
          <p class="var">%s</p>
          <p class="price">À partir de %s</p>
          <a class="add" href="produit.html?id=%s">Choisir</a>
        </article>''' % (p["id"], vis, esc(p["badge"]), p["id"], esc(p["nom"]), esc(p["sub"]), fmt(p["prix"]), p["id"])

HEAD = '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{meta}">
<meta name="theme-color" content="#FAFAF8">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23FAFAF8'/%3E%3Ccircle cx='16' cy='16' r='9' fill='none' stroke='%230B0C0E' stroke-width='1.8'/%3E%3Cpath d='M12 16.3l2.7 2.7L20 13' fill='none' stroke='%230B0C0E' stroke-width='1.8'/%3E%3C/svg%3E">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{meta}">
<meta property="og:type" content="website">
<!-- DEPLOY STEP : remplacer par l'URL live -->
<meta property="og:url" content="https://REMPLACER-AU-DEPLOIEMENT/{fichier}">
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=clash-display@600,700&f[]=satoshi@400,500,700&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/site.css">
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js" defer></script>
<script src="assets/catalogue.js" defer></script>
<script src="assets/site.js" defer></script>
<script src="assets/shop.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Aller au contenu</a>
<div class="env" aria-hidden="true"><div class="dust" id="dust"></div></div>
'''

HEADER = '''<header class="nav" role="banner">
  <nav class="navin" aria-label="Navigation principale">
    <a class="brand" href="index.html" aria-label="iStore Tech, accueil">
      <img src="assets/logo-istore-tech.png" alt="iStore Tech" width="52" height="32">
    </a>
    <div class="navlinks" id="navlinks">
      <span class="navpill" id="navpill" aria-hidden="true"></span>{nav}
    </div>
    <div class="navtools">
      <a class="navic" href="favoris.html" aria-label="Mes favoris">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 20s-7-4.6-7-9.6A4.4 4.4 0 0 1 12 7a4.4 4.4 0 0 1 7 3.4c0 5-7 9.6-7 9.6z"/></svg>
        <span class="pastille" data-compteur-favoris hidden>0</span>
      </a>
      <a class="navic" href="panier.html" aria-label="Mon panier">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 7h13l-1.4 9.3a2 2 0 0 1-2 1.7H9.4a2 2 0 0 1-2-1.7L6 7z"/><path d="M6 7L5.2 4H3"/><circle cx="10" cy="21" r="1"/><circle cx="16" cy="21" r="1"/></svg>
        <span class="pastille" data-compteur-panier hidden>0</span>
      </a>
      <a class="navcta wa" href="#" aria-label="Commander sur WhatsApp">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" width="15" height="15"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.5 14.1c-.2.7-1.3 1.3-1.8 1.3-.5.1-1 .1-1.7-.1-.4-.1-.9-.3-1.5-.6-2.7-1.2-4.4-3.9-4.5-4.1-.1-.2-1.1-1.4-1.1-2.7 0-1.3.7-1.9.9-2.2.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2 0 .4-.1.5l-.3.4c-.1.1-.3.3-.1.6.1.3.6 1.1 1.4 1.8 1 .9 1.8 1.1 2 1.2.3.1.4.1.6-.1l.8-.9c.2-.2.4-.2.6-.1l1.8.9c.2.1.4.2.4.3.1.2.1.7-.1 1.4Z"/></svg>
        <span class="ctatxt">WhatsApp</span>
      </a>
      <button class="burger" id="burger" type="button"
              aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu">
        <span class="burger-l" aria-hidden="true"></span>
        <span class="burger-l" aria-hidden="true"></span>
        <span class="burger-l" aria-hidden="true"></span>
      </button>
    </div>
  </nav>

  <div class="menu" id="menu" hidden>
    <nav class="menu-in" aria-label="Menu principal">{menu}
      <a class="menu-cta wa" href="#">Commander sur WhatsApp</a>
    </nav>
  </div>
</header>
'''

RASSURE = '''<section class="sec">
  <div class="wrap">
    <div class="trust st">
      <div class="tcell">
        <svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="4" y="7" width="16" height="13" rx="2"/><path d="M4 11h16M12 7v13"/><path d="M8.5 7L12 3.5 15.5 7"/></svg>
        <span class="mono">01 · Scellé</span>
        <h3>Sous film, jamais ouvert.</h3>
        <p>On revend du neuf d'origine. Quand un appareil est d'occasion, c'est écrit sur sa fiche, en toutes lettres.</p>
      </div>
      <div class="tcell">
        <svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="3"/><path d="M2 10h20M6 15h4"/></svg>
        <span class="mono">02 · Paiement</span>
        <h3>Tu paies quand tu l'as en main.</h3>
        <p>Wave, Orange Money ou espèces, à la livraison. Rien d'avance, aucune carte à saisir.</p>
      </div>
      <div class="tcell">
        <svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 7h11v8H3zM14 10h4l3 3v2h-7z"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/></svg>
        <span class="mono">03 · Livraison</span>
        <h3>24 heures, partout au Sénégal.</h3>
        <p>Dakar comme les régions, au même délai. Tu connais l'heure avant de confirmer.</p>
      </div>
      <div class="tcell">
        <svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 21s-7-4.4-7-10a7 7 0 0 1 14 0c0 5.6-7 10-7 10z"/><circle cx="12" cy="11" r="2.5"/></svg>
        <span class="mono">04 · Garantie</span>
        <h3>Deux ans, et une adresse.</h3>
        <p>La garantie est portée ici, à Sacré-Cœur 3. Tu sais où nous trouver.</p>
      </div>
    </div>
  </div>
</section>
'''

FINAL = '''<section class="sec sec-alt final">
  <div class="wrap rise">
    <h2>Dis-nous ce que tu cherches.</h2>
    <p>Un message, on te répond avec le prix, le stock et le délai. Pas de compte à créer.</p>
    <div class="hrow"><a class="btn btn-1 wa" href="#">Commander sur WhatsApp</a></div>
    <p class="addr">Ou passe nous voir : <b>Sacré-Cœur 3, Dakar</b>. Du lundi au samedi, 9h à 19h.</p>
    <span class="mono">Réponse sous 1h · 7j/7</span>
  </div>
</section>
'''

FOOTER = '''<footer class="foot">
  <div class="wrap">
    <div class="footgrid">
      <div>
        <a class="brand" href="index.html" aria-label="iStore Tech, accueil">
          <img src="assets/logo-istore-tech.png" alt="iStore Tech" width="65" height="40">
        </a>
        <p class="tag">Du scellé, livré en 24h, payé à la réception.</p>
        <p class="tag addr-f">Sacré-Cœur 3, Dakar<br>Lundi au samedi, 9h à 19h<br><a href="https://wa.me/{wa}">+221 78 427 72 29</a></p>
      </div>
      <div>
        <h4>Boutique</h4>
        <ul>
          <li><a href="iphone-apple.html">iPhone &amp; Apple</a></li>
          <li><a href="samsung-android.html">Samsung &amp; Android</a></li>
          <li><a href="gaming.html">Gaming</a></li>
          <li><a href="machines.html">Machines</a></li>
        </ul>
      </div>
      <div>
        <h4>Aussi</h4>
        <ul>
          <li><a href="audio.html">Audio</a></li>
          <li><a href="accessoires.html">Accessoires</a></li>
          <li><a href="favoris.html">Mes favoris</a></li>
          <li><a href="panier.html">Mon panier</a></li>
        </ul>
      </div>
      <div>
        <h4>Paiement</h4>
        <ul>
          <li><a href="index.html#comment">Wave</a></li>
          <li><a href="index.html#comment">Orange Money</a></li>
          <li><a href="index.html#comment">Espèces à la livraison</a></li>
        </ul>
      </div>
      <div>
        <h4>Légal</h4>
        <ul>
          <li><a href="#">Mentions légales</a></li>
          <li><a href="#">Conditions de vente</a></li>
        </ul>
      </div>
    </div>
    <p class="fine">© 2026 iStore Tech. Revendeur indépendant. Non affilié à Apple Inc., Samsung, Sony ou Nintendo. Les marques et visuels produits cités appartiennent à leurs propriétaires respectifs.</p>
  </div>
</footer>
</body>
</html>
'''

CAT_TPL = '''<main id="main" tabindex="-1">

<section class="phead">
  <div class="wrap">
    <nav class="crumb" aria-label="Fil d'Ariane">
      <a href="index.html">Accueil</a> <span aria-hidden="true">/</span> <span>{nom}</span>
    </nav>
    <span class="kick rise">{kicker}</span>
    <h1 class="rise">{h1}</h1>
    <p class="plede rise">{lede}</p>
    <p class="mono pstats rise">{n} références · Neuf scellé · Livraison 24h</p>
  </div>
</section>

<hr class="rule">

<section class="sec sec-paper">
  <div class="wrap">
    <div class="grid st">
{cartes}
    </div>
    <p class="pnote mono">Prix à partir de, hors options. Le prix exact dépend de la capacité et du coloris : choisis-les sur la fiche, ou demande sur WhatsApp.</p>
  </div>
</section>

{rassure}
{final}
</main>
'''

SIMPLE_TPL = '''<main id="main" tabindex="-1">
<section class="phead phead-court">
  <div class="wrap">
    <nav class="crumb" aria-label="Fil d'Ariane">
      <a href="index.html">Accueil</a> <span aria-hidden="true">/</span> <span>{nom}</span>
    </nav>
  </div>
</section>
<section class="sec sec-paper">
  <div class="wrap" id="{hote}"></div>
</section>
{final}
</main>
'''

def js_produit(p):
    return dict(id=p["id"], nom=p["nom"], cat=p["cat"], sub=p["sub"], prix=p["prix"],
                badge=p["badge"], img=p["img"], sil=p["sil"], couleurs=p["couleurs"],
                stockages=[[a,b] for a,b in p["stockages"]], etat=p["etat"], note=p["note"],
                images=p.get("images", {}))


INDEX_TPL = """<main id="main" tabindex="-1">

<h1 class="sr">iStore Tech Dakar : neuf, scellé, livré demain.</h1>

<section class="hero" id="film">
  <div class="stage">

    <div class="canvas-wrap" aria-hidden="true">
      <canvas id="film-canvas"></canvas>
      <div class="plate"></div>
    </div>
    <div class="scrim" aria-hidden="true"></div>

    <svg class="ring" viewBox="0 0 48 48" aria-hidden="true">
      <circle cx="24" cy="24" r="20" fill="none" stroke="currentColor" stroke-width="3"
              stroke-dasharray="126" style="stroke-dashoffset:var(--ld,126)"/>
    </svg>

    <div class="bands" id="bands">

      <div class="scene at-right" id="s1" data-a="0.00" data-b="0.124">
        <div class="scene-in">
          <svg class="mesure" viewBox="0 0 10 200" aria-hidden="true" preserveAspectRatio="none">
            <path class="rline" d="M5 0 V200"/>
            <path class="rtick" d="M0 40 H10 M0 100 H10 M0 160 H10"/>
          </svg>
          <div class="block">
            <span class="kick">001 / Dakar</span>
            <p class="headline" aria-hidden="true">
              <span class="mask"><span class="line">Ça commence</span></span>
              <span class="mask"><span class="line">par un téléphone.</span></span>
            </p>
            <span class="sr">Ça commence par un téléphone.</span>
            <p class="sub">Ça ne s'arrête jamais là.</p>
          </div>
        </div>
      </div>

      <div class="scene at-left" id="s2" data-a="0.175" data-b="0.299">
        <div class="scene-in">
          <svg class="mesure" viewBox="0 0 10 200" aria-hidden="true" preserveAspectRatio="none">
            <path class="rline" d="M5 0 V200"/>
            <path class="rtick" d="M0 40 H10 M0 100 H10 M0 160 H10"/>
          </svg>
          <div class="block">
            <span class="kick">002 / Téléphones</span>
            <p class="headline" aria-hidden="true">
              <span class="mask"><span class="line">iPhone. Samsung.</span></span>
              <span class="mask"><span class="line">Neufs, scellés, garantis.</span></span>
            </p>
            <span class="sr">iPhone. Samsung. Neufs, scellés, garantis.</span>
            <p class="sub">Jamais ouverts avant toi. Le film d'origine en est la preuve.</p>
          </div>
        </div>
      </div>

      <div class="scene at-right" id="s3" data-a="0.351" data-b="0.474">
        <div class="scene-in">
          <svg class="mesure" viewBox="0 0 10 200" aria-hidden="true" preserveAspectRatio="none">
            <path class="rline" d="M5 0 V200"/>
            <path class="rtick" d="M0 40 H10 M0 100 H10 M0 160 H10"/>
          </svg>
          <div class="block">
            <span class="kick">003 / Consoles</span>
            <p class="headline" aria-hidden="true">
              <span class="mask"><span class="line">La même exigence</span></span>
              <span class="mask"><span class="line">au rayon jeu.</span></span>
            </p>
            <span class="sr">La même exigence au rayon jeu.</span>
            <p class="sub">Nintendo, PlayStation, et tout ce qui va avec.</p>
          </div>
        </div>
      </div>

      <div class="scene at-left" id="s4" data-a="0.526" data-b="0.650">
        <div class="scene-in">
          <svg class="mesure" viewBox="0 0 10 200" aria-hidden="true" preserveAspectRatio="none">
            <path class="rline" d="M5 0 V200"/>
            <path class="rtick" d="M0 40 H10 M0 100 H10 M0 160 H10"/>
          </svg>
          <div class="block">
            <span class="kick">004 / Gaming</span>
            <p class="headline" aria-hidden="true">
              <span class="mask"><span class="line h-left">Console. Manette.</span></span>
              <span class="mask"><span class="line h-right">Rien à configurer.</span></span>
            </p>
            <span class="sr">Console. Manette. Rien à configurer.</span>
            <p class="sub">Tu branches, tu joues.</p>
          </div>
        </div>
      </div>

      <div class="scene at-right" id="s5" data-a="0.701" data-b="0.825">
        <div class="scene-in">
          <svg class="mesure" viewBox="0 0 10 200" aria-hidden="true" preserveAspectRatio="none">
            <path class="rline" d="M5 0 V200"/>
            <path class="rtick" d="M0 40 H10 M0 100 H10 M0 160 H10"/>
          </svg>
          <div class="block">
            <span class="kick">005 / Ordinateurs</span>
            <p class="headline" aria-hidden="true">
              <span class="mask"><span class="line">Et de quoi</span></span>
              <span class="mask"><span class="line">travailler dessus.</span></span>
            </p>
            <span class="sr">Et de quoi travailler dessus.</span>
            <p class="sub">MacBook, iPad, accessoires.</p>
          </div>
        </div>
      </div>

      <div class="scene at-left live" id="s6" data-a="0.876" data-b="1">
        <div class="scene-in">
          <svg class="mesure" viewBox="0 0 10 200" aria-hidden="true" preserveAspectRatio="none">
            <path class="rline" d="M5 0 V200"/>
            <path class="rtick" d="M0 40 H10 M0 100 H10 M0 160 H10"/>
          </svg>
          <div class="block">
            <span class="kick">006 / iStore Tech</span>
            <p class="headline" aria-hidden="true">
              <span class="mask"><span class="line">Un seul magasin.</span></span>
              <span class="mask"><span class="line">Tout l'écosystème.</span></span>
            </p>
            <span class="sr">Un seul magasin. Tout l'écosystème.</span>
            <p class="sub">Livraison à Dakar en 24 heures. Garantie deux ans.</p>
            <div class="hrow">
              <a class="btn btn-1" href="#categories">Voir la boutique</a>
              <a class="btn btn-2 wa" href="#">Commander sur WhatsApp</a>
            </div>
          </div>
        </div>
      </div>

    </div>

    <div class="still">
      <img class="stillimg" src="assets/hero-ending.jpg" alt="" width="1920" height="1080" fetchpriority="high">
      <div class="stillin">
        <span class="kick">iStore Tech · Dakar</span>
        <p class="htitle sm">Neuf, scellé, livré demain.</p>
        <p class="hsub">iPhone, Samsung, PlayStation, Switch, MacBook. Tu choisis, on confirme sur WhatsApp, tu paies quand tu l'as en main.</p>
        <div class="hrow">
          <a class="btn btn-1" href="#categories">Voir la boutique</a>
          <a class="btn btn-2 wa" href="#">Commander sur WhatsApp</a>
        </div>
        <span class="mono hdata">Wave · Orange Money · Espèces à la livraison</span>
      </div>
    </div>

  </div>
</section>

<hr class="rule">

<section class="sec" id="comment">
  <div class="wrap">
    <div class="head rise">
      <span class="kick">Comment ça marche</span>
      <h2>Trois étapes, aucune carte à saisir.</h2>
      <p>Pas de compte à créer, pas de paiement en ligne. Tu commandes comme tu écrirais à un ami.</p>
    </div>
    <div class="etapes st">
      <div class="etape">
        <h3>Tu choisis.</h3>
        <p>Couleur, capacité, quantité. Le prix se met à jour sous tes yeux, sans surprise à la fin.</p>
      </div>
      <div class="etape">
        <h3>On confirme.</h3>
        <p>Ton panier part sur WhatsApp, déjà rédigé. On te répond avec le stock et l'heure de livraison.</p>
      </div>
      <div class="etape">
        <h3>Tu paies à la réception.</h3>
        <p>Wave, Orange Money ou espèces, une fois l'appareil dans ta main. Tu peux refuser si ça ne va pas.</p>
      </div>
    </div>
    <div class="paiements rise">
      <span class="paie"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 13c3-4 6 4 9 0s6-4 9 0"/></svg>Wave</span>
      <span class="paie"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M10 18h4"/></svg>Orange Money</span>
      <span class="paie"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/></svg>Espèces à la livraison</span>
    </div>
  </div>
</section>

<section class="sec sec-alt" id="categories">
  <div class="wrap">
    <div class="head rise">
      <span class="kick">Catalogue</span>
      <h2>Ce qu'on garde en boutique.</h2>
      <p>Six familles, {n} références. Tout est neuf et scellé, sauf mention contraire écrite sur la fiche.</p>
    </div>
    <div class="cats st">
{cats}
    </div>
  </div>
</section>

<section class="sec sec-paper" id="selection">
  <div class="wrap">
    <div class="head rise">
      <span class="kick">Sélection</span>
      <h2>Ce qui part le plus vite.</h2>
      <p>Un aperçu. Le catalogue complet est dans les pages par famille.</p>
    </div>
    <div class="grid st">
{tops}
    </div>
  </div>
</section>

{rassure}

<section class="sec sec-alt" id="avis">
  <div class="wrap">
    <div class="head rise">
      <span class="kick">Avis</span>
      <h2>Ce qu'ils disent en sortant.</h2>
    </div>
    <!-- AVIS : remplacer par de vrais avis clients, ou supprimer la section -->
    <div class="avis st">
      <article class="rev">
        <div class="stars" aria-label="5 étoiles sur 5">{etoiles}</div>
        <p>Commandé le matin, livré l'après-midi, payé en Wave à la livraison. Rien à dire.</p>
        <div class="who"><b>Avis à remplacer</b><span class="mono">Date</span></div>
      </article>
      <article class="rev">
        <div class="stars" aria-label="5 étoiles sur 5">{etoiles}</div>
        <p>Le film d'origine était encore dessus. J'ai ouvert la boîte moi-même devant le livreur.</p>
        <div class="who"><b>Avis à remplacer</b><span class="mono">Date</span></div>
      </article>
      <article class="rev">
        <div class="stars" aria-label="5 étoiles sur 5">{etoiles}</div>
        <p>Mon écran a lâché au bout de six mois. Je suis passé à la boutique, réparé sous garantie, sans discuter.</p>
        <div class="who"><b>Avis à remplacer</b><span class="mono">Date</span></div>
      </article>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="head rise">
      <span class="kick">Questions</span>
      <h2>Les vraies questions.</h2>
    </div>
    <div class="faq rise" id="faq">
{faq}
    </div>
  </div>
</section>

{final}
</main>
"""

ETOILE = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 1l2.1 4.3 4.7.7-3.4 3.3.8 4.7L8 11.8 3.8 14l.8-4.7L1.2 6l4.7-.7z"/></svg>'

QUESTIONS = [
 (u"Vos téléphones sont neufs ou d'occasion ?",
  u"Neufs et scellés. C'est ce qu'on vend. Quand un appareil est d'occasion, c'est écrit sur sa fiche en toutes lettres. On ne mélange pas les deux."),
 (u"Comment je sais que c'est un vrai ?",
  u"Le film d'origine n'a pas été ouvert. Tu le vois à la livraison, avant de payer, et tu peux refuser si quelque chose ne va pas."),
 (u"Je paie avant ou après ?",
  u"Après. Wave, Orange Money ou espèces, quand tu as l'appareil en main. Rien à avancer, aucune carte à saisir sur le site."),
 (u"Le prix affiché est-il le prix final ?",
  u"C'est le prix de départ. La capacité et le coloris peuvent le faire monter. Le prix exact s'affiche sur la fiche dès que tu choisis tes options."),
 (u"Vous livrez où et en combien de temps ?",
  u"Partout au Sénégal, en 24 heures. Dakar comme les régions, au même délai."),
 (u"Et si l'appareil tombe en panne ?",
  u"Tu passes à la boutique, à Sacré-Cœur 3. Deux ans de garantie, prise en charge sur place."),
]

CATEGORIES_ACCUEIL = [
 ("iphone-apple.html", "iPhone &amp; Apple", u"Du 15 au 16 Pro Max, Watch et iPad.",
  '<rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 18.5h2"/>'),
 ("samsung-android.html", "Samsung &amp; Android", u"Galaxy S, Galaxy A, tablettes.",
  '<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M10 5h4"/>'),
 ("gaming.html", "Gaming", u"PlayStation, Switch, Xbox, manettes.",
  '<rect x="2" y="6" width="20" height="12" rx="4"/><path d="M7 10v4M5 12h4M16 11.5h.01M18.5 14h.01"/>'),
 ("machines.html", "Machines", u"MacBook, PC gamer, écrans.",
  '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 19h20"/>'),
 ("audio.html", "Audio", u"AirPods, casques, enceintes.",
  '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="2" y="13" width="4.5" height="7" rx="2"/><rect x="17.5" y="13" width="4.5" height="7" rx="2"/>'),
 ("accessoires.html", "Accessoires", u"Chargeurs, câbles, coques certifiés.",
  '<path d="M13 2L5 13h6l-2 9 8-11h-6z"/>'),
]

CARTE_CAT = '      <a class="cat" href="%s">\n        <svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">%s</svg>\n        <h3>%s</h3>\n        <p>%s</p>\n        <span class="go">Voir <svg width="11" height="11" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M2 6h8M6.5 2.5L10 6l-3.5 3.5"/></svg></span>\n      </a>'
CARTE_Q = '      <div class="q">\n        <button class="qb" aria-expanded="false">%s<svg class="qi" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M7 1v12M1 7h12"/></svg></button>\n        <div class="qa"><p>%s</p></div>\n      </div>'

def cartes_categories():
    return "\n".join(CARTE_CAT % (u, ic, n, d) for u, n, d, ic in CATEGORIES_ACCUEIL)

def faq_html():
    return "\n".join(CARTE_Q % (esc(q), esc(r)) for q, r in QUESTIONS)


def main():
    # ---- catalogue.js
    idx = dict((p["id"], js_produit(p)) for p in C.PRODUITS)
    cats = dict((k, dict(nom=n, url=u)) for k,n,u in C.CATS)
    js = ["/* Genere par build-pages.py. Ne pas modifier a la main : editer catalogue.py. */",
          "window.CATALOGUE_INDEX = " + json.dumps(idx, ensure_ascii=False, indent=0) + ";",
          "window.CATS_INDEX = " + json.dumps(cats, ensure_ascii=False) + ";",
          "window.SILHOUETTES = " + json.dumps(SIL, ensure_ascii=False) + ";",
          "window.TOP_PRODUITS = " + json.dumps([p["id"] for p in C.PRODUITS if p["top"]], ensure_ascii=False) + ";"]
    io.open(os.path.join(OUT,"assets","catalogue.js"),"w",encoding="utf-8",newline="").write("\n".join(js)+"\n")

    # ---- pages categorie
    for k, nom, url in C.CATS:
        m = PAGES_META[k]
        prods = C.par_cat(k)
        page = (HEAD.format(titre=esc(nom)+" · iStore Tech Dakar", meta=esc(m["meta"]), fichier=url)
                + HEADER.format(nav=nav_html(url), menu=menu_html(url))
                + CAT_TPL.format(nom=esc(nom), kicker=m["kicker"], h1=esc(m["h1"]),
                                 lede=esc(m["lede"]), n=len(prods),
                                 cartes="\n".join(carte(p) for p in prods),
                                 rassure=RASSURE, final=FINAL)
                + FOOTER.format(wa=C.WA))
        io.open(os.path.join(OUT,url),"w",encoding="utf-8",newline="").write(page)
        print("%-24s %2d produits" % (url, len(prods)))

    # ---- produit / panier / favoris
    for fichier, nom, hote, meta in [
        ("produit.html","Fiche produit","produit","Fiche produit iStore Tech : couleur, capacité, quantité, prix. Paiement à la réception, livraison 24h au Sénégal."),
        ("panier.html","Mon panier","panier","Ton panier iStore Tech. Tu confirmes la commande sur WhatsApp et tu paies à la livraison."),
        ("favoris.html","Mes favoris","favoris","Les produits que tu as mis de côté chez iStore Tech Dakar."),
    ]:
        page = (HEAD.format(titre=esc(nom)+" · iStore Tech Dakar", meta=esc(meta), fichier=fichier)
                + HEADER.format(nav=nav_html(fichier), menu=menu_html(fichier))
                + SIMPLE_TPL.format(nom=esc(nom), hote=hote, final=FINAL)
                + FOOTER.format(wa=C.WA))
        io.open(os.path.join(OUT,fichier),"w",encoding="utf-8",newline="").write(page)
        print("%-24s dynamique" % fichier)

    # ---- accueil
    tops = [p for p in C.PRODUITS if p["top"]]
    accueil = (HEAD.format(titre=u"iStore Tech Dakar \u00b7 Neuf, scell\u00e9, livr\u00e9 demain.",
                           meta=u"iPhone, Samsung, PlayStation, Switch et MacBook \u00e0 Dakar. Neufs et scell\u00e9s, livraison 24h partout au S\u00e9n\u00e9gal, paiement \u00e0 la r\u00e9ception par Wave, Orange Money ou esp\u00e8ces.",
                           fichier="index.html")
               + HEADER.format(nav=nav_html("index.html"), menu=menu_html("index.html"))
               + INDEX_TPL.format(n=len(C.PRODUITS), cats=cartes_categories(),
                                  tops="\n".join(carte(p) for p in tops),
                                  rassure=RASSURE, final=FINAL,
                                  faq=faq_html(), etoiles=ETOILE*5)
               + FOOTER.format(wa=C.WA))
    io.open(os.path.join(OUT, "index.html"), "w", encoding="utf-8", newline="").write(accueil)
    print("%-24s %2d en vitrine" % ("index.html", len(tops)))

    print("\n%d produits au catalogue." % len(C.PRODUITS))
    sans = [p["nom"] for p in C.PRODUITS if not p["img"]]
    print("%d attendent encore une photo." % len(sans))

if __name__ == "__main__":
    main()
