# Asiatische Hornisse – Website (Schädlingsbekämpfung, Köln/Bonn/Rhein-Sieg)

Statische One-Page-Website (HTML/CSS/JS, kein Framework, kein Backend) zur Entfernung von Nestern der
Asiatischen Hornisse (*Vespa velutina*). Layout und Typografie basieren auf der Fotografie-Website
(`michaelfalkner-fotografie`), mit einem warmen Bernstein-Akzent.

Live: https://mike21getit.github.io/asiatische-hornisse/

## Struktur

```
index.html              Alle Inhalte inkl. Impressum (#impressum) und Datenschutz (#datenschutz)
css/style.css           Handgeschriebenes CSS (mobile first)
js/main.js              Navigation, Scrollspy, Einblend-Animationen, mailto-Anfrageformular
fonts/                  Cormorant Garamond (SIL Open Font License), lokal eingebunden
img/*.svg               Eigene Illustrationen (Hornissen, Nester, Hero)
img/og-image.png        Vorschaubild für Social Media (1200×630)
favicon.svg, favicon-32.png, apple-touch-icon.png
tools/make_svgs.py      Erzeugt die SVG-Illustrationen und das Favicon neu
tools/screenshot.py     Ganzseiten-Screenshot per Headless Chrome (benötigt websocket-client)
```

## Platzhalter – bitte ersetzen

Alle Platzhalter stehen in **eckigen Klammern** und sind auf der Seite orange markiert (Klasse `ph`).
Suchen mit: `grep -n '\[' index.html`

| Platzhalter | Wo | Hinweis |
|---|---|---|
| `[Firmenname]` | Logo, Texte, Impressum, Datenschutz, Footer, `<title>`, Meta-Tags, JSON-LD | 13× in index.html |
| `[Rechtsform]` | Impressum | z. B. Einzelunternehmen, GmbH |
| `[Inhaber]` | Impressum, Datenschutz | Vor- und Nachname |
| `[Telefon]` | Navigation, Hero-Button, Kontakt, Impressum, Datenschutz, JSON-LD | In `href="tel:[Telefon]"` im internationalen Format **ohne Leerzeichen** eintragen, z. B. `tel:+492223123456`; im sichtbaren Text gern lesbar formatiert |
| `[E-Mail]` | Kontakt, Impressum, Datenschutz, `href="mailto:[E-Mail]"`, `data-mailto="[E-Mail]"` am Formular, JSON-LD | Möglicherweise `mail@falkner-sbk.de` – **nicht verifiziert, bitte prüfen** |
| `[Straße Hausnummer]`, `[PLZ Ort]` | Impressum, Datenschutz, Über uns, JSON-LD | |
| `[Einsatzgebiet]` | Leistungen, Über uns, Kontakt, JSON-LD (`areaServed`) | z. B. „Königswinter, Bonn, Köln, Rhein-Sieg-Kreis“ |
| `[USt-IdNr. …]` | Impressum | sonst Abschnitt löschen |
| `[Handelsregister, … Handwerksrolle …]` | Impressum | nur falls zutreffend |
| `[Name und Sitz des Versicherers …]` | Impressum (Berufshaftpflicht) | nur falls Pflicht/gewünscht |
| `[Sachkunde / Zertifikate]` | Über uns | |
| `[Kurzer Text zu Inhaber …]` | Über uns | |
| `[Maximale Arbeitshöhe / eigene Technik ergänzen]` | Leistungen → Einsätze in der Höhe | nur tatsächlich vorhandene Technik nennen |
| `[Erreichbarkeit, z. B. Mo–Sa 8–18 Uhr]` | Kontakt | |
| `[Bitte an die tatsächliche Praxis anpassen]` | Datenschutz, Abschnitt 5 | |
| `[Eigene Fotos: © Firmenname]` | Impressum → Bildnachweis | nach Einbau eigener Fotos |
| `[FOTO 1]`, `[FOTO 2]`, `[FOTO 3]`, `[FOTO INHABER]` | Ablauf, Über uns | siehe unten |

Platzhalter in Attributen und Kopfbereich nicht vergessen: `<title>`, `meta description`, Open-Graph-Tags,
JSON-LD (`<script type="application/ld+json">`), `tel:`/`mailto:`-Links, `data-mailto` am Formular.
Nach dem Ersetzen die Klasse `ph` am jeweiligen `<span>` entfernen (sonst bleibt der Text orange unterstrichen).

## Eigene Fotos einsetzen

Fotoplätze sind `<figure class="photo-slot">…</figure>` mit Kommentar `<!-- FOTO … -->`. Ersetzen durch z. B.:

```html
<figure class="photo"><img src="img/einsatz-1.jpg" alt="Kurze Beschreibung" width="1200" height="900" loading="lazy"></figure>
```

Nur Fotos verwenden, an denen Sie die Rechte haben (am besten eigene). Keine Stockfotos mit unklarer Lizenz.

## Cache-Busting

CSS/JS werden mit `?v=…` eingebunden (`css/style.css?v=20261031b`, `js/main.js?v=20261031b`).
Nach jeder Änderung an CSS/JS den Wert in `index.html` erhöhen (z. B. `20261101a`).

## Eigene Domain

Bei Umzug auf eine eigene Domain `canonical`, `og:url`, `og:image` und `url` im JSON-LD anpassen
(derzeit `https://mike21getit.github.io/asiatische-hornisse/`) und ggf. eine `CNAME`-Datei anlegen.

## Formular

Kein Server: Das Formular baut eine E-Mail (mailto:) im E-Mail-Programm des Besuchers zusammen. Es werden
keine Daten an die Website übertragen. Fotos hängt der Besucher selbst an.

## Bildnachweis

Alle Illustrationen und Icons sind eigens erstellte SVGs (siehe `tools/make_svgs.py`). Schrift:
Cormorant Garamond, SIL Open Font License, lokal gehostet. Keine externen Ressourcen, keine Cookies.

## Quellen der Fachinhalte (abgerufen 31.10.2026)

- LANUK NRW, Neobiota-Portal – Artsteckbrief: https://neobiota.naturschutzinformationen.nrw.de/neobiota/de/arten/tiere/190771
- LANUK NRW – Maßnahmen: https://neobiota.naturschutzinformationen.nrw.de/neobiota/de/arten/tiere/190771/massnahmen
- Meldeformular: https://neobiota.naturschutzinformationen.nrw.de/neobiota/de/fundpunkte/webformular
- Hinweise zur Fundmeldung: https://neobiota.naturschutzinformationen.nrw.de/neobiota/de/fundpunkte/erfassung
- Rhein-Sieg-Kreis: https://www.rhein-sieg-kreis.de/mobilitaet-umwelt/natur-energie/asiatische-hornisse.php
- Rhein-Sieg-Kreis, Naturschutztelefon: https://www.rhein-sieg-kreis.de/vv/produkte/Amt_66/Abteilung_66.3/Naturschutztelefon.php
- Verordnung (EU) Nr. 1143/2014: https://eur-lex.europa.eu/eli/reg/2014/1143/oj

Rechtliche Hinweise und Meldewege regelmäßig prüfen – sie können sich ändern (Stand im Text: Oktober 2026).
