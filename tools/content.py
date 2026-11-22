# -*- coding: utf-8 -*-
"""
Content for the Captain Busara website (EN + PL).

Every text is a tuple: (English, Polish).
Edit texts / prices / tours here, then run:  python3 tools/build.py
The build writes index.html, pl/index.html, privacy pages, 404.html, sitemap.xml.
"""

SITE = {
    "domain": "https://captainbusara.com",
    "whatsapp": "255622702571",          # international format, no "+"
    "phone": "+255622702571",
    "google_review_url": "https://g.page/r/CQwGKj07Ub4lEBM/review",
    "lat": -5.750387916694523,
    "lng": 39.28784786172583,
    "hours": ("Daily 8:00–20:00", "Codziennie 8:00–20:00"),
    # Optional privacy-friendly analytics (Plausible). Leave "" to keep analytics OFF.
    "analytics_domain": "",
    "lastmod": "2026-11-22",
}

# Image sizes (width, height) – used for width/height attributes (prevents layout shift)
IMAGES = {
    "hero-boat": (831, 609), "mnemba-island": (1400, 788), "mnemba-aerial": (1400, 948),
    "dolphins": (669, 446), "sandbank": (474, 266), "salaam-cave": (474, 331),
    "salaam-turtles": (736, 919), "baraka-turtles": (1200, 630), "baraka-swim": (474, 316),
    "sunset-dhow": (1300, 650), "sunset-deck": (669, 446), "safari-lagoon": (474, 246),
    "baobab": (507, 338), "starfish": (189, 290), "kayak-flowers": (1200, 900),
    "kayak-couple": (1200, 900), "jozani-monkeys": (1200, 900), "jozani-colobus": (1200, 779),
    "stone-town": (669, 446), "spice-fruit": (474, 395), "water-car": (1200, 900),
    "logo": (480, 480),
}

# ---------------------------------------------------------------- UI strings
S = {
    # meta
    "title": ("Captain Busara | Boat Tours from Kendwa Beach, Zanzibar",
              "Captain Busara | Wycieczki łodzią z plaży Kendwa, Zanzibar"),
    "meta_desc": ("Private & small-group boat tours from Kendwa Beach, Zanzibar: Mnemba snorkeling, turtles, "
                  "sandbanks, sunset cruise, Jozani Forest, Stone Town and more. Book directly on WhatsApp.",
                  "Prywatne i kameralne wycieczki łodzią z plaży Kendwa na Zanzibarze: snorkeling przy Mnemba, żółwie, "
                  "mielizny, rejs o zachodzie słońca, las Jozani, Stone Town i więcej. Rezerwuj bezpośrednio na WhatsApp."),
    "og_desc": ("Mnemba • Turtles • Sandbanks • Sunset Cruise • Jozani • Stone Town. Book on WhatsApp.",
                "Mnemba • Żółwie • Mielizny • Rejs o zachodzie słońca • Jozani • Stone Town. Rezerwacja na WhatsApp."),
    "skip": ("Skip to content", "Przejdź do treści"),

    # nav / header
    "brand_sub": ("Local boat tours • Kendwa Beach • Zanzibar", "Lokalne wycieczki łodzią • plaża Kendwa • Zanzibar"),
    "nav_tours": ("Tours", "Wycieczki"),
    "nav_book": ("Book", "Rezerwacja"),
    "nav_gallery": ("Gallery", "Galeria"),
    "nav_reviews": ("Reviews", "Opinie"),
    "nav_faq": ("FAQ", "FAQ"),
    "nav_contact": ("Contact", "Kontakt"),
    "menu_open": ("Open menu", "Otwórz menu"),
    "menu_close": ("Close menu", "Zamknij menu"),
    "lang_label": ("Language", "Język"),

    # hero
    "pill": ("Local captain • Safety gear • Hotel pickup on request",
             "Lokalny kapitan • Sprzęt bezpieczeństwa • Odbiór z hotelu na życzenie"),
    "h1_h": ("Private &amp; small-group boat tours from <span class=\"accent\">Kendwa Beach</span>.",
             "Prywatne i kameralne wycieczki łodzią z <span class=\"accent\">plaży Kendwa</span>."),
    "lead_h": ("Snorkel at Mnemba, meet sea turtles, step onto a sandbank, enjoy a sunset cruise — "
               "with a real local captain. <strong>Book directly on WhatsApp.</strong>",
               "Snorkeling przy Mnemba, żółwie morskie, piaszczysta mielizna i rejs o zachodzie słońca — "
               "z prawdziwym lokalnym kapitanem. <strong>Rezerwuj bezpośrednio na WhatsApp.</strong>"),
    "cta_wa": ("Book on WhatsApp", "Rezerwuj na WhatsApp"),
    "cta_tours": ("See tours", "Zobacz wycieczki"),
    "hero_note": ("Send your date and hotel — we confirm availability on WhatsApp.",
                  "Napisz datę i hotel — dostępność potwierdzimy na WhatsApp."),
    "badge1_t": ("📍 Kendwa Beach", "📍 Plaża Kendwa"),
    "badge1_s": ("Meeting point • hotel pickup on request", "Miejsce spotkania • odbiór z hotelu na życzenie"),
    "badge2_t": ("🛥️ Private boat", "🛥️ Prywatna łódź"),
    "badge2_s": ("Comfort & flexibility", "Komfort i elastyczność"),
    "badge3_t": ("🤿 Snorkeling gear", "🤿 Sprzęt do snorkelingu"),
    "badge3_s": ("Included (most tours)", "W cenie (większość wycieczek)"),
    "glass_t": ("Popular:", "Popularne:"),
    "glass_a": ("Mnemba Snorkeling", "Snorkeling przy Mnemba"),
    "glass_b": ("Half-day", "Pół dnia"),
    "glass_s": ("Ask for availability & price (group/private).", "Zapytaj o dostępność i cenę (grupa/prywatnie)."),

    # trust
    "trust1_t": ("What you get", "Co otrzymujesz"),
    "trust1": (["Clear itinerary + start time confirmation", "Safety-first approach & life jackets",
                "Local knowledge (best spots depending on tide)", "Photo/video help on request"],
               ["Jasny plan i potwierdzenie godziny startu", "Bezpieczeństwo na pierwszym miejscu i kamizelki",
                "Lokalna wiedza (najlepsze miejsca zależnie od pływów)", "Pomoc przy zdjęciach/filmach na życzenie"]),
    "trust2_t": ("Perfect for", "Idealne dla"),
    "trust2": (["Families & couples", "Honeymoon & birthdays", "Small groups", "Chill + authentic Zanzibar vibes"],
               ["Rodzin i par", "Podróży poślubnych i urodzin", "Małych grup", "Relaksu i autentycznego klimatu Zanzibaru"]),
    "trust3_t": ("Languages", "Języki"),
    "trust3": (["English", "Polish (optional)", "Swahili"], ["Angielski", "Polski (opcjonalnie)", "Suahili"]),

    # how it works
    "how_h": ("How booking works", "Jak działa rezerwacja"),
    "how_s": ("Three simple steps — no agency, no middleman.", "Trzy proste kroki — bez agencji i pośredników."),
    "how1_t": ("Pick a tour", "Wybierz wycieczkę"),
    "how1": ("Choose a tour below or ask for a custom day.", "Wybierz wycieczkę poniżej lub poproś o plan na miarę."),
    "how2_t": ("Send your details", "Wyślij szczegóły"),
    "how2": ("Date, hotel, number of people — the form opens WhatsApp with your message ready.",
             "Data, hotel, liczba osób — formularz otworzy WhatsApp z gotową wiadomością."),
    "how3_t": ("Get confirmation", "Otrzymaj potwierdzenie"),
    "how3": ("Captain Busara replies with price, start time (tide-dependent) and meeting point.",
             "Kapitan Busara odpisze z ceną, godziną startu (zależnie od pływów) i miejscem spotkania."),

    # captain
    "cap_h": ("Meet Captain Busara", "Poznaj kapitana Busarę"),
    "cap_s": ("Local, authentic Zanzibar experience — you book directly with the captain.",
              "Lokalne, autentyczne doświadczenie Zanzibaru — rezerwujesz bezpośrednio u kapitana."),
    "cap_p1_h": ("Captain Busara is based on <strong>Kendwa Beach</strong> and knows these waters perfectly — "
                 "tides, hidden snorkeling spots, and the best time for a golden sunset cruise.",
                 "Kapitan Busara mieszka na <strong>plaży Kendwa</strong> i doskonale zna te wody — "
                 "pływy, ukryte miejsca do snorkelingu i najlepszą porę na złoty zachód słońca."),
    "cap_p2": ("No agency, no middleman. Just a friendly local captain, a great boat, and a perfect day in Zanzibar.",
               "Bez agencji i bez pośredników. Po prostu przyjazny lokalny kapitan, świetna łódź i idealny dzień na Zanzibarze."),
    "cap_cta": ("Message Captain Busara", "Napisz do kapitana Busary"),
    "cap_facts": ("Quick facts", "Najważniejsze"),
    "cap_f": (["📍 Kendwa Beach, Zanzibar", "🛟 Life jackets available", "🤿 Snorkeling gear (most tours)",
               "🌊 Best routes based on tides"],
              ["📍 Plaża Kendwa, Zanzibar", "🛟 Kamizelki ratunkowe", "🤿 Sprzęt do snorkelingu (większość wycieczek)",
               "🌊 Trasy dobierane do pływów"]),

    # tours
    "tours_h": ("Tours & experiences", "Wycieczki i atrakcje"),
    "tours_s": ("Choose a ready tour or message to build your custom day.",
                "Wybierz gotową wycieczkę lub napisz, a zaplanujemy dzień na miarę."),
    "f_all": ("All", "Wszystkie"),
    "f_sea": ("Sea & sandbanks", "Morze i mielizny"),
    "f_land": ("Nature & culture", "Natura i kultura"),
    "f_fun": ("Fun", "Atrakcje"),
    "card_go": ("Let’s go", "Chcę jechać"),
    "card_ask": ("Ask on WhatsApp", "Zapytaj na WhatsApp"),
    "from": ("from", "od"),
    "photo_soon": ("Photo coming soon", "Zdjęcie wkrótce"),
    "tours_note": ("* Every tour is priced individually — get in touch and we’ll tailor an offer to your needs and expectations.",
                   "* Każdą wycieczkę wyceniamy indywidualnie — skontaktuj się z nami, a dopasujemy ofertę do Twoich potrzeb i oczekiwań."),
    "custom_t": ("Custom Private Day", "Prywatny dzień na miarę"),
    "custom_d": ("Tell us your hotel location and what you want to see. We’ll build the best route based on tides and conditions.",
                 "Podaj lokalizację hotelu i co chcesz zobaczyć. Ułożymy najlepszą trasę zależnie od pływów i warunków."),
    "custom_l": (["Mnemba + snorkeling", "Turtles + sandbank", "Sunset + celebration"],
                 ["Mnemba + snorkeling", "Żółwie + mielizna", "Zachód słońca + świętowanie"]),
    "custom_cta": ("Plan my day", "Zaplanuj mój dzień"),

    # booking form
    "book_h": ("Request your tour", "Zapytaj o wycieczkę"),
    "book_s": ("Fill in the details — WhatsApp opens with your message ready to send.",
               "Uzupełnij szczegóły — WhatsApp otworzy się z gotową wiadomością."),
    "f_tour": ("Tour", "Wycieczka"),
    "f_date": ("Preferred date", "Preferowana data"),
    "f_people": ("People", "Liczba osób"),
    "f_hotel": ("Hotel / pickup place", "Hotel / miejsce odbioru"),
    "f_hotel_ph": ("e.g. Kendwa Rocks", "np. Kendwa Rocks"),
    "f_type": ("Type", "Rodzaj"),
    "f_private": ("Private", "Prywatna"),
    "f_group": ("Group", "Grupowa"),
    "f_any": ("Not sure yet", "Jeszcze nie wiem"),
    "f_name": ("Your name (optional)", "Twoje imię (opcjonalnie)"),
    "f_notes": ("Additional requests", "Dodatkowe wymagania"),
    "f_notes_ph": ("Kids’ age, celebration, dietary needs…", "Wiek dzieci, okazja, wymagania żywieniowe…"),
    "f_any_tour": ("Not sure — suggest something", "Nie wiem — zaproponujcie coś"),
    "f_submit": ("Continue on WhatsApp", "Przejdź do WhatsApp"),
    "f_preview": ("Your message", "Twoja wiadomość"),
    "f_copy": ("Copy", "Kopiuj"),
    "f_copied": ("Copied ✅", "Skopiowano ✅"),
    "f_copy_err": ("Copy manually", "Skopiuj ręcznie"),
    "f_hint": ("WhatsApp opens with your message ready — press send to submit. A booking is confirmed only after Captain Busara replies.",
               "WhatsApp otworzy się z gotową wiadomością — naciśnij „wyślij”. Rezerwacja jest potwierdzona dopiero po odpowiedzi kapitana Busary."),
    "f_noscript": ("Please use the WhatsApp button to send us your date, hotel and number of people.",
                   "Użyj przycisku WhatsApp i wyślij nam datę, hotel i liczbę osób."),
    # message templates (placeholders in {braces})
    "m_hi": ("Hi Captain Busara! I’d like to ask about / book: {tour}.", "Cześć, kapitanie Busara! Chciał(a)bym zapytać o / zarezerwować: {tour}."),
    "m_anytour": ("a tour in Zanzibar", "wycieczkę na Zanzibarze"),
    "m_date": ("Date: {v}", "Data: {v}"),
    "m_people": ("People: {v}", "Liczba osób: {v}"),
    "m_hotel": ("Hotel: {v}", "Hotel: {v}"),
    "m_type": ("Type: {v}", "Rodzaj: {v}"),
    "m_name": ("Name: {v}", "Imię: {v}"),
    "m_notes": ("Notes: {v}", "Uwagi: {v}"),
    "m_bye": ("Please tailor an offer for us (price and availability). Thanks!", "Poproszę o ofertę dopasowaną do naszych potrzeb (cena i dostępność). Dziękuję!"),
    "m_default": ("Hi! I’d like to book a tour in Zanzibar. Date: __/__/__. Hotel: ____. People: __. Which tours are available? Thanks!",
                  "Cześć! Chciał(a)bym zarezerwować wycieczkę na Zanzibarze. Data: __/__/__. Hotel: ____. Liczba osób: __. Jakie wycieczki są dostępne? Dziękuję!"),

    # gallery
    "gal_h": ("Gallery", "Galeria"),
    "gal_s": ("Zanzibar’s waters, sandbanks and island trails.", "Wody, mielizny i szlaki Zanzibaru."),
    "lb_close": ("Close", "Zamknij"),
    "lb_prev": ("Previous photo", "Poprzednie zdjęcie"),
    "lb_next": ("Next photo", "Następne zdjęcie"),

    # reviews
    "rev_h": ("What guests say", "Opinie gości"),
    "rev_s": ("Short feedback from travelers.", "Krótkie opinie podróżnych."),
    "rev_cta_h": ("Been on a tour with Captain Busara?", "Byłeś na wycieczce z kapitanem Busarą?"),
    "rev_cta_p": ("A short Google review helps other travelers choose — and helps a small local business grow.",
                  "Krótka opinia w Google pomaga innym podróżnym w wyborze i wspiera mały lokalny biznes."),
    "rev_btn": ("Write a Google review", "Napisz opinię w Google"),
    "rev_book": ("Book a tour", "Zarezerwuj wycieczkę"),

    # faq
    "faq_h": ("FAQ", "FAQ"),
    "faq_s": ("Frequently asked questions from travelers.", "Najczęstsze pytania od turystów."),

    # location
    "loc_h": ("How to find Captain Busara", "Jak znaleźć kapitana Busarę"),
    "loc_s": ("Kendwa Beach, Zanzibar — easy meeting point. Message us your hotel name on WhatsApp.",
              "Plaża Kendwa, Zanzibar — łatwe miejsce spotkania. Napisz nam na WhatsApp nazwę hotelu."),
    "loc_card": ("Meeting point", "Miejsce spotkania"),
    "loc_coords": ("Coordinates", "Współrzędne"),
    "loc_l": (["✅ We confirm the exact time based on tide & conditions", "✅ Hotel pickup can be arranged (ask on WhatsApp)",
               "✅ You book directly with the captain"],
              ["✅ Dokładną godzinę potwierdzamy zależnie od pływów i warunków", "✅ Odbiór z hotelu można zorganizować (zapytaj na WhatsApp)",
               "✅ Rezerwujesz bezpośrednio u kapitana"]),
    "loc_cta": ("Send hotel & date on WhatsApp", "Wyślij hotel i datę na WhatsApp"),
    "map_load": ("Show map", "Pokaż mapę"),
    "map_note": ("The map loads from Google when you click.", "Mapa załaduje się z Google po kliknięciu."),
    "map_open": ("Open in Google Maps", "Otwórz w Mapach Google"),
    "map_title": ("Kendwa Beach – Captain Busara meeting point", "Plaża Kendwa – miejsce spotkania z Captain Busara"),

    # contact + footer
    "con_h": ("Contact & booking", "Kontakt i rezerwacja"),
    "con_p_h": ("Fastest way: WhatsApp. Send: <strong>date</strong>, <strong>hotel</strong>, <strong>number of people</strong> and which tour.",
                "Najszybciej przez WhatsApp. Wyślij: <strong>datę</strong>, <strong>hotel</strong>, <strong>liczbę osób</strong> i wybraną wycieczkę."),
    "con_wa": ("Message on WhatsApp", "Napisz na WhatsApp"),
    "con_call": ("Call", "Zadzwoń"),
    "con_loc_t": ("📍 Location", "📍 Lokalizacja"),
    "con_loc": ("Kendwa Beach, north Zanzibar", "Plaża Kendwa, północny Zanzibar"),
    "con_hours_t": ("🕘 Hours", "🕘 Godziny"),
    "con_hours_s": ("Fast reply on WhatsApp", "Szybka odpowiedź na WhatsApp"),
    "con_safe_t": ("🛟 Safety", "🛟 Bezpieczeństwo"),
    "con_safe": ("Life jackets • Local captain", "Kamizelki ratunkowe • Lokalny kapitan"),
    "rights": ("All rights reserved.", "Wszelkie prawa zastrzeżone."),
    "privacy": ("Privacy", "Prywatność"),
    "wa_sticky": ("Book on WhatsApp", "Rezerwacja WhatsApp"),
    "wa_aria": ("Book on WhatsApp", "Zarezerwuj przez WhatsApp"),
    "call_aria": ("Call Captain Busara", "Zadzwoń do kapitana Busary"),

    # 404
    "nf_h": ("Page not found", "Nie znaleziono strony"),
    "nf_p": ("This page doesn’t exist — but the sea is still there.", "Takiej strony nie ma — ale morze wciąż czeka."),
    "nf_btn": ("Back to the homepage", "Wróć na stronę główną"),
}

# ---------------------------------------------------------------- Tours
# cat: sea | land | fun.   img: key from IMAGES (None = no photo yet)
# price: None or e.g. "$60" -> shown as "from $60" on the card (add real prices here when confirmed)
TOURS = [
    dict(id="mnemba", cat="sea", img="mnemba-island", price=None,
         alt=("Aerial view of Mnemba Island with a traditional dhow", "Widok z lotu ptaka na wyspę Mnemba z tradycyjną łodzią dhow"),
         title=("Mnemba Island Snorkeling & Dolphins", "Snorkeling przy Mnemba i delfiny"),
         desc=("Crystal water, colorful fish and coral spots around Mnemba. Dolphin sightings depend on the day. Best time depends on the tide.",
               "Krystalicznie czysta woda, kolorowe ryby i rafy wokół Mnemba. Delfiny widujemy zależnie od dnia. Najlepsza pora zależy od pływów."),
         meta=[("⏱️", ("4–5h", "4–5 h")), ("🤿", ("Gear", "Sprzęt")), ("🚗", ("Pickup (optional)", "Odbiór (opcjonalnie)"))]),
    dict(id="sandbank", cat="sea", img="sandbank", price=None,
         alt=("Boats anchored at a white sandbank in turquoise water", "Łodzie przy białej mieliźnie w turkusowej wodzie"),
         title=("Mnemba Sandbank", "Piaszczysta mielizna przy Mnemba"),
         desc=("Walk barefoot on a pale sandbank surrounded by turquoise water — a classic Zanzibar photo stop. Timing depends on the tide.",
               "Spacer boso po jasnej mieliźnie otoczonej turkusową wodą — klasyczny przystanek na zdjęcia na Zanzibarze. Godzina zależy od pływów."),
         meta=[("🏝️", ("Sandbank", "Mielizna")), ("🏊", ("Swimming", "Kąpiel")), ("📸", ("Photos", "Zdjęcia"))]),
    dict(id="starfish", cat="sea", img="starfish", contain=True, price=None,
         alt=("Starfish on the sand in shallow turquoise water", "Rozgwiazdy na piasku w płytkiej turkusowej wodzie"),
         title=("Starfish Sandbank", "Mielizna z rozgwiazdami"),
         desc=("Discover a different side of Zanzibar in shallow turquoise water. Ask Busara about a visit to a sandbank and the chance to observe starfish in their natural surroundings. Please look, don’t lift — starfish stay in the water.",
               "Odkryj inne oblicze Zanzibaru w płytkiej, turkusowej wodzie. Zapytaj Busarę o wizytę na mieliźnie i możliwość obserwowania rozgwiazd w ich naturalnym otoczeniu. Prosimy: patrzymy, nie wyciągamy — rozgwiazdy zostają w wodzie."),
         meta=[("🏝️", ("Sandbank", "Mielizna")), ("🌿", ("Nature", "Natura")), ("🌊", ("Ocean", "Ocean"))]),
    dict(id="turtles", cat="sea", img="baraka-turtles", price=None,
         alt=("Green sea turtles swimming in shallow water", "Żółwie zielone pływające w płytkiej wodzie"),
         title=("Turtle Experience", "Żółwie – spotkanie z bliska"),
         desc=("Meet and learn about sea turtles. Great for families & kids.",
               "Poznaj żółwie morskie i dowiedz się o nich więcej. Świetne dla rodzin z dziećmi."),
         meta=[("⏱️", ("2–4h", "2–4 h")), ("👨‍👩‍👧‍👦", ("Family", "Rodzina")), ("📍", ("Local spot", "Lokalne miejsce"))]),
    dict(id="sunset", cat="sea", img="sunset-dhow", price=None,
         alt=("Silhouette of a dhow sailing into the sunset", "Sylwetka łodzi dhow na tle zachodu słońca"),
         title=("Sunset Cruise", "Rejs o zachodzie słońca"),
         desc=("Golden hour on the ocean — perfect for couples, birthdays and chill vibes.",
               "Złota godzina na oceanie — idealna dla par, urodzin i relaksu."),
         meta=[("⏱️", ("2–3h", "2–3 h")), ("🌅", ("Sunset", "Zachód słońca")), ("🥂", ("Drinks (optional)", "Napoje (opcjonalnie)"))]),
    dict(id="jozani", cat="land", img="jozani-colobus", price=None,
         alt=("Zanzibar red colobus monkey in Jozani Forest", "Gereza rudy w lesie Jozani"),
         title=("Jozani Forest", "Las Jozani"),
         desc=("Swap the beach for a greener side of Zanzibar. Discover forest scenery, mangrove walkways and the island’s red colobus monkeys.",
               "Zamień plażę na zielone oblicze Zanzibaru. Odkryj leśne krajobrazy, kładki wśród namorzynów i gerezy rude."),
         meta=[("🌳", ("Forest", "Las")), ("🌿", ("Mangroves", "Namorzyny")), ("🐒", ("Wildlife", "Dzika przyroda"))]),
    dict(id="spice", cat="land", img="spice-fruit", price=None,
         alt=("Fresh spice fruit with red seeds held in a hand", "Świeży owoc przyprawy z czerwonymi nasionami w dłoni"),
         title=("Spice Farm", "Plantacja przypraw"),
         desc=("See Zanzibar beyond the beach. Explore the colours and aromas of a spice farm, with time to discover the plants behind familiar flavours.",
               "Poznaj Zanzibar poza plażą. Odkryj kolory i aromaty plantacji przypraw oraz rośliny, z których pochodzą dobrze znane smaki."),
         meta=[("🌶️", ("Spices", "Przyprawy")), ("🌱", ("Plants", "Rośliny")), ("🧭", ("Island discovery", "Odkrywanie wyspy"))]),
    dict(id="stonetown", cat="land", img="stone-town", price=None,
         alt=("A narrow lane in Stone Town with market stalls", "Wąska uliczka w Stone Town z straganami"),
         title=("Stone Town", "Stone Town"),
         desc=("Follow the narrow lanes, carved doorways and everyday scenes of Stone Town. Ask Busara to help plan a walk through this characterful side of Zanzibar.",
               "Odkryj wąskie uliczki, rzeźbione drzwi i codzienne życie Stone Town. Zapytaj Busarę o spacer po tej pełnej charakteru części Zanzibaru."),
         meta=[("🚶", ("Walking", "Spacer")), ("🏛️", ("Architecture", "Architektura")), ("🏘️", ("Local atmosphere", "Lokalny klimat"))]),
    dict(id="kayak", cat="fun", img="kayak-flowers", price=None,
         alt=("Woman lying in a transparent kayak decorated with flowers, seen from above", "Kobieta leżąca w przezroczystym kajaku z kwiatami, widok z góry"),
         title=("Clear Kayak", "Przezroczysty kajak"),
         desc=("Turquoise water, a transparent kayak and a fresh perspective on your Zanzibar holiday. Ask Busara about a clear kayak photo experience for your preferred date.",
               "Turkusowa woda, przezroczysty kajak i nowe spojrzenie na wakacje na Zanzibarze. Zapytaj Busarę o sesję zdjęciową w kajaku w wybranym terminie."),
         meta=[("🛶", ("Clear kayak", "Przezroczysty kajak")), ("📸", ("Photos", "Zdjęcia")), ("🌊", ("Ocean", "Ocean"))]),
    dict(id="watercar", cat="fun", img="water-car", price=None,
         alt=("Yellow car-shaped water vehicle racing across turquoise water, seen from above", "Żółty pojazd wodny w kształcie samochodu na turkusowej wodzie, widok z góry"),
         title=("Water Car", "Samochód wodny"),
         desc=("Take your Zanzibar adventure onto the water in a car-shaped boat. Ask Busara about availability and the experience options for your group.",
               "Przenieś swoją przygodę na Zanzibarze na wodę w łodzi przypominającej samochód. Zapytaj Busarę o dostępność i warianty atrakcji dla Twojej grupy."),
         meta=[("🚗", ("Water car", "Samochód wodny")), ("🌊", ("Ocean", "Ocean")), ("⚡", ("Adventure", "Przygoda"))]),
    dict(id="horse", cat="fun", img=None, price=None,
         alt=("", ""), icon="🐎",
         title=("Horse Riding (Beach)", "Jazda konna (plaża)"),
         desc=("Beach ride experience (partner activity). We help organize transport & time slot.",
               "Przejażdżka konna po plaży (atrakcja partnerska). Pomagamy zorganizować transport i termin."),
         meta=[("⏱️", ("1–2h", "1–2 h")), ("🐎", ("Horse", "Konie")), ("🧭", ("Guided", "Z przewodnikiem"))]),
]

# ---------------------------------------------------------------- Gallery
GALLERY = [
    ("mnemba-island", ("Mnemba Island and a traditional dhow", "Wyspa Mnemba i tradycyjna łódź dhow")),
    ("dolphins", ("Dolphins near Mnemba", "Delfiny w okolicach Mnemba")),
    ("baraka-turtles", ("Sea turtles at Baraka", "Żółwie morskie w Baraka")),
    ("sunset-dhow", ("Sunset under sail", "Zachód słońca pod żaglem")),
    ("kayak-flowers", ("Clear kayak with flowers", "Przezroczysty kajak z kwiatami")),
    ("salaam-turtles", ("Turtles in Salaam Cave", "Żółwie w jaskini Salaam")),
    ("mnemba-aerial", ("Mnemba from above", "Mnemba z lotu ptaka")),
    ("jozani-colobus", ("Red colobus in Jozani Forest", "Gereza rudy w lesie Jozani")),
    ("safari-lagoon", ("Snorkeling in a calm lagoon", "Snorkeling w spokojnej lagunie")),
    ("water-car", ("Water car adventure", "Przygoda samochodem wodnym")),
    ("kayak-couple", ("Clear kayak for two", "Przezroczysty kajak dla dwojga")),
    ("hero-boat", ("Relaxing on the boat", "Relaks na pokładzie łodzi")),
]

# ---------------------------------------------------------------- Reviews
# Only entries with verified=True are shown on the site. Set verified=True once you've confirmed
# the review is real (ideally a copy of a Google review). Never publish invented reviews.
# Add only real, verified guest reviews here: dict(verified=True, name=..., country=(EN, PL), text=(EN, PL))
REVIEWS = []

# ---------------------------------------------------------------- FAQ
FAQ = [
    (("What should I bring?", "Co zabrać ze sobą?"),
     ("Sunscreen, towel, water, hat, sunglasses. For snorkeling: you can bring your own mask, but we provide gear on most tours.",
      "Krem z filtrem, ręcznik, wodę, kapelusz i okulary przeciwsłoneczne. Do snorkelingu możesz zabrać własną maskę, ale na większości wycieczek zapewniamy sprzęt.")),
    (("Is it safe for kids?", "Czy to bezpieczne dla dzieci?"),
     ("Yes — we adapt the pace and stops. Life jackets available. Tell us kids’ age when booking.",
      "Tak — dostosowujemy tempo i przystanki. Kamizelki ratunkowe są dostępne. Podaj wiek dzieci przy rezerwacji.")),
    (("Do you offer hotel pickup?", "Czy organizujecie odbiór z hotelu?"),
     ("Pickup can be arranged depending on location and tour. Message your hotel name on WhatsApp.",
      "Odbiór można zorganizować w zależności od lokalizacji i wycieczki. Napisz nam nazwę hotelu na WhatsApp.")),
    (("How do I pay?", "Jak mogę zapłacić?"),
     ("Cash is common. If you want card transfer options, ask on WhatsApp and we’ll confirm what’s available.",
      "Najczęściej płaci się gotówką. Jeśli wolisz przelew lub kartę, zapytaj na WhatsApp — potwierdzimy dostępne opcje.")),
    (("How does booking work?", "Jak wygląda rezerwacja?"),
     ("Choose a tour and send your date, hotel and number of people on WhatsApp (the form on this page prepares the message for you). Captain Busara replies with price and start time. A booking is confirmed only after he replies.",
      "Wybierz wycieczkę i wyślij na WhatsApp datę, hotel i liczbę osób (formularz na tej stronie przygotuje wiadomość). Kapitan Busara odpisze z ceną i godziną startu. Rezerwacja jest potwierdzona dopiero po jego odpowiedzi.")),
    (("Does the weather or tide change the plan?", "Czy pogoda lub pływy zmieniają plan?"),
     ("Routes and timing depend on tide and sea conditions, so we confirm the exact start time with you before the tour.",
      "Trasa i godzina zależą od pływów i warunków na morzu, dlatego dokładną godzinę startu potwierdzamy z Tobą przed wycieczką.")),
    (("Which languages do you speak?", "W jakich językach się porozumiewacie?"),
     ("English, Swahili, and Polish (optional).", "Po angielsku, suahili i — opcjonalnie — po polsku.")),
]

# ---------------------------------------------------------------- Privacy page
PRIVACY = {
    "title": ("Privacy | Captain Busara", "Prywatność | Captain Busara"),
    "h": ("Privacy notice", "Informacja o prywatności"),
    "updated": ("Last updated: 22 November 2026", "Ostatnia aktualizacja: 22 listopada 2026"),
    "blocks": [
        (("What this website collects", "Co zbiera ta strona"),
         ("This website does not use advertising cookies or trackers. It does not store the information you type in the request form on a server: "
          "the form only prepares a WhatsApp message in your browser.",
          "Ta strona nie używa reklamowych plików cookie ani trackerów. Dane wpisane w formularzu zapytania nie są zapisywane na serwerze: "
          "formularz tylko przygotowuje wiadomość WhatsApp w Twojej przeglądarce.")),
        (("WhatsApp", "WhatsApp"),
         ("When you press “Continue on WhatsApp”, you are taken to WhatsApp. What you send there is handled by Captain Busara and by WhatsApp under WhatsApp’s own privacy policy. "
          "We use your details (date, hotel, number of people, name) only to answer your request and organise the tour.",
          "Po kliknięciu „Przejdź do WhatsApp” przechodzisz do aplikacji WhatsApp. To, co tam wyślesz, trafia do kapitana Busary i podlega polityce prywatności WhatsApp. "
          "Twoje dane (data, hotel, liczba osób, imię) wykorzystujemy wyłącznie do odpowiedzi na zapytanie i organizacji wycieczki.")),
        (("Google Maps", "Mapy Google"),
         ("The map is loaded from Google only after you click “Show map”. Google may then set cookies under its own policy.",
          "Mapa ładuje się z Google dopiero po kliknięciu „Pokaż mapę”. Google może wtedy zapisać pliki cookie zgodnie z własną polityką.")),
        (("Fonts and images", "Czcionki i obrazy"),
         ("Fonts are loaded from Google Fonts. Images are served from this website.",
          "Czcionki ładują się z Google Fonts. Obrazy są serwowane z tej strony.")),
        (("Analytics", "Analityka"),
         ("If cookieless, privacy-friendly analytics (Plausible) is switched on, it counts visits and button clicks without cookies and without personal profiles.",
          "Jeśli włączona jest analityka bez plików cookie (Plausible), liczy ona odwiedziny i kliknięcia przycisków bez cookies i bez profili osobowych.")),
        (("Contact", "Kontakt"),
         ("Questions about your data: message Captain Busara on WhatsApp or call the number shown on the website.",
          "Pytania o dane: napisz do kapitana Busary na WhatsApp lub zadzwoń pod numer podany na stronie.")),
    ],
}
