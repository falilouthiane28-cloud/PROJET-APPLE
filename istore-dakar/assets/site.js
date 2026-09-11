/* iStore Tech : comportements partagés par toutes les pages. */
(function(){
"use strict";

var WA_NUMBER = "221784277229";
var WA_TEXT   = "Bonjour iStore Tech, je cherche ";

function rng(seed){ var s=seed>>>0; return function(){ s=(s*1664525+1013904223)>>>0; return s/4294967296 } }

/* ---------- liens WhatsApp ---------- */
function liensWA(){
  var links = document.querySelectorAll("a.wa");
  for (var i=0;i<links.length;i++){
    var a = links[i], t = WA_TEXT;
    var carte = a.closest ? a.closest(".card") : null;
    var cat   = a.closest ? a.closest(".cat")  : null;
    if (carte && carte.querySelector("h3")) t = WA_TEXT + carte.querySelector("h3").textContent.trim();
    else if (cat && cat.querySelector("h3")) t = WA_TEXT + cat.querySelector("h3").textContent.trim();
    a.href = "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(t);
    a.target = "_blank"; a.rel = "noopener";
  }
}

/* ---------- poussière de fond ---------- */
function poussiere(){
  var hote = document.getElementById("dust");
  if (!hote) return;
  // 8 et non 26. Chaque grain est une couche composée qui tourne en boucle sans
  // jamais s'arrêter, et la règle est un élément vivant par section, à peine
  // perceptible. Vingt-six grains coûtaient de la mémoire pour un effet que
  // personne ne compte.
  var r = rng(20260909), n = window.innerWidth < 720 ? 5 : 8, html = "";
  for (var i=0;i<n;i++){
    var d = 16 + r()*26, delay = -r()*d, x = r()*100;
    html += '<i style="left:' + x.toFixed(2) + '%;animation-duration:' + d.toFixed(1) +
            's;animation-delay:' + delay.toFixed(1) + 's"></i>';
  }
  hote.innerHTML = html;
}

/* ---------- pilule de navigation ---------- */
function pilule(){
  var box = document.getElementById("navlinks"), pill = document.getElementById("navpill");
  if (!box || !pill) return;
  var links = box.querySelectorAll("a");
  function bouge(el){
    pill.style.width = el.offsetWidth + "px";
    pill.style.transform = "translateX(" + el.offsetLeft + "px)";
    pill.style.opacity = "1";
  }
  for (var i=0;i<links.length;i++){
    links[i].addEventListener("mouseenter", function(e){ bouge(e.currentTarget) });
    links[i].addEventListener("focus", function(e){ bouge(e.currentTarget) });
  }
  box.addEventListener("mouseleave", function(){ pill.style.opacity = "0" });
  box.addEventListener("focusout", function(){
    if (!box.contains(document.activeElement)) pill.style.opacity = "0";
  });
  var actif = box.querySelector("a.on");
  if (actif) bouge(actif);
}

/* ---------- entrées au scroll ---------- */
function entrees(){
  if (!("IntersectionObserver" in window)) {
    var tous = document.querySelectorAll(".rise,.st,.rule,.plan");
    for (var t=0;t<tous.length;t++) tous[t].classList.add("in");
    return;
  }
  var io = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if (!e.isIntersecting) return;
      var el = e.target;
      el.classList.add("in");
      if (el.classList.contains("st")) setTimeout(function(){ el.classList.add("done") }, 1400);
      io.unobserve(el);
    });
  }, {rootMargin:"0px 0px -12% 0px", threshold:.12});
  var cibles = document.querySelectorAll(".rise,.st,.rule,.plan");
  for (var i=0;i<cibles.length;i++) io.observe(cibles[i]);
}

/* ---------- le film du héros : le défilement pilote les images ----------
   Rendu image par image dans un canvas, et non par déplacement d'une vidéo.
   Une vidéo qu'on déplace au scroll doit chercher son image : cela impose une
   file d'attente, un verrou, et une latence. Ici chaque position de défilement
   peint directement la bonne image. 240 images WebP pèsent 4,2 Mo contre 3,6 Mo
   pour la vidéo : un studio blanc se compresse très bien, donc la fluidité ne
   coûte presque rien. */
function film(){
  var cv    = document.getElementById("film-canvas");
  var stage = document.querySelector(".stage");
  var hote  = document.getElementById("bands");
  var zone  = document.querySelector(".hero");
  if (!cv || !stage || !hote || !zone) return;

  /* 120 images à 1152 px, et non 240 à 1920. Le canvas n'affiche que 1088 px de
     large : une source plus grande ne se voit pas et coûte cher. Décodées, 240
     images à 1920 px occupaient deux gigaoctets de mémoire, ce qui suffisait à
     faire ramer toute la page d'accueil. Là c'est 358 Mo, et 1 Mo sur le réseau
     au lieu de 4. */
  var NB_IMAGES = 120;
  var CHEMIN    = "assets/frames/f_";
  var POSTER    = "assets/hero-poster.jpg";
  var PAGE      = "#FAFAF8";
  var PREMIERES = 12;        // assez pour peindre sans attendre le reste

  var ctx    = cv.getContext("2d", { alpha: false });
  var ring   = stage.querySelector(".ring");
  var plate  = stage.querySelector(".plate");
  var bandes = [].slice.call(hote.querySelectorAll(".band"));

  var images = new Array(NB_IMAGES);
  var chargees = 0;
  var vue = 0, montre = 0, rafId = null, dernier = 0, minuteur = null;
  var indexAffiche = -1, sourceAffichee = null;
  var aLecran = true, loadK = 0;
  var scrubOn = false, initFait = false, lenis = null;

  /* --- découpage du texte, une seule fois, avec un tirage reproductible --- */
  bandes.forEach(function(b, i){
    b.a = parseFloat(b.dataset.a);
    b.z = parseFloat(b.dataset.b);
    b.ramp = b.dataset.ramp ? parseFloat(b.dataset.ramp) : 0;
    b.spread = b.dataset.spread ? parseFloat(b.dataset.spread) : 0;
    b.op = -1; b.k = -1;
    var cible = b.querySelector("[data-split]");
    if (cible) decouper(cible, b, 9271 + i * 733);
  });

  function decouper(el, bande, graine){
    var mode = el.dataset.split, texte = el.textContent.trim(), r = rng(graine);
    var lu = document.createElement("span");
    lu.className = "sr"; lu.textContent = texte;
    var vu = document.createElement("span");
    vu.setAttribute("aria-hidden", "true");
    var mots = texte.split(" "), total = texte.replace(/ /g, "").length, n = 0;
    for (var mi = 0; mi < mots.length; mi++){
      var w = document.createElement("span");
      w.className = "w";
      if (mode === "word"){
        w.textContent = mots[mi];
        w.style.setProperty("--th", ((mi / mots.length) * 0.55).toFixed(3));
        var cote = mi < mots.length / 2 ? -1 : 1;
        w.style.setProperty("--jx", (cote * (18 + r() * 26)).toFixed(1) + "px");
      } else {
        w.style.setProperty("--th", "0");
        for (var ci = 0; ci < mots[mi].length; ci++){
          var c = document.createElement("span");
          c.className = "c";
          c.textContent = mots[mi][ci];
          var th = bande.spread
            ? (n / Math.max(1, total)) * bande.spread + r() * 0.06
            : r() * 0.55;
          c.style.setProperty("--th", th.toFixed(3));
          c.style.setProperty("--jx", ((r() * 2 - 1) * 30).toFixed(1) + "px");
          c.style.setProperty("--jy", ((r() * 2 - 1) * 26).toFixed(1) + "px");
          c.style.setProperty("--jr", ((r() * 2 - 1) * 16).toFixed(1) + "deg");
          w.appendChild(c);
          n++;
        }
      }
      vu.appendChild(w);
      if (mi < mots.length - 1) vu.appendChild(document.createTextNode(" "));
    }
    el.textContent = "";
    el.appendChild(lu);
    el.appendChild(vu);
  }

  /* --- progression 0 à 1 dans la zone épinglée --- */
  /* La position du héros est mesurée une fois, au chargement et au
     redimensionnement. Interroger la mise en page à chaque image de défilement
     force le navigateur à tout recalculer au pire moment, et c'est une cause
     classique de saccade. */
  var zoneHaut = 0, zoneCourse = 1;
  function mesureZone(){
    var y = window.scrollY || window.pageYOffset || 0;
    var r = zone.getBoundingClientRect();
    zoneHaut = r.top + y;
    zoneCourse = Math.max(1, r.height - window.innerHeight);
  }
  function progression(){
    var y = (window.scrollY || window.pageYOffset || 0) - zoneHaut;
    return Math.min(1, Math.max(0, y / zoneCourse));
  }

  /* --- le rendu ---
     La vitesse est linéaire. La skill propose d'accélérer les images pour que le
     produit finisse de se former vers 55% du défilement, ce qui vaut pour un
     produit qui s'assemble puis reste en place. Ici le film enchaîne six
     appareils, chacun avec son palier mesuré : accélérer écraserait les paliers
     sous le seuil de lisibilité du test de molette. */
  function indexPour(p){
    return Math.max(0, Math.min(NB_IMAGES - 1, Math.round(p * (NB_IMAGES - 1))));
  }

  function dessine(i){
    var img = images[i];
    if (!img){                                  // pas encore là : la plus proche
      for (var d = 1; d < NB_IMAGES; d++){
        if (i - d >= 0 && images[i - d]){ img = images[i - d]; break }
        if (i + d < NB_IMAGES && images[i + d]){ img = images[i + d]; break }
      }
    }
    if (!img) return;
    if (i === indexAffiche && img === sourceAffichee) return;   // rien n'a changé
    indexAffiche = i; sourceAffichee = img;

    // Le canvas fait exactement la taille du film : un seul dessin, aucune
    // lecture de mise en page, aucun dégradé. C'est ce qui tient les 60 i/s.
    ctx.drawImage(img, 0, 0, cv.width, cv.height);
  }

  function taille(){
    // Plafonné à 1,5 : à 2, un écran 1920 fait redessiner huit millions de
    // pixels par image, ce qui suffit à faire tomber le défilement sous 60 i/s.
    // Sur une photo, l'écart de netteté entre 1,5 et 2 ne se voit pas.
    var d = Math.min(1.5, window.devicePixelRatio || 1);
    var r = plate.getBoundingClientRect();
    var w = Math.round(r.width), h = Math.round(r.height);
    if (!w || !h) return;
    cv.width = Math.round(w * d); cv.height = Math.round(h * d);
    // Un canvas opaque jamais peint est NOIR. On le peint donc à la couleur de
    // la page avant toute chose, sinon un héros sans images vire au noir.
    ctx.fillStyle = PAGE;
    ctx.fillRect(0, 0, cv.width, cv.height);
    mesureZone();
    indexAffiche = -1; sourceAffichee = null;
    dessine(indexPour(montre));
  }

  /* --- le dessin ---
     Piège payé ici : Lenis lisse déjà la position de défilement. Lisser une
     seconde fois l'index d'image empilait deux amortissements, et le film
     traînait derrière la molette au lieu de la suivre. Quand Lenis tourne, on
     prend sa position telle quelle. Sans Lenis, on garde un lissage court pour
     que la molette native ne paraisse pas crantée. */
  function tick(now){
    if (lenis){
      // Relire la position au moment du dessin, pas à l'arrivée de l'événement :
      // Lenis a bougé entre les deux, et dessiner l'ancienne valeur ajoute une
      // image de retard. La lecture est gratuite, la mesure étant en cache.
      vue = progression();
      montre = vue; rafId = null; dernier = 0;
    } else {
      var dt = Math.min(100, now - (dernier || now));
      dernier = now;
      montre += (vue - montre) * (1 - Math.pow(1 - 0.34, dt / 16.667));
      if (Math.abs(vue - montre) < 0.0005){ montre = vue; rafId = null; dernier = 0 }
      else rafId = requestAnimationFrame(tick);
    }
    dessine(indexPour(montre));
    majBandes(montre);
  }

  /* Filet déjà payé une fois sur ce projet : requestAnimationFrame ne se
     déclenche pas sur une page qui ne peint pas (onglet d'arrière-plan, panneau
     d'aperçu). Sans ce minuteur, le film resterait bloqué sur sa première image
     pendant que le visiteur défile. Le lissage est perdu, la justesse non. */
  function auScroll(){
    vue = progression();
    if (rafId === null && aLecran){ dernier = 0; rafId = requestAnimationFrame(tick) }
    if (minuteur === null) minuteur = setTimeout(secours, 220);
  }
  function secours(){
    minuteur = null;
    if (Math.abs(vue - montre) < 0.0005) return;
    montre = vue;
    dessine(indexPour(montre));
    majBandes(montre);
  }

  function lissePas(p, e0, e1){
    var t = Math.min(1, Math.max(0, (p - e0) / (e1 - e0)));
    return t * t * (3 - 2 * t);
  }

  function majBandes(p){
    for (var i = 0; i < bandes.length; i++){
      var b = bandes[i], a = b.a, z = b.z;
      var f = Math.min(0.02, (z - a) / 3);
      // la première ouvre déjà posée, la dernière ne repart jamais
      var op = (i === 0 ? 1 : lissePas(p, a, a + f))
             * (i === bandes.length - 1 ? 1 : 1 - lissePas(p, z - f, z));
      var ramp = b.ramp || Math.min(0.025, (z - a) * 0.35);
      var k = Math.min(1, Math.max(0, (p - a) / ramp));
      if (i === 0) k = Math.max(k, loadK);
      if (Math.abs(op - b.op) > 0.004){ b.op = op; b.style.opacity = op.toFixed(3) }
      if (Math.abs(k - b.k) > 0.008){ b.k = k; b.style.setProperty("--k", k.toFixed(3)) }
    }
  }

  /* --- la première bande s'assemble au chargement puis rend la main au scroll --- */
  function rampeChargement(){
    var t0 = performance.now();
    (function pas(now){
      loadK = Math.min(1, (now - t0) / 900);
      majBandes(montre);
      if (loadK < 1) requestAnimationFrame(pas);
    })(t0);
    setTimeout(function(){ loadK = 1; majBandes(montre) }, 1000);
  }

  /* --- le chargement des images : les premières tout de suite, le reste ensuite --- */
  function url(i){
    var n = String(i + 1);
    while (n.length < 4) n = "0" + n;
    return CHEMIN + n + ".webp";
  }
  function charge(i){
    return new Promise(function(fini){
      var im = new Image();
      im.decoding = "async";
      function pret(){ images[i] = im; compte(); fini() }
      // On ne décode d'avance que les premières images, celles qu'il faut
      // peindre tout de suite. Forcer le décodage des 120 épinglait tout en
      // mémoire et rendait la page lourde. Les autres se décodent toutes seules,
      // sans bloquer le fil principal, et si l'une n'est pas prête le dessin
      // reprend l'image voisine déjà chargée.
      im.onload  = function(){
        if (i < PREMIERES && im.decode) im.decode().then(pret, pret); else pret();
      };
      im.onerror = function(){ compte(); fini() };
      im.src = url(i);
    });
  }
  function compte(){
    chargees++;
    if (ring) ring.style.setProperty("--ld", Math.round(126 * (1 - chargees / NB_IMAGES)));
  }
  function precharge(){
    var premiers = [];
    for (var i = 0; i < PREMIERES; i++) premiers.push(charge(i));
    Promise.all(premiers).then(function(){
      // Si rien n'est arrivé, l'affiche fixe garde le héros et les légendes
      // continuent de défiler par-dessus : la page reste entière.
      var aucune = true;
      for (var q = 0; q < PREMIERES; q++) if (images[q]){ aucune = false; break }
      if (aucune){
        stage.classList.add("film-rate");
        if (ring) ring.style.opacity = "0";
        return;
      }
      dessine(indexPour(montre));
      stage.classList.add("film-pret");
      var j = PREMIERES;
      (function suite(){
        if (j >= NB_IMAGES){ if (ring) ring.style.opacity = "0"; return }
        var lot = [];
        for (var k = 0; k < 8 && j < NB_IMAGES; k++, j++) lot.push(charge(j));
        Promise.all(lot).then(function(){ dessine(indexPour(montre)); suite() });
      })();
    });
  }

  /* Lenis adoucit le défilement lui-même. Il tourne sur requestAnimationFrame,
     et ce projet a déjà payé le fait que rAF ne tourne pas sur une page qui ne
     peint pas. On ne l'installe donc que si rAF répond vraiment : sinon Lenis
     avalerait la molette sans jamais faire défiler la page. */
  /* Lenis prend la molette à sa charge. Si sa boucle s'arrête alors que le
     visiteur continue de faire tourner la molette, la page ne défile plus du
     tout : c'est le pire défaut possible, bien pire qu'un héros figé. Dès que
     la molette bouge sans que la boucle ait battu depuis une demi-seconde, on
     rend la main au défilement natif. */
  var battement = 0;
  window.addEventListener("wheel", function(){
    if (!lenis || !battement) return;
    if (performance.now() - battement < 500) return;
    try { lenis.destroy() } catch(e){}
    lenis = null;
    document.documentElement.classList.remove("lenis", "lenis-smooth", "lenis-scrolling");
    auScroll();
  }, { passive: true });

  /* Mettre à false pour revenir au défilement natif du navigateur, qui répond
     instantanément mais sans inertie. Un seul mot à changer. */
  var LISSAGE = true;

  function tenteLenis(){
    if (!LISSAGE) return;
    if (typeof window.Lenis !== "function") return;
    if (matchMedia("(prefers-reduced-motion:reduce)").matches) return;
    var vivant = false;
    requestAnimationFrame(function(){ vivant = true });
    setTimeout(function(){
      if (!vivant || lenis || !scrubOn) return;
      try {
        // 0,42 et non 1,2. La skill propose 1,2, mais c'est écrit pour une page
        // vitrine qu'on parcourt lentement. Ici c'est une boutique : au-delà de
        // 0,5 la page continue de glisser après l'arrêt de la molette et tout
        // paraît répondre en retard.
        lenis = new window.Lenis({
          duration: 0.42, smoothWheel: true, wheelMultiplier: 1.2,
          easing: function(t){ return 1 - Math.pow(1 - t, 3) }
        });
        (function boucle(t){ if (!lenis) return; battement = t; lenis.raf(t); requestAnimationFrame(boucle) })(performance.now());
        lenis.on("scroll", auScroll);
      } catch(e){ lenis = null }
    }, 350);
  }

  function initFilmUneFois(){
    if (initFait) return; initFait = true;
    if (plate) plate.style.backgroundImage = "url('" + POSTER + "')";
    stage.classList.add("plate-on");
    taille();
    precharge();
    rampeChargement();
  }

  /* --- les cinq portes, décidées en direct et non une fois pour toutes --- */
  var PORTES = [
    "(max-width:720px)",
    "(orientation:portrait) and (max-width:1024px)",
    "(orientation:portrait) and (pointer:coarse)",
    "(orientation:landscape) and (pointer:coarse) and (max-height:560px)",
    "(prefers-reduced-motion:reduce)"
  ];
  var MQLS = PORTES.map(function(q){ return matchMedia(q) });

  function activer(){
    if (scrubOn) return; scrubOn = true;
    initFilmUneFois();
    window.addEventListener("scroll", auScroll, { passive: true });
    for (var i = 0; i < bandes.length; i++){ bandes[i].op = -1; bandes[i].k = -1 }
    majBandes(progression());
    auScroll();
    tenteLenis();
  }
  function desactiver(){
    if (!scrubOn) return; scrubOn = false;
    window.removeEventListener("scroll", auScroll);
    if (rafId !== null){ cancelAnimationFrame(rafId); rafId = null }
    if (minuteur !== null){ clearTimeout(minuteur); minuteur = null }
    if (lenis){ try { lenis.destroy() } catch(e){} lenis = null }
  }
  function appliquerMode(){
    var ferme = false;
    for (var i = 0; i < MQLS.length; i++) if (MQLS[i].matches) ferme = true;
    if (ferme) desactiver(); else activer();
  }
  for (var m = 0; m < MQLS.length; m++){
    if (MQLS[m].addEventListener) MQLS[m].addEventListener("change", appliquerMode);
    else if (MQLS[m].addListener) MQLS[m].addListener(appliquerMode);
  }

  /* la boucle ne tourne pas quand le héros est hors de l'écran */
  if ("IntersectionObserver" in window){
    new IntersectionObserver(function(es){
      aLecran = es[0].isIntersecting;
      if (aLecran && scrubOn && rafId === null){ dernier = 0; rafId = requestAnimationFrame(tick) }
    }, { threshold: 0 }).observe(stage);
  }

  window.addEventListener("resize", function(){
    if (!scrubOn) return;
    taille(); auScroll();
  }, { passive: true });

  appliquerMode();
}

/* ---------- FAQ ---------- */
function faq(){
  var f = document.getElementById("faq");
  if (!f) return;
  var qs = f.querySelectorAll(".q");
  for (var i=0;i<qs.length;i++){
    (function(q){
      var b = q.querySelector(".qb"), a = q.querySelector(".qa");
      b.addEventListener("click", function(){
        var ouvert = q.classList.contains("open");
        for (var j=0;j<qs.length;j++){
          qs[j].classList.remove("open");
          qs[j].querySelector(".qa").style.height = "0px";
          qs[j].querySelector(".qb").setAttribute("aria-expanded","false");
        }
        if (!ouvert){
          q.classList.add("open");
          a.style.height = a.firstElementChild.offsetHeight + "px";
          b.setAttribute("aria-expanded","true");
        }
      });
    })(qs[i]);
  }
}

/* ---------- pause hors onglet ---------- */
document.addEventListener("visibilitychange", function(){
  document.body.classList.toggle("paused", document.hidden);
});

/* ---------- mouvement réduit, dans les deux sens ---------- */
function figer(){
  var t = document.querySelectorAll(".rise,.st,.rule,.plan");
  for (var i=0;i<t.length;i++){
    t[i].classList.add("in");
    if (t[i].classList.contains("st")) t[i].classList.add("done");
  }
}
/* Le héros se réarme tout seul : il écoute la même requête parmi ses cinq
   portes, donc rien à faire ici pour lui. */
var rm = matchMedia("(prefers-reduced-motion:reduce)");
function surRM(e){ if (e.matches) figer(); else entrees() }
if (rm.addEventListener) rm.addEventListener("change", surRM);
else if (rm.addListener) rm.addListener(surRM);

/* ---------- démarrage ---------- */
function init(){
  film();
  liensWA();
  poussiere();
  pilule();
  entrees();
  faq();
  if (rm.matches) figer();
  // Deux déclencheurs : la première frame si la page est visible, sinon un
  // minuteur. Sans le second, un onglet ouvert en arrière-plan reste vide.
  function pret(){ document.body.classList.add("ready") }
  requestAnimationFrame(pret);
  setTimeout(pret, 120);
}
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
else init();
})();
