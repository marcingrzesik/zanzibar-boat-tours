#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for captainbusara.com (no dependencies, Python 3.8+).

    python3 tools/build.py

Reads tools/content.py and writes:
    index.html            English home page
    pl/index.html         Polish home page
    privacy.html          English privacy notice
    pl/privacy.html       Polish privacy notice
    404.html              Bilingual "not found" page
    site.webmanifest      Web app manifest
    sitemap.xml           Sitemap with hreflang alternates
"""
import html
import json
import pathlib
import sys
from urllib.parse import quote

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from content import SITE, IMAGES, S, TOURS, GALLERY, REVIEWS, FAQ, PRIVACY  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANGS = ("en", "pl")
VERSION = SITE["lastmod"].replace("-", "")
WA_ICON = ('<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" '
           'd="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>')
PHONE_ICON = ('<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" '
              'd="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2a1 1 0 011-.25 11.4 11.4 0 003.6.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.6a1 1 0 01-.25 1z"/></svg>')


def esc(x):
    return html.escape(x, quote=True)


def wa_link(text):
    return "https://wa.me/%s?text=%s" % (SITE["whatsapp"], quote(text, safe=""))


class Page:
    """Helpers bound to one language."""

    def __init__(self, lang):
        self.lang = lang
        self.i = LANGS.index(lang)
        self.A = "" if lang == "en" else "../"          # relative prefix to site root
        self.url = SITE["domain"] + ("/" if lang == "en" else "/pl/")

    def s(self, key):
        return S[key][self.i]

    def t(self, pair):
        return pair[self.i]

    def img(self, key, alt, cls="", lazy=True, priority=False, sizes=None):
        w, h = IMAGES[key]
        attrs = 'src="%simages/%s.webp" width="%d" height="%d" alt="%s"' % (self.A, key, w, h, esc(alt))
        if cls:
            attrs += ' class="%s"' % cls
        if priority:
            attrs += ' fetchpriority="high" decoding="async"'
        elif lazy:
            attrs += ' loading="lazy" decoding="async"'
        if sizes:
            attrs += ' sizes="%s"' % sizes
        return "<img %s>" % attrs


# ------------------------------------------------------------------ sections
def head(p, title, desc, canonical, alternates, extra="", noindex=False):
    d = SITE["domain"]
    lines = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>%s</title>" % esc(title),
        '<meta name="description" content="%s">' % esc(desc),
        '<meta name="theme-color" content="#0B2D5B">',
    ]
    if noindex:
        lines.append('<meta name="robots" content="noindex">')
    else:
        lines.append('<link rel="canonical" href="%s">' % canonical)
        for hl, href in alternates:
            lines.append('<link rel="alternate" hreflang="%s" href="%s">' % (hl, href))
    lines += [
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Captain Busara">',
        '<meta property="og:title" content="%s">' % esc(title),
        '<meta property="og:description" content="%s">' % esc(p.s("og_desc")),
        '<meta property="og:url" content="%s">' % canonical,
        '<meta property="og:image" content="%s/images/og.jpg">' % d,
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:locale" content="%s">' % ("en_US" if p.lang == "en" else "pl_PL"),
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % esc(title),
        '<meta name="twitter:description" content="%s">' % esc(p.s("og_desc")),
        '<meta name="twitter:image" content="%s/images/og.jpg">' % d,
        '<link rel="icon" type="image/png" sizes="48x48" href="%simages/favicon-48.png">' % p.A,
        '<link rel="icon" type="image/png" sizes="192x192" href="%simages/icon-192.png">' % p.A,
        '<link rel="apple-touch-icon" href="%simages/apple-touch-icon.png">' % p.A,
        '<link rel="manifest" href="%ssite.webmanifest">' % p.A,
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">',
        '<link rel="stylesheet" href="%sstyles.css?v=%s">' % (p.A, VERSION),
    ]
    if extra:
        lines.append(extra)
    return "\n  ".join(lines)


def json_ld(p):
    d = SITE["domain"]
    offers = []
    for t in TOURS:
        offers.append({"@type": "Offer", "itemOffered": {
            "@type": "TouristTrip", "name": p.t(t["title"]), "description": p.t(t["desc"])}})
    biz = {
        "@context": "https://schema.org",
        "@type": "TravelAgency",
        "@id": d + "/#business",
        "name": "Captain Busara",
        "alternateName": "Captain Busara – Zanzibar Experiences",
        "description": p.s("meta_desc"),
        "url": p.url,
        "image": d + "/images/og.jpg",
        "logo": d + "/images/logo.webp",
        "telephone": SITE["phone"],
        "address": {"@type": "PostalAddress", "addressLocality": "Kendwa", "addressRegion": "Zanzibar",
                    "addressCountry": "TZ"},
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lng"]},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "08:00", "closes": "20:00"}],
        "knowsLanguage": ["en", "pl", "sw"],
        "hasMap": "https://www.google.com/maps?q=%s,%s" % (SITE["lat"], SITE["lng"]),
        "makesOffer": offers,
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": p.t(q),
                        "acceptedAnswer": {"@type": "Answer", "text": p.t(a)}} for q, a in FAQ],
    }
    out = ""
    for obj in (biz, faq):
        out += '<script type="application/ld+json">%s</script>\n  ' % json.dumps(obj, ensure_ascii=False)
    return out.rstrip()


def header(p, page="home"):
    # On the home page links are in-page anchors; on other pages they point to the language's home page.
    link = (lambda a: "#" + a) if page == "home" else (lambda a: "./#" + a)
    items = [("tours", "nav_tours"), ("book", "nav_book"), ("gallery", "nav_gallery"),
             ("reviews", "nav_reviews"), ("faq", "nav_faq")]
    nav = "".join('<a href="%s">%s</a>' % (link(a), p.s(k)) for a, k in items)
    nav += '<a href="%s" class="btn btn--ghost">%s</a>' % (link("contact"), p.s("nav_contact"))
    mobile = "".join('<a href="%s">%s</a>' % (link(a), p.s(k)) for a, k in items + [("contact", "nav_contact")])
    en_href = ("./" if p.lang == "en" else "../") if page == "home" else ("./privacy.html" if p.lang == "en" else "../privacy.html")
    pl_href = ("pl/" if p.lang == "en" else "./") if page == "home" else ("pl/privacy.html" if p.lang == "en" else "./privacy.html")
    brand_href = "#top" if page == "home" else "./"
    return f"""<header class="topbar">
    <div class="container topbar__inner">
      <a class="brand" href="{brand_href}">
        <img class="brand__logo" src="{p.A}images/logo.webp" width="48" height="48" alt="">
        <span class="brand__text"><strong>Captain Busara</strong><small>{p.s('brand_sub')}</small></span>
      </a>
      <nav class="nav" aria-label="Main">{nav}</nav>
      <div class="lang" role="group" aria-label="{p.s('lang_label')}">
        <a class="lang__btn{' is-active' if p.lang == 'en' else ''}" href="{en_href}" hreflang="en" lang="en" data-lang="en"{' aria-current="true"' if p.lang == 'en' else ''}>EN</a>
        <a class="lang__btn{' is-active' if p.lang == 'pl' else ''}" href="{pl_href}" hreflang="pl" lang="pl" data-lang="pl"{' aria-current="true"' if p.lang == 'pl' else ''}>PL</a>
      </div>
      <button class="burger" id="burger" type="button" aria-label="{p.s('menu_open')}" aria-expanded="false" aria-controls="mobileMenu" data-open="{p.s('menu_open')}" data-close="{p.s('menu_close')}"><span aria-hidden="true">☰</span></button>
    </div>
    <div class="mobileMenu" id="mobileMenu" hidden>{mobile}</div>
  </header>"""


def hero(p):
    default_wa = wa_link(p.s("m_default"))
    return f"""<section class="hero">
      <div class="container hero__inner">
        <div class="hero__content">
          <p class="pill">{p.s('pill')}</p>
          <h1>{p.s('h1_h')}</h1>
          <p class="lead">{p.s('lead_h')}</p>
          <div class="hero__cta">
            <a class="btn btn--primary" href="{default_wa}" target="_blank" rel="noopener" data-wa data-track="whatsapp_hero">{WA_ICON}{p.s('cta_wa')}</a>
            <a class="btn btn--secondary" href="#tours">{p.s('cta_tours')}</a>
          </div>
          <p class="hero__note">{p.s('hero_note')}</p>
          <div class="hero__badges">
            <div class="badge"><strong>{p.s('badge1_t')}</strong><span>{p.s('badge1_s')}</span></div>
            <div class="badge"><strong>{p.s('badge2_t')}</strong><span>{p.s('badge2_s')}</span></div>
            <div class="badge"><strong>{p.s('badge3_t')}</strong><span>{p.s('badge3_s')}</span></div>
          </div>
        </div>
        <div class="hero__media">
          <div class="photoGrid">
            {p.img('hero-boat', 'A traditional boat on turquoise water' if p.lang == 'en' else 'Tradycyjna łódź na turkusowej wodzie', priority=True)}
            {p.img('kayak-flowers', p.t(TOURS[8]['alt']), lazy=False)}
            {p.img('sunset-dhow', p.t(TOURS[4]['alt']), lazy=False)}
          </div>
          <div class="glassCard">
            <strong>{p.s('glass_t')}</strong>
            <div class="glassRow"><span>{p.s('glass_a')}</span><span class="dot" aria-hidden="true">•</span><span>{p.s('glass_b')}</span></div>
            <small>{p.s('glass_s')}</small>
          </div>
        </div>
      </div>
    </section>"""


def trust(p):
    def card(tk, lk):
        return '<div class="trustCard"><h3>%s</h3><ul>%s</ul></div>' % (
            p.s(tk), "".join("<li>%s</li>" % esc(x) for x in p.s(lk)))
    return ('<section class="trust"><div class="container trust__inner">%s%s%s</div></section>'
            % (card("trust1_t", "trust1"), card("trust2_t", "trust2"), card("trust3_t", "trust3")))


def how(p):
    steps = "".join(
        '<li class="step"><span class="step__n" aria-hidden="true">%d</span><div><h3>%s</h3><p>%s</p></div></li>'
        % (n, p.s("how%d_t" % n), p.s("how%d" % n)) for n in (1, 2, 3))
    return f"""<section class="section section--tight" id="how">
      <div class="container">
        <div class="sectionHeader"><h2>{p.s('how_h')}</h2><p>{p.s('how_s')}</p></div>
        <ol class="steps">{steps}</ol>
      </div>
    </section>"""


def captain(p):
    facts = "".join("<li>%s</li>" % esc(x) for x in p.s("cap_f"))
    msg = wa_link(p.s("m_default"))
    return f"""<section class="section" id="captain">
      <div class="container">
        <div class="sectionHeader"><h2>{p.s('cap_h')}</h2><p>{p.s('cap_s')}</p></div>
        <div class="captain">
          <div class="captain__text">
            <p>{p.s('cap_p1_h')}</p>
            <p>{p.s('cap_p2')}</p>
            <div class="captain__cta">
              <a class="btn btn--primary" href="{msg}" target="_blank" rel="noopener" data-wa data-track="whatsapp_captain">{WA_ICON}{p.s('cap_cta')}</a>
              <a class="btn btn--ghost" href="#tours">{p.s('cta_tours')}</a>
            </div>
          </div>
          <div class="captain__card"><h3>{p.s('cap_facts')}</h3><ul>{facts}</ul></div>
        </div>
      </div>
    </section>"""


def tour_card(p, t):
    title = p.t(t["title"])
    meta = "".join('<span><span aria-hidden="true">%s</span> %s</span>' % (ic, esc(p.t(txt))) for ic, txt in t["meta"])
    if t.get("img"):
        w, h = IMAGES[t["img"]]
        src = "%simages/%s.webp" % (p.A, t["img"])
        if t.get("contain"):
            media = ('<div class="card__img card__img--contain" style="--bg:url(%s)">'
                     '<img src="%s" width="%d" height="%d" alt="%s" loading="lazy" decoding="async"></div>'
                     % (src, src, w, h, esc(p.t(t["alt"]))))
        else:
            media = ('<div class="card__img"><img src="%s" width="%d" height="%d" alt="%s" loading="lazy" decoding="async"></div>'
                     % (src, w, h, esc(p.t(t["alt"]))))
    else:
        media = ('<div class="card__img card__img--ph" aria-hidden="true"><span class="ph__icon">%s</span>'
                 '<span class="ph__txt">%s</span></div>' % (t.get("icon", "🌊"), p.s("photo_soon")))
    price = ""
    if t.get("price"):
        price = '<p class="price">%s <strong>%s</strong></p>' % (p.s("from"), esc(t["price"]))
    wa = wa_link(p.t(S["m_hi"]).format(tour=title) + " " + p.t(S["m_bye"]))
    return f"""<article class="card" data-cat="{t['cat']}" id="tour-{t['id']}">
          {media}
          <div class="card__body">
            <h3>{esc(title)}</h3>
            <p>{esc(p.t(t['desc']))}</p>
            <div class="meta">{meta}</div>
            {price}
            <div class="card__cta">
              <button class="btn btn--primary" type="button" data-book="{esc(title)}">{p.s('card_go')}</button>
              <a class="btn btn--ghost" href="{wa}" target="_blank" rel="noopener" data-wa data-track="whatsapp_tour" data-tour="{esc(title)}">{WA_ICON}{p.s('card_ask')}</a>
            </div>
          </div>
        </article>"""


def tours(p):
    cards = "\n        ".join(tour_card(p, t) for t in TOURS)
    custom_l = "".join("<li>%s</li>" % esc(x) for x in p.s("custom_l"))
    custom = f"""<article class="card card--special" data-cat="all-only" id="tour-custom">
          <div class="card__body">
            <h3>{p.s('custom_t')}</h3>
            <p class="big">{p.s('custom_d')}</p>
            <ul class="check">{custom_l}</ul>
            <div class="card__cta">
              <button class="btn btn--primary" type="button" data-book="{esc(p.s('custom_t'))}">{p.s('custom_cta')}</button>
            </div>
          </div>
        </article>"""
    filters = "".join(
        '<button class="chip%s" type="button" data-filter="%s" aria-pressed="%s">%s</button>'
        % (" is-active" if f == "all" else "", f, "true" if f == "all" else "false", p.s(k))
        for f, k in (("all", "f_all"), ("sea", "f_sea"), ("land", "f_land"), ("fun", "f_fun")))
    return f"""<section class="section" id="tours">
      <div class="container">
        <div class="sectionHeader"><h2>{p.s('tours_h')}</h2><p>{p.s('tours_s')}</p></div>
        <div class="filters" role="group" aria-label="{esc(p.s('tours_h'))}">{filters}</div>
        <div class="cards" id="cards">
        {cards}
        {custom}
        </div>
        <p class="note">{p.s('tours_note')}</p>
      </div>
    </section>"""


def booking(p):
    opts = '<option value="">%s</option>' % esc(p.s("f_any_tour"))
    for t in TOURS:
        opts += '<option value="%s">%s</option>' % (esc(p.t(t["title"])), esc(p.t(t["title"])))
    opts += '<option value="%s">%s</option>' % (esc(p.s("custom_t")), esc(p.s("custom_t")))
    default_wa = wa_link(p.s("m_default"))
    return f"""<section class="section section--alt" id="book">
      <div class="container book">
        <div class="book__form">
          <div class="sectionHeader sectionHeader--stack"><h2>{p.s('book_h')}</h2><p>{p.s('book_s')}</p></div>
          <form id="bookForm" novalidate>
            <div class="grid2">
              <label class="field field--wide"><span>{p.s('f_tour')}</span><select id="fTour" name="tour">{opts}</select></label>
              <label class="field"><span>{p.s('f_date')}</span><input id="fDate" name="date" type="date"></label>
              <label class="field"><span>{p.s('f_people')}</span><input id="fPeople" name="people" type="number" min="1" max="30" inputmode="numeric" placeholder="2"></label>
              <label class="field field--wide"><span>{p.s('f_hotel')}</span><input id="fHotel" name="hotel" type="text" autocomplete="off" placeholder="{esc(p.s('f_hotel_ph'))}"></label>
              <label class="field"><span>{p.s('f_type')}</span>
                <select id="fType" name="type"><option value="">{p.s('f_any')}</option><option value="{esc(p.s('f_private'))}">{p.s('f_private')}</option><option value="{esc(p.s('f_group'))}">{p.s('f_group')}</option></select></label>
              <label class="field"><span>{p.s('f_name')}</span><input id="fName" name="name" type="text" autocomplete="given-name"></label>
              <label class="field field--wide"><span>{p.s('f_notes')}</span><textarea id="fNotes" name="notes" rows="3" placeholder="{esc(p.s('f_notes_ph'))}"></textarea></label>
            </div>
            <button class="btn btn--primary btn--lg" type="submit" data-track="whatsapp_form">{WA_ICON}{p.s('f_submit')}</button>
            <p class="hint">{p.s('f_hint')}</p>
            <noscript><p class="hint"><a class="link" href="{default_wa}" target="_blank" rel="noopener">{p.s('f_noscript')}</a></p></noscript>
          </form>
        </div>
        <aside class="book__preview" aria-live="polite">
          <h3>{p.s('f_preview')}</h3>
          <pre class="mono" id="msgPreview">{esc(p.s('m_default'))}</pre>
          <button class="btn btn--ghost" id="copyBtn" type="button">{p.s('f_copy')}</button>
        </aside>
      </div>
    </section>"""


def gallery(p):
    items = ""
    for i, (key, cap) in enumerate(GALLERY):
        w, h = IMAGES[key]
        c = p.t(cap)
        items += (f'<li><button class="gal__item" type="button" data-index="{i}" aria-label="{esc(c)}">'
                  f'<img src="{p.A}images/{key}.webp" width="{w}" height="{h}" alt="{esc(c)}" loading="lazy" decoding="async">'
                  f'</button></li>\n          ')
    return f"""<section class="section" id="gallery">
      <div class="container">
        <div class="sectionHeader"><h2>{p.s('gal_h')}</h2><p>{p.s('gal_s')}</p></div>
        <ul class="gallery">
          {items}</ul>
      </div>
      <dialog class="lightbox" id="lightbox" aria-label="{esc(p.s('gal_h'))}">
        <button class="lb__close" type="button" id="lbClose" aria-label="{p.s('lb_close')}">✕</button>
        <button class="lb__nav lb__prev" type="button" id="lbPrev" aria-label="{p.s('lb_prev')}">‹</button>
        <figure><img id="lbImg" src="" alt=""><figcaption id="lbCap"></figcaption></figure>
        <button class="lb__nav lb__next" type="button" id="lbNext" aria-label="{p.s('lb_next')}">›</button>
      </dialog>
    </section>"""


def reviews(p):
    shown = [r for r in REVIEWS if r.get("verified")]
    quotes = ""
    if shown:
        quotes = '<div class="quotes">%s</div>' % "".join(
            '<figure class="quote"><blockquote>“%s”</blockquote><figcaption>— %s, %s</figcaption></figure>'
            % (esc(p.t(r["text"])), esc(r["name"]), esc(p.t(r["country"]))) for r in shown)
    head_html = ('<div class="sectionHeader"><h2>%s</h2><p>%s</p></div>' % (p.s("rev_h"), p.s("rev_s"))) if shown else ""
    return f"""<section class="section section--alt" id="reviews">
      <div class="container">
        {head_html}
        {quotes}
        <div class="reviewBox">
          <h2 class="reviewBox__h">{p.s('rev_cta_h')}</h2>
          <p>{p.s('rev_cta_p')}</p>
          <div class="reviewActions">
            <a class="btn btn--primary" href="{SITE['google_review_url']}" target="_blank" rel="noopener" data-track="google_review">⭐ {p.s('rev_btn')}</a>
            <a class="btn btn--ghost" href="#tours">{p.s('rev_book')}</a>
          </div>
        </div>
      </div>
    </section>"""


def faq(p):
    items = "".join('<details><summary>%s</summary><div class="faq__content">%s</div></details>'
                    % (esc(p.t(q)), esc(p.t(a))) for q, a in FAQ)
    return f"""<section class="section" id="faq">
      <div class="container">
        <div class="sectionHeader"><h2>{p.s('faq_h')}</h2><p>{p.s('faq_s')}</p></div>
        <div class="faq">{items}</div>
      </div>
    </section>"""


def location(p):
    lat, lng = SITE["lat"], SITE["lng"]
    lis = "".join("<li>%s</li>" % esc(x) for x in p.s("loc_l"))
    wa = wa_link(p.s("m_default"))
    embed = "https://www.google.com/maps?q=%s,%s&z=15&output=embed" % (lat, lng)
    gmaps = "https://www.google.com/maps?q=%s,%s" % (lat, lng)
    return f"""<section class="section section--alt" id="location">
      <div class="container">
        <div class="sectionHeader"><h2>{p.s('loc_h')}</h2><p>{p.s('loc_s')}</p></div>
        <div class="location">
          <div class="location__card">
            <h3>{p.s('loc_card')}</h3>
            <p><strong>{p.s('badge1_t').replace('📍 ', '')}</strong><br>{p.s('loc_coords')}: <span class="monoInline">{lat}, {lng}</span></p>
            <ul>{lis}</ul>
            <div class="location__cta">
              <a class="btn btn--primary" href="{wa}" target="_blank" rel="noopener" data-wa data-track="whatsapp_location">{WA_ICON}{p.s('loc_cta')}</a>
              <a class="btn btn--ghost" href="{gmaps}" target="_blank" rel="noopener">{p.s('map_open')}</a>
            </div>
          </div>
          <div class="location__map" id="mapBox" data-src="{embed}" data-title="{esc(p.s('map_title'))}">
            <div class="map__poster">
              <button class="btn btn--secondary" id="mapLoad" type="button">🗺️ {p.s('map_load')}</button>
              <small>{p.s('map_note')}</small>
            </div>
          </div>
        </div>
      </div>
    </section>"""


def contact(p):
    wa = wa_link(p.s("m_default"))
    priv = "privacy.html"
    return f"""<section class="section" id="contact">
      <div class="container">
        <div class="contact__card">
          <h2>{p.s('con_h')}</h2>
          <p>{p.s('con_p_h')}</p>
          <div class="contact__actions">
            <a class="btn btn--primary" href="{wa}" target="_blank" rel="noopener" data-wa data-track="whatsapp_contact">{WA_ICON}{p.s('con_wa')}</a>
            <a class="btn btn--secondary" href="tel:{SITE['phone']}" data-track="call">{PHONE_ICON}{p.s('con_call')} {SITE['phone'].replace('+255', '+255 ')}</a>
          </div>
          <div class="contact__grid">
            <div class="contactInfo"><strong>{p.s('con_loc_t')}</strong><span>{p.s('con_loc')}</span></div>
            <div class="contactInfo"><strong>{p.s('con_hours_t')}</strong><span>{p.t(SITE['hours'])} • {p.s('con_hours_s')}</span></div>
            <div class="contactInfo"><strong>{p.s('con_safe_t')}</strong><span>{p.s('con_safe')}</span></div>
            <div class="contactInfo"><strong>{p.s('con_lang_t')}</strong><span>{p.s('con_lang')}</span></div>
          </div>
        </div>
      </div>
    </section>"""


def footer(p, page="home"):
    priv = "privacy.html"
    home = "./" if page != "home" else "#top"
    return f"""<footer class="footer">
    <div class="container footer__inner">
      <p>© <span id="year">2026</span> Captain Busara – Zanzibar Experiences. {p.s('rights')}</p>
      <p><a class="link" href="{priv}">{p.s('privacy')}</a></p>
    </div>
  </footer>"""


def sticky(p):
    wa = wa_link(p.s("m_default"))
    return f"""<div class="stickyBar" id="stickyBar">
    <a class="stickyWA" href="{wa}" target="_blank" rel="noopener" aria-label="{esc(p.s('wa_aria'))}" data-wa data-track="whatsapp_sticky">{WA_ICON}<span>{p.s('wa_sticky')}</span></a>
    <a class="stickyCall" href="tel:{SITE['phone']}" aria-label="{esc(p.s('call_aria'))}" data-track="call_sticky">{PHONE_ICON}</a>
  </div>"""


def client_config(p):
    cfg = {
        "lang": p.lang,
        "whatsapp": SITE["whatsapp"],
        "analytics": bool(SITE["analytics_domain"]),
        "msg": {k: p.s(k) for k in ("m_hi", "m_anytour", "m_date", "m_people", "m_hotel", "m_type", "m_name", "m_notes", "m_bye", "m_default")},
        "ui": {"copied": p.s("f_copied"), "copyErr": p.s("f_copy_err"), "copy": p.s("f_copy")},
    }
    return '<script type="application/json" id="siteConfig">%s</script>' % json.dumps(cfg, ensure_ascii=False)


def analytics_tag():
    d = SITE["analytics_domain"]
    if not d:
        return ""
    return ('<script defer data-domain="%s" src="https://plausible.io/js/script.tagged-events.js"></script>' % esc(d))


# ------------------------------------------------------------------ pages
def home_page(lang):
    p = Page(lang)
    alts = [("en", SITE["domain"] + "/"), ("pl", SITE["domain"] + "/pl/"), ("x-default", SITE["domain"] + "/")]
    hd = head(p, p.s("title"), p.s("meta_desc"), p.url, alts,
              extra=json_ld(p) + ("\n  " + analytics_tag() if analytics_tag() else ""))
    body = "\n\n    ".join([hero(p), trust(p), how(p), captain(p), tours(p), booking(p), gallery(p), reviews(p),
                            faq(p), location(p), contact(p)])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  {hd}
</head>
<body data-page="home">
  <a class="skip" href="#main">{p.s('skip')}</a>
  {header(p)}

  <main id="main">
    <span id="top"></span>
    {body}
  </main>

  {footer(p)}
  {sticky(p)}
  {client_config(p)}
  <script src="{p.A}script.js?v={VERSION}" defer></script>
</body>
</html>
"""


def privacy_page(lang):
    p = Page(lang)
    i = p.i
    url = SITE["domain"] + ("/privacy.html" if lang == "en" else "/pl/privacy.html")
    alts = [("en", SITE["domain"] + "/privacy.html"), ("pl", SITE["domain"] + "/pl/privacy.html")]
    title = PRIVACY["title"][i]
    hd = head(p, title, PRIVACY["h"][i], url, alts)
    blocks = "".join("<h2>%s</h2><p>%s</p>" % (esc(h[i]), esc(b[i])) for h, b in PRIVACY["blocks"])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  {hd}
</head>
<body data-page="privacy">
  <a class="skip" href="#main">{p.s('skip')}</a>
  {header(p, page='privacy')}
  <main id="main" class="doc">
    <div class="container container--narrow">
      <h1>{PRIVACY['h'][i]}</h1>
      <p class="muted">{PRIVACY['updated'][i]}</p>
      {blocks}
      <p><a class="btn btn--primary" href="./">{p.s('nf_btn')}</a></p>
    </div>
  </main>
  {footer(p, page='privacy')}
  {client_config(p)}
  <script src="{p.A}script.js?v={VERSION}" defer></script>
</body>
</html>
"""


def not_found_page():
    d = SITE["domain"]
    en, pl = Page("en"), Page("pl")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>404 | Captain Busara</title>
  <meta name="robots" content="noindex">
  <meta name="theme-color" content="#0B2D5B">
  <link rel="icon" type="image/png" href="/images/favicon-48.png">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css?v={VERSION}">
</head>
<body>
  <main class="doc notfound">
    <div class="container container--narrow">
      <img class="notfound__logo" src="/images/logo.webp" width="160" height="160" alt="Captain Busara">
      <h1>404</h1>
      <p><strong>{en.s('nf_h')}</strong> — {en.s('nf_p')}</p>
      <p><strong>{pl.s('nf_h')}</strong> — {pl.s('nf_p')}</p>
      <p class="notfound__btns"><a class="btn btn--primary" href="/">{en.s('nf_btn')}</a>
      <a class="btn btn--ghost" href="/pl/">{pl.s('nf_btn')}</a></p>
    </div>
  </main>
</body>
</html>
"""


def manifest():
    return json.dumps({
        "name": "Captain Busara – Zanzibar Experiences",
        "short_name": "Captain Busara",
        "start_url": "/",
        "display": "browser",
        "background_color": "#0B2D5B",
        "theme_color": "#0B2D5B",
        "icons": [{"src": "/images/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/images/favicon-512.png", "sizes": "512x512", "type": "image/png"}],
    }, ensure_ascii=False, indent=2) + "\n"


def sitemap():
    d, lm = SITE["domain"], SITE["lastmod"]

    def entry(en_path, pl_path):
        out = ""
        for loc in (en_path, pl_path):
            out += ("  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n"
                    '    <xhtml:link rel="alternate" hreflang="en" href="%s%s"/>\n'
                    '    <xhtml:link rel="alternate" hreflang="pl" href="%s%s"/>\n'
                    "  </url>\n") % (d, loc, lm, d, en_path, d, pl_path)
        return out
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + entry("/", "/pl/") + entry("/privacy.html", "/pl/privacy.html") + "</urlset>\n")


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", rel)


def main():
    write("index.html", home_page("en"))
    write("pl/index.html", home_page("pl"))
    write("privacy.html", privacy_page("en"))
    write("pl/privacy.html", privacy_page("pl"))
    write("404.html", not_found_page())
    write("site.webmanifest", manifest())
    write("sitemap.xml", sitemap())
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE["domain"])


if __name__ == "__main__":
    main()
