# Captain Busara – captainbusara.com

Statyczna strona (GitHub Pages, domena w pliku `CNAME`) w wersji EN (`/`) i PL (`/pl/`).

## Jak zmieniać treści
Teksty, wycieczki, FAQ, opinie, galeria i dane kontaktowe są w **`tools/content.py`** (każdy tekst: `(angielski, polski)`).
Po zmianie uruchom:

```bash
python3 tools/build.py
```

Skrypt generuje `index.html`, `pl/index.html`, `privacy.html`, `pl/privacy.html`, `404.html`, `sitemap.xml`, `robots.txt`
i `site.webmanifest`. Nie edytuj tych plików ręcznie – zostaną nadpisane. Wygląd: `styles.css`, zachowanie: `script.js`.

## Do uzupełnienia / potwierdzenia przed publikacją
- **Ceny** – w `TOURS` ustaw `price="$60"` przy wycieczce (na karcie pojawi się „od $60”). Puste = bez ceny.
- **Opinie** – wpisy w `REVIEWS` mają `verified=False` i nie są pokazywane. Ustaw `True` dopiero dla prawdziwych opinii (najlepiej skopiowanych z Google).
- **Zdjęcia** – prawa do publikacji nie są potwierdzone (patrz raport Inbox Review w Dysku). Nie używaj zdjęć z widocznym znakiem wodnym/podpisem fotografa.
- **Zdjęcie jazdy konnej** – brak; karta ma placeholder. Dodaj plik w `images/` i wpisz klucz w `TOURS` oraz wymiary w `IMAGES`.
- **Analityka** – opcjonalnie wpisz domenę Plausible w `SITE["analytics_domain"]` (domyślnie wyłączona).
- **Polityka prywatności** – tekst ogólny, do przejrzenia przez właściciela.
