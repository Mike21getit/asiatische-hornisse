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
img/hero-vespa-solo*.webp  Startbild (eigenes Foto, 2000 + 1000 px, quadratisch)
img/foto-crabro.webp    Einziges verbliebenes Fremdfoto (Wikimedia Commons, siehe „Bildnachweis“)
img/eigen-*.webp        Eigene Fotos (Michael Falkner), je 2000 px (lange Kante) + -800; dazu 3 Video-Poster
video/*.mp4             Eigene Videos (H.264, 720×1280, ohne Ton, Metadaten entfernt):
                        nest-badezimmer, nest-badezimmer-flugloch, nest-fensterrahmen
img/og-image.jpg        Vorschaubild für Social Media (1200×630, mit eigenem Hero-Foto vespa-solo)
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
| `[FOTO 3]`, `[FOTO INHABER]` | Ablauf, Über uns | siehe unten (FOTO 1 + 2 sind mit eigenen Fotos belegt) |

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

CSS/JS werden mit `?v=…` eingebunden (`css/style.css?v=20261101d`, `js/main.js?v=20261101d`).
Nach jeder Änderung an CSS/JS den Wert in `index.html` erhöhen (z. B. `20261101e`).

## Eigene Domain

Bei Umzug auf eine eigene Domain `canonical`, `og:url`, `og:image` und `url` im JSON-LD anpassen
(derzeit `https://mike21getit.github.io/asiatische-hornisse/`) und ggf. eine `CNAME`-Datei anlegen.

## Formular

Kein Server: Das Formular baut eine E-Mail (mailto:) im E-Mail-Programm des Besuchers zusammen. Es werden
keine Daten an die Website übertragen. Fotos hängt der Besucher selbst an.

## Bildnachweis

**Eigene Fotos und Videos** © [Firmenname]/Michael Falkner. Exif-/GPS-Daten und Video-Metadaten wurden beim
Konvertieren entfernt. Bildunterschriften beschreiben nur, was zu sehen ist (keine Orts-/Datumsangaben).

| Datei | Verwendung | Original (Drive „Vespa Velutina“) |
|---|---|---|
| `img/hero-vespa-solo.webp`, `img/hero-vespa-solo-1000.webp`, `img/og-image.jpg` | Startbild, Social-Media-Vorschau (ersetzt Stockfoto Vassen) | vespa-solo.jpg |
| `img/eigen-velutina.webp` | Erkennen – Fotovergleich Asiatische Hornisse (Ausschnitt, ersetzt Stockfoto Sharp) | velutina-01.jpg |
| `img/eigen-velutina-nest(-800).webp` | Galerie – Asiatische Hornissen auf der Nesthülle | velutina-01.jpg |
| `img/eigen-waben-hornissen(-800).webp` | Galerie – Hornissen auf einer Wabe | Wabe.jpg |
| `img/eigen-waben-puppen(-800).webp` | Galerie – geöffnete Wabenetagen mit verdeckelten Zellen | Wabe-2.jpg |
| `img/eigen-nest-fenster(-800).webp` | Galerie – Nest in einer Fensterlaibung | IMG_5958 2.JPG |
| `img/eigen-nest-fensterrahmen(-800).webp` | Nester – Fotopaar links: Sekundärnest an einem Fensterrahmen (dasselbe Nest wie im Video `nest-fensterrahmen`; ersetzt Stockfoto Ithurburu) | IMG_9848 2.JPG |
| `img/eigen-nest-baumkrone(-800).webp` | Nester – Fotopaar rechts | IMG_6398 2.JPG |
| `img/eigen-nest-badezimmer(-800).webp` | Galerie – Nest an der Duschvorhangstange im Badezimmer | IMG_0266.jpg |
| `img/eigen-hornissen-nahaufnahme(-800).webp` | Galerie – Arbeiterinnen auf der Nesthülle | IMG_0275.jpg |
| `img/eigen-nest-offen-baum(-800).webp` | Galerie – Nest im Baum mit offener Hülle | IMG_6406.JPG |
| `img/eigen-waben-wiese(-800).webp` | Galerie – geöffnetes Nest auf einer Wiese | IMG_6408 2.JPG |
| `img/eigen-waben-boden(-800).webp` | Galerie – Wabenetagen am Boden | IMG_6401.JPG |
| `img/eigen-hornissen-am-nest(-800).webp` | Ablauf – Fotoplatz 1 | IMG_0275.jpg (16:9-Ausschnitt) |
| `img/eigen-flugloch(-800).webp` | Ablauf – Fotoplatz 2 | vespa-01.jpg |
| `video/nest-badezimmer.mp4` + `img/eigen-video-poster.webp` | Praxis-Block „Nest im Badezimmer“, Video 1 (18 s, 3,5 MB) | IMG_0270.MP4 (inhaltsgleich mit „Automatic 3.MP4“) |
| `video/nest-badezimmer-flugloch.mp4` + `img/eigen-video2-poster.webp` | Praxis-Block „Nest im Badezimmer“, Video 2 (47 s, 6,5 MB) | 1080p_Match_Framerate.MP4 |
| `video/nest-fensterrahmen.mp4` + `img/eigen-video-fensterrahmen-poster.webp` | Rubrik „Sekundärnest“ (`#sekundaernest`, in der Navigation), Sekundärnest an einem Fensterrahmen (19 s, 5,9 MB) | Automatic-03.MP4 (bearbeitete Fassung von IMG_9853.MP4) |

Die Galerie nutzt die Lightbox der Fotografie-Seite (Tastatur ←/→/Esc, Wischen auf Touch-Geräten); neue Bilder
einfach als weiteres `<li class="g-item">` in `#gallery` ergänzen (`href` = große Datei, `data-w`/`data-h`/`data-caption`).

Fremdfoto von Wikimedia Commons (frei lizenziert, Artbestimmung geprüft). Es wurde zugeschnitten, verkleinert und
als WebP gespeichert. Der Nachweis steht auch auf
der Seite im Impressum unter „Bildnachweise“ (`#bildnachweise`) und als Kurzzeile an jedem Foto.
**Wer ein Foto austauscht oder entfernt, muss den Nachweis an beiden Stellen anpassen.**

| Datei | Verwendung | Original | Urheber | Lizenz |
|---|---|---|---|---|
| `img/foto-crabro.webp` | Erkennen – Fotovergleich | [Frelon européen (Vespa crabo), Parc de Woluwé, Bruxelles](https://commons.wikimedia.org/wiki/File:Frelon_europ%C3%A9en_(Vespa_crabro),_Parc_de_Woluw%C3%A9,_Bruxelles_(51791202897).jpg) | Frank Vassen | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) |

Alle übrigen Illustrationen und Icons sind eigens erstellte SVGs (siehe `tools/make_svgs.py`). Schrift:
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
