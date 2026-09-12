/* iStore Tech : panier, favoris, page produit.
   Tout vit dans le navigateur du visiteur. Aucun serveur, aucune donnée qui part ailleurs.
   La commande finale part sur WhatsApp, rédigée. */
(function(){
"use strict";

var WA = "221784277229";
var K_PANIER = "ist_panier_v1";
var K_FAV    = "ist_favoris_v1";
var LIVRAISON_DAKAR = 0;

/* ---------- stockage : il peut échouer (navigation privée), jamais planter ---------- */
function lire(k, defaut){
  try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : defaut }
  catch(e){ return defaut }
}
function ecrire(k, v){
  try { localStorage.setItem(k, JSON.stringify(v)); return true }
  catch(e){ return false }
}

function panier(){ var p = lire(K_PANIER, []); return Array.isArray(p) ? p : [] }
function favoris(){ var f = lire(K_FAV, []); return Array.isArray(f) ? f : [] }

function prixDe(prod, stockage){
  var p = prod.prix;
  for (var i=0;i<prod.stockages.length;i++){
    if (prod.stockages[i][0] === stockage) p += prod.stockages[i][1];
  }
  return p;
}
function fmt(n){ return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " F" }

function cle(id, couleur, stockage){ return id + "|" + (couleur||"") + "|" + (stockage||"") }

/* ---------- panier ---------- */
function ajouter(id, couleur, stockage, qte){
  var prod = window.CATALOGUE_INDEX[id];
  if (!prod) return false;
  var p = panier(), k = cle(id, couleur, stockage), trouve = false;
  for (var i=0;i<p.length;i++){
    if (cle(p[i].id, p[i].couleur, p[i].stockage) === k){ p[i].qte += qte; trouve = true; break }
  }
  if (!trouve) p.push({id:id, couleur:couleur, stockage:stockage, qte:qte});
  ecrire(K_PANIER, p);
  compteurs();
  return true;
}
function changerQte(k, delta){
  var p = panier();
  for (var i=0;i<p.length;i++){
    if (cle(p[i].id, p[i].couleur, p[i].stockage) === k){
      p[i].qte += delta;
      if (p[i].qte < 1) p.splice(i,1);
      break;
    }
  }
  ecrire(K_PANIER, p); compteurs(); return p;
}
function retirer(k){
  var p = panier().filter(function(l){ return cle(l.id,l.couleur,l.stockage) !== k });
  ecrire(K_PANIER, p); compteurs(); return p;
}
function totalPanier(){
  var t = 0, p = panier();
  for (var i=0;i<p.length;i++){
    var prod = window.CATALOGUE_INDEX[p[i].id];
    if (prod) t += prixDe(prod, p[i].stockage) * p[i].qte;
  }
  return t;
}
function nbArticles(){
  return panier().reduce(function(a,l){ return a + l.qte }, 0);
}

/* ---------- favoris ---------- */
function estFavori(id){ return favoris().indexOf(id) !== -1 }
function basculerFavori(id){
  var f = favoris(), i = f.indexOf(id);
  if (i === -1) f.push(id); else f.splice(i,1);
  ecrire(K_FAV, f); compteurs();
  return i === -1;
}

/* ---------- compteurs dans la barre du haut ---------- */
/* La pastille est un chiffre posé sur une icône : à la lecture vocale elle
   arrive détachée de ce qu'elle compte, ou pas du tout quand elle est masquée.
   Le nombre est donc écrit dans le libellé du lien lui-même, qui est la seule
   chose qu'un lecteur d'écran annonce de façon fiable sur un bouton sans texte. */
function motArticles(n){
  return n === 0 ? "vide" : (n === 1 ? "1 article" : n + " articles");
}
function motFavoris(n){
  return n === 0 ? "aucun favori" : (n === 1 ? "1 favori" : n + " favoris");
}
function compteurs(){
  var n = nbArticles(), nf = favoris().length;
  var cp = document.querySelectorAll("[data-compteur-panier]");
  for (var i=0;i<cp.length;i++){
    cp[i].textContent = n;
    cp[i].hidden = n === 0;
    var lienP = cp[i].closest ? cp[i].closest("a") : null;
    if (lienP) lienP.setAttribute("aria-label", "Mon panier, " + motArticles(n));
  }
  var cf = document.querySelectorAll("[data-compteur-favoris]");
  for (var j=0;j<cf.length;j++){
    cf[j].textContent = nf;
    cf[j].hidden = nf === 0;
    var lienF = cf[j].closest ? cf[j].closest("a") : null;
    if (lienF) lienF.setAttribute("aria-label", "Mes favoris, " + motFavoris(nf));
  }
}

/* ---------- petit message de confirmation ---------- */
var toastT = null;
function toast(txt, lien){
  var el = document.getElementById("toast");
  if (!el){
    el = document.createElement("div");
    el.id = "toast"; el.className = "toast"; el.setAttribute("role","status");
    document.body.appendChild(el);
  }
  el.innerHTML = "";
  var s = document.createElement("span"); s.textContent = txt; el.appendChild(s);
  if (lien){
    var a = document.createElement("a"); a.href = lien.href; a.textContent = lien.txt; el.appendChild(a);
  }
  el.classList.add("on");
  clearTimeout(toastT);
  toastT = setTimeout(function(){ el.classList.remove("on") }, 4000);
}

/* ---------- message WhatsApp depuis le panier ---------- */
function messageCommande(paiement){
  var p = panier(), l = ["Bonjour iStore Tech, je voudrais commander :",""];
  for (var i=0;i<p.length;i++){
    var prod = window.CATALOGUE_INDEX[p[i].id];
    if (!prod) continue;
    var d = [];
    if (p[i].couleur) d.push(p[i].couleur);
    if (p[i].stockage) d.push(p[i].stockage);
    l.push("- " + prod.nom + (d.length ? " (" + d.join(", ") + ")" : "") +
           " x" + p[i].qte + " : " + fmt(prixDe(prod, p[i].stockage) * p[i].qte));
  }
  l.push("");
  l.push("Total : " + fmt(totalPanier()));
  if (paiement) l.push("Paiement : " + paiement);
  return l.join("\n");
}

/* ---------- rendu : page produit ---------- */
function rendreProduit(){
  var hote = document.getElementById("produit");
  if (!hote) return;
  var id = new URLSearchParams(location.search).get("id");
  var prod = window.CATALOGUE_INDEX[id];

  if (!prod){
    hote.innerHTML = '<div class="vide"><h1>Ce produit n\'existe plus.</h1>' +
      '<p>Il a peut-être changé de nom ou de page.</p>' +
      '<a class="btn btn-1" href="index.html">Retour à l\'accueil</a></div>';
    return;
  }

  document.title = prod.nom + " · iStore Tech Dakar";
  var d = document.querySelector('meta[name="description"]');
  if (d) d.setAttribute("content", prod.nom + " " + prod.sub + " à Dakar. " +
      (prod.note || "") + " Livraison 24h, paiement à la réception.");

  var visuel = prod.img
    ? '<img src="assets/produits/' + prod.img + '" alt="' + prod.nom + ', ' + prod.sub + '.">'
    : '<span class="sil" role="img" aria-label="' + prod.nom + ', illustration technique en attendant la photo">' +
      (window.SILHOUETTES[prod.sil] || "") + '</span>';

  var cat = window.CATS_INDEX[prod.cat] || {nom:"Boutique", url:"index.html"};

  var h = [];
  h.push('<nav class="crumb" aria-label="Fil d\'Ariane"><a href="index.html">Accueil</a> <span aria-hidden="true">/</span> <a href="' + cat.url + '">' + cat.nom + '</a> <span aria-hidden="true">/</span> <span>' + prod.nom + '</span></nav>');
  h.push('<div class="pgrid">');
  h.push('  <div class="pvis">' + visuel + '<span class="sceau-mini" aria-hidden="true">Scellé</span></div>');
  h.push('  <div class="pinfo">');
  h.push('    <span class="badge">' + prod.badge + '</span>');
  h.push('    <h1>' + prod.nom + '</h1>');
  h.push('    <p class="psub">' + prod.sub + ' · ' + prod.etat + '</p>');
  if (prod.note) h.push('    <p class="pnote2">' + prod.note + '</p>');
  h.push('    <p class="pprix" id="pprix">' + fmt(prod.prix) + '</p>');

  if (prod.couleurs.length > 1){
    h.push('    <fieldset class="opt"><legend>Couleur</legend><div class="opts" id="opt-couleur">');
    for (var i=0;i<prod.couleurs.length;i++){
      h.push('<label class="chip2"><input type="radio" name="couleur" value="' + prod.couleurs[i] + '"' + (i===0?' checked':'') + '><span>' + prod.couleurs[i] + '</span></label>');
    }
    h.push('</div></fieldset>');
  }
  if (prod.stockages.length > 1){
    h.push('    <fieldset class="opt"><legend>Capacité</legend><div class="opts" id="opt-stockage">');
    for (var j=0;j<prod.stockages.length;j++){
      h.push('<label class="chip2"><input type="radio" name="stockage" value="' + prod.stockages[j][0] + '"' + (j===0?' checked':'') + '><span>' + prod.stockages[j][0] + '</span></label>');
    }
    h.push('</div></fieldset>');
  }

  h.push('    <div class="achat">');
  h.push('      <div class="qte" role="group" aria-label="Quantité">');
  h.push('        <button type="button" class="qbtn" id="q-moins" aria-label="Enlever un">&minus;</button>');
  h.push('        <output class="qval" id="q-val" aria-live="polite">1</output>');
  h.push('        <button type="button" class="qbtn" id="q-plus" aria-label="Ajouter un">+</button>');
  h.push('      </div>');
  h.push('      <button type="button" class="btn btn-1" id="ajout">Ajouter au panier</button>');
  h.push('      <button type="button" class="btn btn-fav" id="fav" aria-pressed="false">' + coeur() + '<span>Favori</span></button>');
  h.push('    </div>');
  h.push('    <ul class="prass">');
  h.push('      <li>Neuf, scellé d\'origine. Le film n\'a pas été ouvert.</li>');
  h.push('      <li>Tu paies à la réception : Wave, Orange Money ou espèces.</li>');
  h.push('      <li>Livraison en 24h partout au Sénégal.</li>');
  h.push('      <li>Garantie 2 ans, portée par la boutique à Sacré-Cœur 3.</li>');
  h.push('    </ul>');

  /* Les caractéristiques. Une liste de définitions et non un tableau : c'est
     une suite d'étiquettes et de valeurs, pas des données croisées, et une dl
     se lit correctement à la voix comme au doigt. */
  if (prod.fiche && prod.fiche.length){
    h.push('    <section class="specs" aria-labelledby="specs-t">');
    h.push('      <h2 id="specs-t">Caractéristiques</h2>');
    h.push('      <dl>');
    for (var f = 0; f < prod.fiche.length; f++){
      h.push('        <div><dt>' + prod.fiche[f][0] + '</dt><dd>' + prod.fiche[f][1] + '</dd></div>');
    }
    h.push('      </dl>');
    h.push('    </section>');
  }
  h.push('  </div>');
  h.push('</div>');
  hote.innerHTML = h.join("\n");

  var qte = 1;
  var qv = document.getElementById("q-val");
  function couleur(){ var e = hote.querySelector('input[name="couleur"]:checked'); return e ? e.value : (prod.couleurs[0] || "") }
  function stockage(){ var e = hote.querySelector('input[name="stockage"]:checked'); return e ? e.value : (prod.stockages.length ? prod.stockages[0][0] : "") }
  function majPrix(){ document.getElementById("pprix").textContent = fmt(prixDe(prod, stockage()) * qte) }

  // La photo suit le coloris choisi. Quand ce coloris n'a pas encore sa photo,
  // on revient a la photo par defaut ET on dit lequel est montre : laisser la
  // photo du coloris precedent ferait croire au client qu'il commande celui-la.
  function majVisuel(){
    var c = couleur();
    var imgs = prod.images || {};
    var f = imgs[c] || prod.img;
    if (!f) return;

    var boite = hote.querySelector(".pvis");
    var img = boite.querySelector("img");
    if (!img){
      var sil = boite.querySelector(".sil");
      if (sil) sil.remove();
      img = document.createElement("img");
      boite.insertBefore(img, boite.firstChild);
    }
    if (img.getAttribute("src") !== "assets/produits/" + f){
      img.setAttribute("src", "assets/produits/" + f);
    }

    // quel coloris la photo montre-t-elle vraiment
    var montre = null;
    for (var k in imgs){ if (imgs[k] === f){ montre = k; break } }
    img.setAttribute("alt", prod.nom + (montre ? ", " + montre : "") + ".");

    var note = boite.querySelector(".photonote");
    if (montre && montre !== c){
      if (!note){
        note = document.createElement("p");
        note.className = "photonote mono";
        boite.appendChild(note);
      }
      note.textContent = "Photo du coloris " + montre + ". " + c + " disponible en boutique.";
    } else if (note){
      note.remove();
    }
  }

  document.getElementById("q-moins").addEventListener("click", function(){ if (qte>1){ qte--; qv.textContent = qte; majPrix() } });
  document.getElementById("q-plus").addEventListener("click", function(){ if (qte<20){ qte++; qv.textContent = qte; majPrix() } });
  var radios = hote.querySelectorAll('input[type="radio"]');
  for (var r=0;r<radios.length;r++) radios[r].addEventListener("change", function(){ majPrix(); majVisuel() });
  majVisuel();

  document.getElementById("ajout").addEventListener("click", function(){
    ajouter(prod.id, couleur(), stockage(), qte);
    toast(qte + " × " + prod.nom + " au panier.", {href:"panier.html", txt:"Voir le panier"});
  });

  var bf = document.getElementById("fav");
  function majFav(){
    var on = estFavori(prod.id);
    bf.setAttribute("aria-pressed", on ? "true" : "false");
    bf.querySelector("span").textContent = on ? "Dans les favoris" : "Favori";
  }
  majFav();
  bf.addEventListener("click", function(){
    var on = basculerFavori(prod.id); majFav();
    toast(on ? prod.nom + " ajouté aux favoris." : prod.nom + " retiré des favoris.",
          on ? {href:"favoris.html", txt:"Voir les favoris"} : null);
  });
}

function coeur(){
  return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M12 20s-7-4.6-7-9.6A4.4 4.4 0 0 1 12 7a4.4 4.4 0 0 1 7 3.4c0 5-7 9.6-7 9.6z"/></svg>';
}

/* ---------- rendu : panier ---------- */
function rendrePanier(){
  var hote = document.getElementById("panier");
  if (!hote) return;
  var p = panier();

  if (!p.length){
    hote.innerHTML = '<div class="vide"><h1>Ton panier est vide.</h1>' +
      '<p>Ajoute ce qui te plaît, tu confirmes la commande sur WhatsApp juste après.</p>' +
      '<a class="btn btn-1" href="index.html">Voir la boutique</a></div>';
    return;
  }

  var h = ['<h1>Ton panier</h1>', '<div class="pangrid">', '<div class="panlist">'];
  for (var i=0;i<p.length;i++){
    var prod = window.CATALOGUE_INDEX[p[i].id];
    if (!prod) continue;
    var k = cle(p[i].id, p[i].couleur, p[i].stockage);
    var det = [];
    if (p[i].couleur) det.push(p[i].couleur);
    if (p[i].stockage) det.push(p[i].stockage);
    var vis = prod.img
      ? '<img src="assets/produits/' + prod.img + '" alt="">'
      : '<span class="sil" aria-hidden="true">' + (window.SILHOUETTES[prod.sil] || "") + '</span>';
    h.push('<article class="panline" data-k="' + k + '">');
    h.push('  <a class="panvis" href="produit.html?id=' + prod.id + '">' + vis + '</a>');
    h.push('  <div class="pantxt">');
    h.push('    <h2><a href="produit.html?id=' + prod.id + '">' + prod.nom + '</a></h2>');
    h.push('    <p class="mono">' + (det.join(" · ") || prod.sub) + '</p>');
    h.push('    <button type="button" class="lien-sup" data-sup="' + k + '">Retirer</button>');
    h.push('  </div>');
    h.push('  <div class="qte" role="group" aria-label="Quantité">');
    h.push('    <button type="button" class="qbtn" data-moins="' + k + '" aria-label="Enlever un">&minus;</button>');
    h.push('    <output class="qval">' + p[i].qte + '</output>');
    h.push('    <button type="button" class="qbtn" data-plus="' + k + '" aria-label="Ajouter un">+</button>');
    h.push('  </div>');
    h.push('  <p class="panprix">' + fmt(prixDe(prod, p[i].stockage) * p[i].qte) + '</p>');
    h.push('</article>');
  }
  h.push('</div>');

  h.push('<aside class="recap">');
  h.push('  <h2>Récapitulatif</h2>');
  h.push('  <dl><dt>Sous-total</dt><dd id="soustotal">' + fmt(totalPanier()) + '</dd>');
  h.push('  <dt>Livraison</dt><dd>Offerte</dd></dl>');
  h.push('  <p class="rectotal"><span>Total</span><b id="total">' + fmt(totalPanier()) + '</b></p>');
  h.push('  <fieldset class="opt"><legend>Paiement à la réception</legend><div class="opts">');
  h.push('    <label class="chip2"><input type="radio" name="paiement" value="Wave" checked><span>Wave</span></label>');
  h.push('    <label class="chip2"><input type="radio" name="paiement" value="Orange Money"><span>Orange Money</span></label>');
  h.push('    <label class="chip2"><input type="radio" name="paiement" value="Espèces à la livraison"><span>Espèces</span></label>');
  h.push('  </div></fieldset>');
  h.push('  <a class="btn btn-1 btn-full" id="commander" href="#">Commander sur WhatsApp</a>');
  h.push('  <p class="recnote">Tu ne paies rien maintenant. On confirme le stock et l\'heure de livraison sur WhatsApp, et tu paies quand tu as l\'appareil en main.</p>');
  h.push('</aside>');
  h.push('</div>');
  hote.innerHTML = h.join("\n");

  if (!hote.dataset.lie){
    hote.dataset.lie = "1";
    hote.addEventListener("click", function(e){
      var t = e.target.closest ? e.target.closest("[data-moins],[data-plus],[data-sup]") : null;
      if (!t) return;
      if (t.hasAttribute("data-moins")) changerQte(t.getAttribute("data-moins"), -1);
      else if (t.hasAttribute("data-plus")) changerQte(t.getAttribute("data-plus"), 1);
      else retirer(t.getAttribute("data-sup"));
      rendrePanier();
    });
  }

  function majLien(){
    var e = hote.querySelector('input[name="paiement"]:checked');
    var lien = document.getElementById("commander");
    if (!lien) return;
    lien.href = "https://wa.me/" + WA + "?text=" + encodeURIComponent(messageCommande(e ? e.value : ""));
    lien.target = "_blank"; lien.rel = "noopener";
  }
  if (!hote.dataset.liePaie){
    hote.dataset.liePaie = "1";
    hote.addEventListener("change", function(e){
      if (e.target && e.target.name === "paiement") majLien();
    });
  }
  majLien();
}

/* ---------- rendu : favoris ---------- */
function rendreFavoris(){
  var hote = document.getElementById("favoris");
  if (!hote) return;
  var f = favoris();

  if (!f.length){
    hote.innerHTML = '<div class="vide"><h1>Aucun favori pour l\'instant.</h1>' +
      '<p>Le cœur sur une fiche produit garde l\'article ici, même si tu fermes le site.</p>' +
      '<a class="btn btn-1" href="index.html">Voir la boutique</a></div>';
    return;
  }

  var h = ['<h1>Tes favoris</h1>', '<div class="grid">'];
  for (var i=0;i<f.length;i++){
    var prod = window.CATALOGUE_INDEX[f[i]];
    if (!prod) continue;
    h.push(carteHTML(prod, true));
  }
  h.push('</div>');
  hote.innerHTML = h.join("\n");

  if (!hote.dataset.lie){
    hote.dataset.lie = "1";
    hote.addEventListener("click", function(e){
      var t = e.target.closest ? e.target.closest("[data-defav]") : null;
      if (!t) return;
      basculerFavori(t.getAttribute("data-defav"));
      rendreFavoris();
    });
  }
}

function carteHTML(prod, avecRetrait){
  var vis = prod.img
    ? '<img src="assets/produits/' + prod.img + '" alt="' + prod.nom + ', ' + prod.sub + '." loading="lazy">'
    : '<span class="sil" role="img" aria-label="' + prod.nom + ', illustration technique en attendant la photo">' + (window.SILHOUETTES[prod.sil] || "") + '</span>';
  return '<article class="card">' +
    '<a class="pic" href="produit.html?id=' + prod.id + '">' + vis + '</a>' +
    '<span class="badge">' + prod.badge + '</span>' +
    '<h3><a href="produit.html?id=' + prod.id + '">' + prod.nom + '</a></h3>' +
    '<p class="var">' + prod.sub + '</p>' +
    '<p class="price">À partir de ' + fmt(prod.prix) + '</p>' +
    (avecRetrait
      ? '<button type="button" class="add add-out" data-defav="' + prod.id + '">Retirer des favoris</button>'
      : '<a class="add" href="produit.html?id=' + prod.id + '">Choisir</a>') +
    '</article>';
}

/* ---------- démarrage ---------- */
function init(){
  compteurs();
  rendreProduit();
  rendrePanier();
  rendreFavoris();
  // le panier peut changer dans un autre onglet
  window.addEventListener("storage", function(e){
    if (e.key === K_PANIER || e.key === K_FAV){ compteurs(); rendrePanier(); rendreFavoris() }
  });
}
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
else init();

window.ISTORE = {ajouter:ajouter, basculerFavori:basculerFavori, estFavori:estFavori,
                 compteurs:compteurs, toast:toast, fmt:fmt, carteHTML:carteHTML};
})();
