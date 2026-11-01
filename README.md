# Asiatische Hornisse – Website der Falkner Schädlingsbekämpfung GmbH (Bonn/Köln/Rhein-Sieg · Mannheim/Rhein-Neckar)

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
img/hero-velutina*.webp Startbild – TEST seit 01.11.2026 (eigenes Foto „velutina-01“, 2000 + 1000 px, quadratisch)
img/hero-start*.webp    Bisheriges Startbild „start“ (2000 + 1000 px, 3:2) – bleibt für schnellen Rücktausch im Repo
img/erkennen-crabro*.webp  Bild neben der Zeichnung der Europäischen Hornisse (Erkennen), KI-generiert (Drive „Vespa Crabo.JPG“), 1152 + 800 px
img/hero-vespa-solo*.webp  Foto neben der Zeichnung der Asiatischen Hornisse (Erkennen), 2000 + 1000 px
img/foto-crabro.webp    Einziges verbliebenes Fremdfoto (Wikimedia Commons, siehe „Bildnachweis“)
img/eigen-*.webp        Eigene Fotos (Michael Falkner), je 2000 px (lange Kante) + -800; dazu 3 Video-Poster
video/*.mp4             Eigene Videos (H.264 High, 1080×1920, CRF 21/24, faststart, ohne Ton, Metadaten entfernt):
                        nest-badezimmer, nest-badezimmer-flugloch, nest-fensterrahmen
img/og-image.jpg        Vorschaubild für Social Media (1200×630, mit eigenem Hero-Foto „start“)
favicon.ico, favicon-32.png, apple-touch-icon.png (Grasmarke aus dem Logo; favicon.svg alt, nicht eingebunden)
img/logo/               Firmenlogo: Original-JPG + transparente PNG/WebP (hochkant/quer, original/hell), Icons
tools/make_svgs.py      Erzeugt die SVG-Illustrationen und das Favicon neu
tools/screenshot.py     Ganzseiten-Screenshot per Headless Chrome (benötigt websocket-client)
```

## Firmendaten (eingetragen am 01.11.2026)

| Feld | Wert | Wo |
|---|---|---|
| Firmenname / Rechtsform | Falkner Schädlingsbekämpfung GmbH | Header-Logo (aria-label), Texte, Impressum, Datenschutz, Footer, `<title>`, Meta/OG, JSON-LD, Bildnachweise |
| Standort Bonn | 53225 Bonn · 0228 4336945 (`tel:+492284336945`) | Navigation, Hero, Kontakt, Impressum, Datenschutz, JSON-LD |
| Standort Mannheim | Neuhofer Straße 15, 68219 Mannheim · 0621 72492117 (`tel:+4962172492117`) | Hero, Kontakt, Impressum (Anschrift), Datenschutz (Verantwortlicher), JSON-LD |
| E-Mail | mail@falkner-sbk.de | Kontakt, Formular (`data-mailto`/`action`), Impressum, Datenschutz, JSON-LD |
| Hauptwebsite | https://www.falkner-sbk.de | Mobile-Menü, Über uns, Kontakt, Impressum, Footer, JSON-LD `sameAs` |
| Einsatzgebiet | Region Bonn / Rhein-Sieg / Köln und Region Mannheim / Rhein-Neckar | Leistungen, Über uns, Kontakt, Footer, JSON-LD `areaServed` – **bitte bestätigen** |

Hinweis: `img/og-image.jpg` enthält noch den eingebrannten Text „KÖLN · BONN · RHEIN-SIEG“ (ohne Mannheim).

## Platzhalter – noch offen

Alle Platzhalter stehen in **eckigen Klammern** und sind auf der Seite orange markiert (Klasse `ph`).
Suchen mit: `grep -n 'class="ph"' index.html`

| Platzhalter | Wo | Hinweis |
|---|---|---|
| `[Sitz der Gesellschaft bitte bestätigen …]` | Impressum | Anschrift ist vorläufig Mannheim; laut Handelsregister prüfen |
| `[Geschäftsführer]` | Impressum (Vertreten durch), Datenschutz | Vor- und Nachname laut Handelsregister |
| `[Geschäftsführer / verantwortliche Person]` | Impressum (§ 18 Abs. 2 MStV) | |
| `[Registergericht …]`, `[HRB-Nummer]` | Impressum (Registereintrag) | Pflichtangabe für GmbH |
| `[USt-IdNr.]` | Impressum | falls vorhanden |
| `[je nach Sitz … LfDI BW … oder LDI NRW …]` | Datenschutz, Abschnitt Ihre Rechte | zuständige Aufsichtsbehörde nach Sitz wählen |
| `[Name und Sitz des Versicherers …]` | Impressum (Berufshaftpflicht) | nur falls Pflicht/gewünscht |
| `[Sachkunde / Zertifikate]` | Über uns | |
| `[Kurzer Text zu Inhaber …]` | Über uns | |
| `[Maximale Arbeitshöhe / eigene Technik ergänzen]` | Leistungen → Einsätze in der Höhe | nur tatsächlich vorhandene Technik nennen |
| `[Erreichbarkeit, z. B. Mo–Sa 8–18 Uhr]` | Kontakt | |
| `[Bitte an die tatsächliche Praxis anpassen]` | Datenschutz, Abschnitt 5 | |
| `[FOTO 3]`, `[FOTO INHABER]` | Ablauf, Über uns | siehe unten (FOTO 1 + 2 sind mit eigenen Fotos belegt) |

Nach dem Ersetzen die Klasse `ph` am jeweiligen `<span>` entfernen (sonst bleibt der Text orange unterstrichen).

## Logo

Original: `img/logo/falkner-logo-original.jpg` (185×599, hochkant, weißer Hintergrund). Daraus freigestellt (transparent):

| Datei | Verwendung |
|---|---|
| `img/logo/falkner-logo-horizontal-light.(webp\|png)` | Header (52 px hoch, mobil 42 px) und Footer – helle Variante für den dunklen Hintergrund, 90° im Uhrzeigersinn gedreht |
| `img/logo/falkner-logo-horizontal.(webp\|png)` | Originalfarben quer – für helle Hintergründe |
| `img/logo/falkner-logo-vertical(-light).(webp\|png)` | hochkant, Originalfarben bzw. hell |
| `img/logo/falkner-grass-mark.png`, `icon-192.png`, `icon-512.png` | Grasmarke (Bildmarke) |
| `favicon.ico` (16/32/48), `favicon-32.png`, `apple-touch-icon.png` (180) | Grasmarke dunkelgrün auf Creme – im `<head>` eingebunden |

`favicon.svg` (alte Hornissen-Grafik) liegt noch im Repo, ist aber nicht mehr eingebunden.

## Eigene Fotos einsetzen

Fotoplätze sind `<figure class="photo-slot">…</figure>` mit Kommentar `<!-- FOTO … -->`. Ersetzen durch z. B.:

```html
<figure class="photo"><img src="img/einsatz-1.jpg" alt="Kurze Beschreibung" width="1200" height="900" loading="lazy"></figure>
```

Nur Fotos verwenden, an denen Sie die Rechte haben (am besten eigene). Keine Stockfotos mit unklarer Lizenz.

## Cache-Busting

CSS/JS werden mit `?v=…` eingebunden (`css/style.css?v=20261101g`, `js/main.js?v=20261101g`).
Nach jeder Änderung an CSS/JS den Wert in `index.html` erhöhen (z. B. `20261101h`).

## Eigene Domain

Bei Umzug auf eine eigene Domain `canonical`, `og:url`, `og:image` und `url` im JSON-LD anpassen
(derzeit `https://mike21getit.github.io/asiatische-hornisse/`) und ggf. eine `CNAME`-Datei anlegen.

## Formular

Kein Server: Das Formular baut eine E-Mail (mailto:) im E-Mail-Programm des Besuchers zusammen. Es werden
keine Daten an die Website übertragen. Fotos hängt der Besucher selbst an.

## Bildnachweis

**Eigene Fotos und Videos** © Falkner Schädlingsbekämpfung GmbH / Michael Falkner. Exif-/GPS-Daten und Video-Metadaten wurden beim
Konvertieren entfernt. Bildunterschriften beschreiben nur, was zu sehen ist (keine Orts-/Datumsangaben).

| Datei | Verwendung | Original (Drive „Vespa Velutina“) |
|---|---|---|
| `img/hero-velutina.webp`, `img/hero-velutina-1000.webp` | Startbild (TEST) | velutina-01.jpg |
| `img/hero-start.webp`, `img/hero-start-1000.webp`, `img/og-image.jpg` | Bisheriges Startbild (Reserve), Social-Media-Vorschau (weiterhin aus „start“) | start.jpg |
| `img/erkennen-crabro.webp`, `img/erkennen-crabro-800.webp` | Erkennen – Bild neben der Zeichnung der Europäischen Hornisse; **KI-generiert** (Bildsignatur in den Metadaten), daher als „KI-generierte Darstellung“ gekennzeichnet und **nicht** im Fotovergleich verwendet | Vespa Crabo.JPG |
| `img/hero-vespa-solo.webp`, `img/hero-vespa-solo-1000.webp` | Erkennen – Foto rechts neben der Zeichnung der Asiatischen Hornisse (bis 01.11.2026 Startbild) | vespa-solo.jpg |
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
| `video/nest-badezimmer.mp4` + `img/eigen-video-poster.webp` | Praxis-Block „Nest im Badezimmer“, Video 1 (18 s, 1080×1920, 10,9 MB, CRF 21) | IMG_0270.MP4 (inhaltsgleich mit „Automatic 3.MP4“) |
| `video/nest-badezimmer-flugloch.mp4` + `img/eigen-video2-poster.webp` | Praxis-Block „Nest im Badezimmer“, Video 2 (47 s, 1080×1920, 19,4 MB, CRF 24) | 1080p_Match_Framerate.MP4 |
| `video/nest-fensterrahmen.mp4` + `img/eigen-video-fensterrahmen-poster.webp` | Rubrik „Sekundärnest“ (`#sekundaernest`, in der Navigation), Sekundärnest an einem Fensterrahmen (19 s, 1080×1920, 16,7 MB, CRF 21) | Automatic-03.MP4 (bearbeitete Fassung von IMG_9853.MP4) |

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

### Videos neu kodieren

Aus den Originalen (IMG_0270 und Automatic-03 in 2160×3840, 1080p_Match_Framerate in 1080×1920):

    ffmpeg -i ORIGINAL.MP4 -map 0:v:0 -an -map_metadata -1 -map_chapters -1 \
      -vf "scale='min(1080,iw)':-2:flags=lanczos,format=yuv420p" \
      -c:v libx264 -profile:v high -preset slow -crf 21 -tune film -movflags +faststart ZIEL.mp4

Videos werden mit `object-fit: contain` angezeigt, im Vollbild (`:fullscreen`) ebenfalls – so wird nie ein Ausschnitt abgeschnitten.

### Startbild zurück auf „start“

In `index.html` im Hero-`<img>`: `hero-velutina` → `hero-start`, `width="2000" height="1334"`, `sizes="(min-width: 900px) 60vw, 330vw"`,
Alt-Text „Foto eines großen Nests der Asiatischen Hornisse mit geschwungen gemusterter Papierhülle; auf der Hülle sitzen Asiatische Hornissen, rechts unscharfer grüner Hintergrund“.
In `css/style.css`: Desktop `.hero-img { object-position: 44% 50%; }`, Mobil `object-position: 47% 50%`. Danach `?v=` erhöhen.
