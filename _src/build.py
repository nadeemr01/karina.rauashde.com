#!/usr/bin/env python3
"""Builds index.html (EN), ar/index.html and ru/index.html from content.py.
Run from anywhere:  python3 _src/build.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content import (T, LANGS, PATHS, SWITCH_LABEL, SWITCH_NAME, PHONE_DISPLAY, PHONE_TEL,  # noqa: E402
                     WHATSAPP, EMAIL, CV_FILE, SITE)

VERSION = "1"  # bump to bust caches of css/js after edits

ICONS = {
    "syringe": '<path d="m18 2 4 4"/><path d="m17 7 3-3"/><path d="M19 9 8.7 19.3a2.4 2.4 0 0 1-3.4 0l-.6-.6a2.4 2.4 0 0 1 0-3.4L15 5"/><path d="m9 11 4 4"/><path d="m5 19-3 3"/><path d="m14 4 6 6"/>',
    "light": '<circle cx="12" cy="12" r="3.2"/><path d="M12 2v3M12 19v3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M2 12h3M19 12h3M4.9 19.1 7 17M17 7l2.1-2.1"/>',
    "drop": '<path d="M12 2.8S5.5 9.6 5.5 14.3a6.5 6.5 0 0 0 13 0C18.5 9.6 12 2.8 12 2.8z"/><path d="M9.2 14.8a2.9 2.9 0 0 0 2.8 2.7"/>',
    "stetho": '<path d="M5 3H4v6a5 5 0 0 0 10 0V3h-1"/><path d="M9 14v1.5a6 6 0 0 0 12 0V12"/><circle cx="21" cy="10" r="2"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "check": '<circle cx="12" cy="12" r="10"/><path d="m8 12.5 2.8 2.8L16.5 9.5"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "chat": '<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/><path d="M9 10.5c.4 1.6 2.4 3.6 4 4l1.3-1.2 1.9.9"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/>',
    "arrow": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
}


def icon(name, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


# Fonts per language (Google Fonts)
FONTS_LATIN = ("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500"
               "&family=Manrope:wght@400;500;600;700&display=swap")
FONTS_AR = ("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,500"
            "&family=IBM+Plex+Sans+Arabic:wght@400;500;600&family=Noto+Naskh+Arabic:wght@500;600;700&display=swap")

# Only the English root page sends first-time Arabic/Russian browsers to their language.
REDIRECT_JS = """<script>(function(){try{if(localStorage.getItem('lang'))return;var l=((navigator.languages&&navigator.languages[0])||navigator.language||'').toLowerCase();if(l.indexOf('ar')===0)location.replace('ar/'+location.hash);else if(l.indexOf('ru')===0)location.replace('ru/'+location.hash);}catch(e){}})();</script>"""

MOTES = [  # x%, bottom%, size px, duration s, delay s, drift px
    (8, 18, 5, 9, 0, 14), (16, 30, 3, 7, 2.5, -10), (24, 10, 4, 10, 5, 8), (78, 22, 5, 8, 1, -12),
    (86, 12, 3, 9.5, 3.5, 10), (92, 34, 4, 7.5, 6, -8), (50, 8, 3, 11, 4, 6), (64, 16, 4, 8.5, 7, -6),
    (34, 22, 3, 9, 8, 12), (70, 40, 3, 10, 2, -10),
]


def page(lang):
    t = T[lang]
    p = "" if lang == "en" else "../"
    url = SITE + PATHS[lang]

    # ---------- head ----------
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE}{PATHS[l]}">' for l in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}">'
    og_alt = "\n".join(
        f'<meta property="og:locale:alternate" content="{T[l]["og_locale"]}">' for l in LANGS if l != lang
    )
    ld = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Karina Rauashde",
        "alternateName": ["Karina Rawashdeh", "كارينا الرواشدة", "Рауашде Карина Раедовна"],
        "jobTitle": "Dermatologist",
        "url": SITE,
        "image": SITE + "img/og.jpg",
        "email": "mailto:" + EMAIL,
        "telephone": PHONE_TEL,
        "address": {"@type": "PostalAddress", "addressLocality": "Moscow", "addressCountry": "RU"},
        "alumniOf": [
            {"@type": "CollegeOrUniversity", "name": "Volgograd State Medical University"},
            {"@type": "CollegeOrUniversity", "name": "RUDN University"},
        ],
        "knowsLanguage": ["ar", "ru", "en"],
    }
    fonts = FONTS_AR if lang == "ar" else FONTS_LATIN

    switch = "".join(
        f'<a href="{p}{PATHS[l]}" hreflang="{l}" lang="{l}" aria-label="{SWITCH_NAME[l]}"'
        f'{" aria-current=\"page\"" if l == lang else ""}>{SWITCH_LABEL[l]}</a>'
        for l in LANGS
    )
    nav = "".join(f'<a href="#{i}">{label}</a>' for i, label in t["nav"])

    # ---------- hero ----------
    meta_icons = ["pin", "check", "globe"]
    hero_meta = "".join(f"<li>{icon(meta_icons[i])}<span>{m}</span></li>" for i, m in enumerate(t["meta"]))
    motes = "".join(
        f'<span style="--x:{x}%;--b:{b}%;--s:{s}px;--d:{d}s;--delay:{dl}s;--dx:{dx}px"></span>'
        for x, b, s, d, dl, dx in MOTES
    )

    # ---------- about ----------
    about_p = "".join(f"<p>{para}</p>" for para in t["about_p"])
    stats = "".join(
        f'<div class="stat"><b dir="ltr">{n}</b><span>{label}</span></div>' for n, label in t["stats"]
    )

    # ---------- experience ----------
    exp_items = []
    for e in t["exp"]:
        bullets = ""
        if e["bullets"]:
            bullets = '<ul class="t-list">' + "".join(f"<li>{b}</li>" for b in e["bullets"]) + "</ul>"
        chips = ""
        if e["chips"]:
            chips = '<div class="chips">' + "".join(f'<span class="chip">{c}</span>' for c in e["chips"]) + "</div>"
        desc = f'<p class="t-desc">{e["desc"]}</p>' if e["desc"] else ""
        exp_items.append(f"""
        <article class="t-item reveal">
          <div class="t-top"><span class="period">{e["period"]}</span><span class="place">{icon("pin")}{e["place"]}</span></div>
          <h3 class="t-role">{e["role"]}</h3>
          <p class="t-org">{e["org"]}</p>
          {desc}{bullets}{chips}
        </article>""")
    exp_html = "".join(exp_items)

    # ---------- procedures ----------
    proc_cards = []
    for ic, title, items in t["proc"]:
        lis = "".join(
            f"<li><b>{name}</b>{f'<span>{detail}</span>' if detail else ''}</li>" for name, detail in items
        )
        proc_cards.append(f"""
        <article class="proc reveal">
          <div class="proc-icon">{icon(ic)}</div>
          <h3>{title}</h3>
          <ul>{lis}</ul>
        </article>""")
    proc_html = "".join(proc_cards)

    # ---------- education ----------
    edu_html = "".join(f"""
          <li class="edu-item reveal">
            <span class="edu-period">{period}</span>
            <div><h3 class="edu-org">{org}</h3><p class="edu-prog">{prog}</p><p class="edu-place">{place}</p></div>
          </li>""" for period, org, prog, place in t["edu"])
    langs_html = "".join(
        f'<li><span class="lang-name">{name}</span>{f"<em>{lvl}</em>" if lvl else ""}</li>' for name, lvl in t["langs"]
    )

    rtl_bdi = ' dir="ltr"'
    cv_href = f"{p}{CV_FILE}"

    return f"""<!doctype html>
<html lang="{lang}" dir="{t["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t["title"]}</title>
<meta name="description" content="{t["description"]}">
<link rel="canonical" href="{url}">
{alternates}
<meta property="og:type" content="profile">
<meta property="og:site_name" content="Dr. Karina Rauashde">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["description"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{t["img_alt"]}">
<meta property="og:locale" content="{t["og_locale"]}">
{og_alt}
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f4ebdf">
<meta name="color-scheme" content="light">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<link rel="preload" as="image" href="{p}img/karina-float.webp" type="image/webp" fetchpriority="high">
<link rel="stylesheet" href="{p}css/style.css?v={VERSION}">
<script>document.documentElement.classList.add('js')</script>
{REDIRECT_JS if lang == "en" else ""}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{t["skip"]}</a>

<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="#top" aria-label="{t["brand"]}"><span class="brand-mark" aria-hidden="true">KR</span><span class="brand-name">{t["brand"]}</span></a>
    <nav class="nav" aria-label="Sections">{nav}</nav>
    <div class="lang">{switch}</div>
  </div>
</header>

<main id="main">
  <section class="hero" id="top">
    <div class="hero-bg" aria-hidden="true"></div>
    <div class="container hero-grid">
      <div class="hero-text">
        <p class="eyebrow hero-in" style="--i:1">{t["eyebrow"]}</p>
        <h1 class="hero-name hero-in" style="--i:2">{t["name_html"]}</h1>
        <p class="hero-role hero-in" style="--i:3">{t["role"]}</p>
        <p class="hero-lead hero-in" style="--i:4">{t["lead"]}</p>
        <div class="btns hero-in" style="--i:5">
          <a class="btn btn-primary" href="#contact">{t["cta_contact"]}{icon("arrow", "ico flip")}</a>
          <a class="btn btn-ghost" href="{cv_href}" download>{icon("download")}<span>{t["cta_cv"]}</span><small>{t["cv_note"]}</small></a>
        </div>
        <ul class="hero-meta hero-in" style="--i:6">{hero_meta}</ul>
      </div>

      <div class="hero-visual hero-in" style="--i:2">
        <div class="stage">
          <div class="arch" aria-hidden="true"><span class="rays"></span></div>
          <div class="ripples" aria-hidden="true"><i></i><i></i><i></i></div>
          <div class="float-shadow" aria-hidden="true"></div>
          <div class="motes" aria-hidden="true">{motes}</div>
          <picture>
            <source srcset="{p}img/karina-float.webp" type="image/webp">
            <img class="float" src="{p}img/karina-float.png" width="944" height="1244" alt="{t["img_alt"]}" fetchpriority="high" decoding="async">
          </picture>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="about">
    <div class="container">
      <div class="about">
        <div class="section-head reveal">
          <p class="eyebrow">{t["about_label"]}</p>
          <h2 class="h2">{t["about_title"]}</h2>
        </div>
        <div class="about-text reveal">{about_p}</div>
      </div>
      <div class="stats reveal">{stats}</div>
    </div>
  </section>

  <section class="section section-alt" id="experience">
    <div class="container">
      <div class="section-head reveal">
        <p class="eyebrow">{t["exp_label"]}</p>
        <h2 class="h2">{t["exp_title"]}</h2>
      </div>
      <div class="timeline">{exp_html}
      </div>
    </div>
  </section>

  <section class="section" id="procedures">
    <div class="container">
      <div class="section-head reveal">
        <p class="eyebrow">{t["proc_label"]}</p>
        <h2 class="h2">{t["proc_title"]}</h2>
        <p class="intro">{t["proc_intro"]}</p>
      </div>
      <div class="proc-grid">{proc_html}
      </div>
    </div>
  </section>

  <section class="section section-alt" id="education">
    <div class="container">
      <div class="section-head reveal">
        <p class="eyebrow">{t["edu_label"]}</p>
        <h2 class="h2">{t["edu_title"]}</h2>
      </div>
      <div class="edu-grid">
        <ol class="edu-list">{edu_html}
        </ol>
        <div class="edu-side">
          <article class="license reveal">
            <p class="eyebrow">{t["lic_label"]}</p>
            <div class="license-top"><span class="badge">{icon("check")}{t["lic_status"]}</span><span class="license-date">{t["lic_date"]}</span></div>
            <h3>{t["lic_name"]}</h3>
            <p>{t["lic_issuer"]}</p>
          </article>
          <article class="langs reveal">
            <p class="eyebrow">{t["langs_label"]}</p>
            <ul>{langs_html}</ul>
          </article>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="contact">
    <div class="container">
      <div class="contact reveal">
        <div class="contact-head">
          <p class="eyebrow">{t["contact_label"]}</p>
          <h2 class="h2">{t["contact_title"]}</h2>
          <p class="intro">{t["contact_lead"]}</p>
        </div>
        <div class="contact-grid">
          <a class="c-card" href="tel:{PHONE_TEL}">{icon("phone")}<span class="k">{t["c_phone"]}</span><span class="v"{rtl_bdi}>{PHONE_DISPLAY}</span></a>
          <a class="c-card" href="{WHATSAPP}" target="_blank" rel="noopener">{icon("chat")}<span class="k">{t["c_whatsapp"]}</span><span class="v">{t["c_whatsapp_v"]}</span></a>
          <a class="c-card" href="mailto:{EMAIL}">{icon("mail")}<span class="k">{t["c_email"]}</span><span class="v"{rtl_bdi}>{EMAIL}</span></a>
          <div class="c-card">{icon("pin")}<span class="k">{t["c_location"]}</span><span class="v">{t["c_location_v"]}</span></div>
        </div>
        <a class="btn btn-light" href="{cv_href}" download>{icon("download")}<span>{t["c_cv"]}</span></a>
      </div>
    </div>
  </section>
</main>

<footer class="footer">
  <div class="container footer-inner">
    <p>{t["footer"]}</p>
    <div class="lang lang-foot">{switch}</div>
  </div>
</footer>

<script src="{p}js/main.js?v={VERSION}" defer></script>
</body>
</html>
"""


def main():
    for lang in LANGS:
        out_dir = os.path.join(ROOT, PATHS[lang])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(lang))
    # sitemap with hreflang alternates
    urls = []
    for lang in LANGS:
        alts = "".join(
            f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{PATHS[l]}"/>' for l in LANGS
        )
        urls.append(f"<url><loc>{SITE}{PATHS[lang]}</loc>{alts}</url>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:xhtml="http://www.w3.org/1999/xhtml">' + "".join(urls) + "</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    print("built:", ", ".join("/" + PATHS[l] for l in LANGS))


if __name__ == "__main__":
    main()
