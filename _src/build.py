#!/usr/bin/env python3
"""Builds the multi-page site (EN at /, AR at /ar/, RU at /ru/) from content.py.

Pages per language: home, about, experience, treatments, education, contact.
Run from anywhere:  python3 _src/build.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content import (T, LANGS, LANG_PREFIX, SWITCH_LABEL, SWITCH_NAME, PAGES, SLUG, NEXT,  # noqa: E402
                     PHONE_DISPLAY, PHONE_TEL, WHATSAPP, EMAIL, CV_FILE, SITE)

VERSION = "2"  # bump after editing css/js so browsers fetch the new files

ICONS = {
    "syringe": '<path d="m18 2 4 4"/><path d="m17 7 3-3"/><path d="M19 9 8.7 19.3a2.4 2.4 0 0 1-3.4 0l-.6-.6a2.4 2.4 0 0 1 0-3.4L15 5"/><path d="m9 11 4 4"/><path d="m5 19-3 3"/><path d="m14 4 6 6"/>',
    "light": '<circle cx="12" cy="12" r="3.2"/><path d="M12 2v3M12 19v3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M2 12h3M19 12h3M4.9 19.1 7 17M17 7l2.1-2.1"/>',
    "drop": '<path d="M12 2.8S5.5 9.6 5.5 14.3a6.5 6.5 0 0 0 13 0C18.5 9.6 12 2.8 12 2.8z"/><path d="M9.2 14.8a2.9 2.9 0 0 0 2.8 2.7"/>',
    "stetho": '<path d="M5 3H4v6a5 5 0 0 0 10 0V3h-1"/><path d="M9 14v1.5a6 6 0 0 0 12 0V12"/><circle cx="21" cy="10" r="2"/>',
    "person": '<circle cx="12" cy="7.5" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "check": '<path d="M12 2.5 14.6 4l3 .1 1.5 2.6 2.4 1.7-.5 3 .9 2.8-2 2.3-.6 3-2.9.9-2.2 2-2.8-1-2.8 1-2.2-2-2.9-.9-.6-3-2-2.3.9-2.8-.5-3L4.9 6.7 6.4 4.1l3-.1z"/><path d="m8.5 12.3 2.4 2.4 4.6-4.8"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "chat": '<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/><path d="M9 10.5c.4 1.6 2.4 3.6 4 4l1.3-1.2 1.9.9"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/>',
    "chev": '<path d="m9 5 7 7-7 7"/>',
}


def icon(name, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


CHEV = icon("chev", "chev")

# System fonts first (SF Pro / SF Arabic on Apple devices); web fonts only download where those are missing.
FONTS = {
    "latin": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
    "ar": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700"
          "&family=Inter:wght@400;500;600;700&display=swap",
}

# English pages send first-time Arabic/Russian browsers to the same page in their language.
REDIRECT_JS = ("<script>(function(){try{if(localStorage.getItem('lang'))return;"
               "var l=((navigator.languages&&navigator.languages[0])||navigator.language||'').toLowerCase();"
               "var p=l.indexOf('ar')===0?'/ar':l.indexOf('ru')===0?'/ru':'';"
               "if(p)location.replace(p+location.pathname+location.search+location.hash);}catch(e){}})();</script>")

MOTES = [  # x%, bottom%, size px, duration s, delay s, drift px
    (8, 18, 5, 9, 0, 14), (16, 30, 3, 7, 2.5, -10), (24, 10, 4, 10, 5, 8), (78, 22, 5, 8, 1, -12),
    (86, 12, 3, 9.5, 3.5, 10), (92, 34, 4, 7.5, 6, -8), (50, 8, 3, 11, 4, 6), (64, 16, 4, 8.5, 7, -6),
    (34, 22, 3, 9, 8, 12), (70, 40, 3, 10, 2, -10),
]

PHOTO_POS = {"about": "50% 42%", "experience": "50% 30%", "treatments": "40% 30%"}   # page heroes (4:5)
TILE_POS = {"about": "50% 54%", "experience": "50% 22%", "treatments": "45% 34%"}    # home tiles (wide)


def href(lang, page):
    return "/" + LANG_PREFIX[lang] + SLUG[page]


def cv_href():
    return "/" + CV_FILE


def picture(name, alt, cls="", eager=False, pos=None):
    loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
    pos = pos or PHOTO_POS.get(name, "50% 50%")
    return (f'<picture class="{cls}"><source srcset="/img/{name}.webp" type="image/webp">'
            f'<img src="/img/{name}.jpg" width="960" height="1280" alt="{alt}" {loading} decoding="async" '
            f'style="object-position:{pos}"></picture>')


def stage(alt, eager=True):
    motes = "".join(
        f'<span style="--x:{x}%;--b:{b}%;--s:{s}px;--d:{d}s;--delay:{dl}s;--dx:{dx}px"></span>'
        for x, b, s, d, dl, dx in MOTES
    )
    prio = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f"""<div class="stage">
          <div class="arch" aria-hidden="true"><span class="rays"></span></div>
          <div class="ripples" aria-hidden="true"><i></i><i></i><i></i></div>
          <div class="float-shadow" aria-hidden="true"></div>
          <div class="motes" aria-hidden="true">{motes}</div>
          <picture>
            <source srcset="/img/karina-float.webp" type="image/webp">
            <img class="float" src="/img/karina-float.png" width="944" height="1244" alt="{alt}" {prio} decoding="async">
          </picture>
        </div>"""


# ───────────────────────── shared chrome ─────────────────────────

def head(lang, page):
    t = T[lang]
    title, desc = t["meta"][page]
    url = SITE.rstrip("/") + href(lang, page)
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE.rstrip("/")}{href(l, page)}">' for l in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE.rstrip("/")}{href("en", page)}">'
    og_alt = "\n".join(
        f'<meta property="og:locale:alternate" content="{T[l]["og_locale"]}">' for l in LANGS if l != lang
    )
    fonts = FONTS["ar" if lang == "ar" else "latin"]
    preload = ""
    if page in ("home", "contact"):
        preload = '<link rel="preload" as="image" href="/img/karina-float.webp" type="image/webp" fetchpriority="high">'
    elif page in PHOTO_POS:
        preload = f'<link rel="preload" as="image" href="/img/{page}.webp" type="image/webp">'
    ld = ""
    if page == "home":
        data = {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": "Karina Rauashde",
            "honorificPrefix": "Dr.",
            "alternateName": ["Karina Rawashdeh", "كارينا الرواشدة", "Рауашде Карина Раедовна"],
            "jobTitle": "Dermatologist",
            "worksFor": {"@type": "MedicalClinic", "name": "Ashab Clinics",
                         "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"}},
            "url": SITE,
            "image": SITE + "img/og.jpg",
            "email": "mailto:" + EMAIL,
            "telephone": PHONE_TEL,
            "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"},
            "alumniOf": [
                {"@type": "CollegeOrUniversity", "name": "Volgograd State Medical University"},
                {"@type": "CollegeOrUniversity", "name": "RUDN University"},
            ],
            "hasCredential": {
                "@type": "EducationalOccupationalCredential",
                "name": "SCFHS Professional Classification — Registrar, Dermatology",
                "dateCreated": "2026-11",
                "recognizedBy": {"@type": "Organization", "name": "Saudi Commission for Health Specialties"},
            },
            "knowsLanguage": ["ar", "ru", "en"],
        }
        ld = f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'
    return f"""<!doctype html>
<html lang="{lang}" dir="{t["dir"]}" data-page="{page}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{alternates}
<meta property="og:type" content="profile">
<meta property="og:site_name" content="Dr. Karina Rauashde">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{t["hero_alt"]}">
<meta property="og:locale" content="{t["og_locale"]}">
{og_alt}
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#fbfbfd">
<meta name="color-scheme" content="light">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
{preload}
<link rel="stylesheet" href="/css/style.css?v={VERSION}">
<script>document.documentElement.classList.add('js')</script>
{REDIRECT_JS if lang == "en" else ""}
{ld}
</head>"""


def lang_switch(lang, page, cls="lang"):
    links = "".join(
        f'<a href="{href(l, page)}" hreflang="{l}" lang="{l}" aria-label="{SWITCH_NAME[l]}"'
        f'{" aria-current=\"true\"" if l == lang else ""}>{SWITCH_LABEL[l]}</a>'
        for l in LANGS
    )
    return f'<div class="{cls}">{links}</div>'


def gnav(lang, page):
    t = T[lang]
    links = "".join(
        f'<a href="{href(lang, p)}"{" aria-current=\"page\"" if p == page else ""}>{t["nav"][p]}</a>'
        for p in PAGES if p != "home"
    )
    menu_links = "".join(
        f'<li style="--i:{i}"><a href="{href(lang, p)}"{" aria-current=\"page\"" if p == page else ""}>{t["nav"][p]}</a></li>'
        for i, p in enumerate(PAGES)
    )
    return f"""<a class="skip" href="#main">{t["skip"]}</a>
<header class="gnav">
  <div class="gnav-inner">
    <a class="brand" href="{href(lang, "home")}"><span class="brand-mark" aria-hidden="true">K</span><span class="brand-name">{t["brand"]}</span></a>
    <nav class="gnav-links" aria-label="{t["menu"]}">{links}</nav>
    {lang_switch(lang, page)}
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu" data-open="{t["menu"]}" data-close="{t["close"]}" aria-label="{t["menu"]}"><span></span><span></span></button>
  </div>
</header>
<nav class="menu" id="menu" aria-label="{t["menu"]}">
  <ul>{menu_links}</ul>
  <a class="menu-cv" href="{cv_href()}" download style="--i:{len(PAGES)}">{icon("download")}{t["cta_cv"]}</a>
</nav>"""


def footer(lang, page):
    t = T[lang]
    pages = "".join(f'<li><a href="{href(lang, p)}">{t["nav"][p]}</a></li>' for p in PAGES)
    contact = (f'<li><a href="tel:{PHONE_TEL}" dir="ltr">{PHONE_DISPLAY}</a></li>'
               f'<li><a href="{WHATSAPP}" target="_blank" rel="noopener">{t["c_whatsapp"]}</a></li>'
               f'<li><a href="mailto:{EMAIL}" dir="ltr">{EMAIL}</a></li>'
               f'<li><a href="{cv_href()}" download>{t["cta_cv"]}</a></li>')
    langs = "".join(
        f'<li><a href="{href(l, page)}" hreflang="{l}" lang="{l}"{" aria-current=\"true\"" if l == lang else ""}>{SWITCH_NAME[l]}</a></li>'
        for l in LANGS
    )
    crumb = f'<a href="{href(lang, "home")}">{t["brand"]}</a>'
    if page != "home":
        crumb += f'{CHEV}<span>{t["nav"][page]}</span>'
    return f"""<footer class="foot">
  <div class="wrap">
    <p class="foot-tag">{t["foot_tagline"]}</p>
    <nav class="crumbs" aria-label="Breadcrumb">{crumb}</nav>
    <div class="foot-dir">
      <div><h2>{t["foot_pages"]}</h2><ul>{pages}</ul></div>
      <div><h2>{t["foot_contact"]}</h2><ul>{contact}</ul></div>
      <div><h2>{t["foot_lang"]}</h2><ul>{langs}</ul></div>
    </div>
    <div class="foot-legal"><p>{t["copyright"]}</p><p dir="ltr">karina.rauashde.com</p></div>
  </div>
</footer>
<script src="/js/main.js?v={VERSION}" defer></script>
</body>
</html>
"""


def next_link(lang, page):
    if page not in NEXT:
        return ""
    t = T[lang]
    n = NEXT[page]
    return f"""
  <section class="next-wrap">
    <div class="wrap">
      <a class="next reveal" href="{href(lang, n)}"><span class="next-k">{t["next"]}</span><span class="next-t">{t["nav"][n]}{CHEV}</span></a>
    </div>
  </section>"""


def phero(title, lead, media, extra=""):
    return f"""
  <section class="phero">
    <div class="wrap phero-grid">
      <div class="phero-copy">
        <h1 class="phero-title hero-in" style="--i:0">{title}</h1>
        <p class="phero-lead hero-in" style="--i:1">{lead}</p>{extra}
      </div>
      <div class="phero-media hero-in" style="--i:2">{media}</div>
    </div>
  </section>"""


def ctas(lang, big=False):
    t = T[lang]
    return (f'<div class="ctas{" ctas-big" if big else ""}">'
            f'<a class="btn" href="{href(lang, "contact")}">{t["cta_contact"]}</a>'
            f'<a class="btn btn-outline" href="{cv_href()}" download>{t["cta_cv"]}</a></div>')


def license_card(lang, tag="h2"):
    t = T[lang]
    return f"""<div class="lic">
          <div class="lic-top"><span class="lic-seal">{icon("check")}</span><span class="lic-k">{t["lic_label"]}</span><span class="lic-date">{t["lic_date"]}</span></div>
          <p class="lic-issuer">{t["lic_issuer"]}</p>
          <{tag} class="lic-name">{t["lic_name"]}</{tag}>
          <p class="lic-rank">{t["lic_rank"]}</p>
        </div>"""


# ───────────────────────── pages ─────────────────────────

def body_home(lang):
    t = T[lang]
    stats = "".join(f'<li><b dir="ltr">{n}</b><span>{label}</span></li>' for n, label in t["stats"])

    def tile_photo(p):
        title, sub = t["tiles"][p]
        alt = {"about": t["about_alt"], "experience": t["exp_alt"], "treatments": t["tr_alt"]}[p]
        return f"""
      <a class="tile tile-photo reveal" href="{href(lang, p)}">
        <div class="tile-copy"><h2 class="tile-title">{title}</h2><p class="tile-sub">{sub}</p><span class="more">{t["more"]}{CHEV}</span></div>
        {picture(p, alt, "tile-media", pos=TILE_POS[p])}
      </a>"""

    edu_title, edu_sub = t["tiles"]["education"]
    c_title, c_sub = t["tiles"]["contact"]
    return f"""
<main id="main">
  <section class="hero">
    <div class="hero-glow" aria-hidden="true"></div>
    <div class="wrap hero-copy">
      <p class="eyebrow hero-in" style="--i:0">{t["hero_eyebrow"]}</p>
      <h1 class="hero-title hero-in" style="--i:1">{t["hero_title"]}</h1>
      <p class="hero-sub hero-in" style="--i:2">{t["hero_sub"]}</p>
      <div class="hero-in" style="--i:3">{ctas(lang)}</div>
    </div>
    <div class="hero-visual hero-in" style="--i:2">
      <div class="parallax">
        {stage(t["hero_alt"])}
      </div>
    </div>
  </section>

  <section class="band band-dark">
    <div class="wrap">
      <div class="band-head reveal">
        <p class="eyebrow">{t["glance_label"]}</p>
        <h2 class="headline">{t["glance_title"]}</h2>
      </div>
      <ul class="stats reveal">{stats}</ul>
    </div>
  </section>

  <section class="tiles-wrap" aria-label="{t["menu"]}">
    <div class="tiles">{tile_photo("about")}{tile_photo("experience")}{tile_photo("treatments")}
      <a class="tile tile-license reveal" href="{href(lang, "education")}">
        <div class="tile-copy"><h2 class="tile-title">{edu_title}</h2><p class="tile-sub">{edu_sub}</p><span class="more">{t["more"]}{CHEV}</span></div>
        <div class="lic-art" aria-hidden="true">
          <span class="lic-art-seal">{icon("check")}</span>
          <b>{t["lic_tile_rank"]}</b>
          <span>{t["lic_tile_field"]} · SCFHS</span>
        </div>
      </a>
      <div class="tile tile-contact reveal">
        <div class="tile-copy">
          <h2 class="tile-title">{c_title}</h2><p class="tile-sub">{c_sub}</p>
          {ctas(lang)}
        </div>
      </div>
    </div>
  </section>
</main>"""


def body_about(lang):
    t = T[lang]
    paras = "".join(f"<p>{p}</p>" for p in t["about_p"])
    features = "".join(f"""
        <li class="feature reveal">{icon(ic)}<h3>{title}</h3><p>{text}</p></li>""" for ic, title, text in t["approach"])
    langs = "".join(
        f'<li class="reveal"><span class="lb-native" lang="{code}" dir="{"rtl" if code == "ar" else "ltr"}">{native}</span>'
        f'<span class="lb-label">{label}</span></li>'
        for native, label, code in t["langs"]
    )
    return f"""
<main id="main">{phero(t["about_title"], t["about_lead"], picture("about", t["about_alt"], "photo", eager=True))}

  <section class="section">
    <div class="wrap narrow">
      <p class="intro-big reveal">{t["about_intro"]}</p>
      <div class="prose reveal">{paras}</div>
    </div>
  </section>

  <section class="section gray">
    <div class="wrap">
      <div class="sec-head reveal">
        <p class="eyebrow">{t["approach_label"]}</p>
        <h2 class="headline">{t["approach_title"]}</h2>
      </div>
      <ul class="features">{features}
      </ul>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal"><p class="eyebrow">{t["langs_label"]}</p></div>
      <ul class="langs-big">{langs}</ul>
    </div>
  </section>
{next_link(lang, "about")}
</main>"""


def body_experience(lang):
    t = T[lang]
    jobs = []
    for e in t["exp"]:
        now = f'<span class="badge-now"><i></i>{t["now"]}</span>' if e.get("current") else ""
        desc = f'<p class="job-desc">{e["desc"]}</p>' if e["desc"] else ""
        bullets = ("<ul class=\"job-list\">" + "".join(f"<li>{b}</li>" for b in e["bullets"]) + "</ul>") if e["bullets"] else ""
        chips = ""
        if e["chips"]:
            chips = ('<div class="chips">' + "".join(f'<span class="chip">{c}</span>' for c in e["chips"]) + "</div>"
                     f'<a class="link" href="{href(lang, "treatments")}">{t["exp_see_all"]}{CHEV}</a>')
        jobs.append(f"""
        <li class="job reveal{" is-current" if e.get("current") else ""}">
          <div class="job-when"><span class="job-period">{e["period"]}</span><span class="job-place">{icon("pin")}{e["place"]}</span></div>
          <div class="job-body">{now}
            <h2 class="job-org">{e["org"]}</h2>
            <p class="job-role">{e["role"]}</p>
            {desc}{bullets}{chips}
          </div>
        </li>""")
    return f"""
<main id="main">{phero(t["exp_title"], t["exp_lead"], picture("experience", t["exp_alt"], "photo", eager=True))}

  <section class="section gray">
    <div class="wrap">
      <ol class="jobs">{"".join(jobs)}
      </ol>
    </div>
  </section>
{next_link(lang, "experience")}
</main>"""


def body_treatments(lang):
    t = T[lang]
    seg = "".join(f'<a href="#{cid}">{title}</a>' for cid, _, title, _, _ in t["proc"])
    cats = []
    for n, (cid, ic, title, intro, items) in enumerate(t["proc"]):
        lis = []
        for name, detail in items:
            if "IPL" in name:
                lis.append(f"""
          <li class="item item-feature reveal">
            <span class="item-badge">{icon("check")}{t["ipl_badge"]}</span>
            <h3>{name}</h3><p>{t["ipl_note"]}</p>
          </li>""")
            else:
                lis.append(f"""
          <li class="item reveal"><h3>{name}</h3>{f"<p>{detail}</p>" if detail else ""}</li>""")
        cats.append(f"""
  <section class="section cat{" gray" if n % 2 == 0 else ""}" id="{cid}">
    <div class="wrap">
      <div class="cat-head reveal">
        <span class="cat-icon">{icon(ic)}</span>
        <h2 class="headline">{title}</h2>
        <p class="sub">{intro}</p>
      </div>
      <ul class="items">{"".join(lis)}
      </ul>
    </div>
  </section>""")
    return f"""
<main id="main">{phero(t["tr_title"], t["tr_lead"], picture("treatments", t["tr_alt"], "photo", eager=True))}
  <nav class="seg" aria-label="{t["tr_jump"]}"><div class="seg-inner">{seg}</div></nav>
{"".join(cats)}
{next_link(lang, "treatments")}
</main>"""


def body_education(lang):
    t = T[lang]
    edu = "".join(f"""
        <li class="edu-card reveal">
          <span class="edu-period">{period}</span>
          <h3 class="edu-org">{org}</h3>
          <p class="edu-prog">{prog}</p>
          <p class="edu-place">{icon("pin")}{place}</p>
        </li>""" for period, org, prog, place in t["edu"])
    return f"""
<main id="main">{phero(t["edu_title"], t["edu_lead"], license_card(lang))}

  <section class="section gray">
    <div class="wrap">
      <div class="sec-head reveal"><h2 class="headline">{t["edu_label"]}</h2></div>
      <ol class="edu">{edu}
      </ol>
    </div>
  </section>
{next_link(lang, "education")}
</main>"""


def body_contact(lang):
    t = T[lang]
    return f"""
<main id="main">{phero(t["c_title"], t["c_lead"], stage(t["hero_alt"]))}

  <section class="section gray">
    <div class="wrap">
      <div class="cgrid">
        <a class="ccard reveal" href="tel:{PHONE_TEL}">{icon("phone")}<span class="k">{t["c_phone"]}</span><span class="v" dir="ltr">{PHONE_DISPLAY}</span></a>
        <a class="ccard reveal" href="{WHATSAPP}" target="_blank" rel="noopener">{icon("chat")}<span class="k">{t["c_whatsapp"]}</span><span class="v">{t["c_whatsapp_v"]}</span></a>
        <a class="ccard reveal" href="mailto:{EMAIL}">{icon("mail")}<span class="k">{t["c_email"]}</span><span class="v" dir="ltr">{EMAIL}</span></a>
        <div class="ccard reveal">{icon("pin")}<span class="k">{t["c_location"]}</span><span class="v">{t["c_location_v"]}</span></div>
      </div>
      <div class="cv-card reveal">
        <div><h2 class="cv-title">{t["c_cv_title"]}</h2><p>{t["c_cv_text"]}</p></div>
        <div class="cv-action"><a class="btn btn-light" href="{cv_href()}" download>{icon("download")}{t["cta_cv"]}</a><small>{t["cv_meta"]}</small></div>
      </div>
    </div>
  </section>
</main>"""


BODIES = {"home": body_home, "about": body_about, "experience": body_experience,
          "treatments": body_treatments, "education": body_education, "contact": body_contact}


def render(lang, page):
    return head(lang, page) + "\n<body>\n" + gnav(lang, page) + BODIES[page](lang) + "\n" + footer(lang, page)


def not_found():
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found — Dr. Karina Rauashde</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/css/style.css?v=""" + VERSION + """">
</head>
<body class="nf">
<main class="nf-main">
  <p class="eyebrow">404</p>
  <h1 class="phero-title">This page can’t be found.</h1>
  <p class="phero-lead" dir="rtl" lang="ar">لم يتم العثور على هذه الصفحة.</p>
  <p class="phero-lead" lang="ru">Страница не найдена.</p>
  <div class="ctas"><a class="btn" href="/">Home</a><a class="btn btn-outline" href="/ar/" lang="ar">الرئيسية</a><a class="btn btn-outline" href="/ru/" lang="ru">Главная</a></div>
</main>
</body>
</html>
"""


def main():
    written = []
    for lang in LANGS:
        for page in PAGES:
            rel = LANG_PREFIX[lang] + SLUG[page]
            out_dir = os.path.join(ROOT, rel)
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(render(lang, page))
            written.append("/" + rel)
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(not_found())

    base = SITE.rstrip("/")
    urls = []
    for lang in LANGS:
        for page in PAGES:
            alts = "".join(
                f'<xhtml:link rel="alternate" hreflang="{l}" href="{base}{href(l, page)}"/>' for l in LANGS
            ) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{base}{href("en", page)}"/>'
            urls.append(f"<url><loc>{base}{href(lang, page)}</loc>{alts}</url>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    print(f"built {len(written)} pages + 404:", " ".join(written))


if __name__ == "__main__":
    main()
