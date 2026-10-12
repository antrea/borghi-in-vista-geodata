# Borghi in Vista — dati geografici gratuiti

Database europei per il futuro sistema di pacchetti di **Borghi in Vista**, app Android 100% gratuita. I dati si scaricano senza pagamento: non sono pacchetti Premium.

## Dove sono i pacchetti

Gli SQLite sono dentro gli ZIP negli **Assets delle Releases**, non nella lista dei file Git:

- [r4 — 90 nuovi POI OSM autonomi, 2.646.502 record](https://github.com/antrea/borghi-in-vista-geodata/releases/tag/geodata-eu-core-20261012-r4)
- [r3 — due POI britannici OS Open Names](https://github.com/antrea/borghi-in-vista-geodata/releases/tag/geodata-eu-core-20261012-r3)
- [r2 — POI Svizzera e Liechtenstein swisstopo](https://github.com/antrea/borghi-in-vista-geodata/releases/tag/geodata-eu-core-20261012-r2)
- [r1 — 135 DEM](https://github.com/antrea/borghi-in-vista-geodata/releases/tag/geodata-eu-core-20261009-r1)

Il manifest r4 contiene gli URL immutabili di tutte le revisioni: non occorre ricopiare i DEM sotto r4. Ogni ZIP contiene SQLite, metadata, copertura, fonti e licenze. SHA-256 di ZIP e database sono nel manifest firmato e nei checksum.

## Stato reale della copertura

| Voce | Risultato |
|---|---|
| Unità pianificate | 240 = 91 POI (Italia inclusa) + 149 DEM |
| Nuovi POI OSM READY | 90 |
| Record nuovi OSM | 2.646.502 |
| Territori/paesi nei nuovi OSM | 55 |
| Pacchetti precedenti riutilizzati | 135 DEM + 4 POI nazionali alternativi |
| Asset runtime nel catalogo r4 | 229 |
| Unità pianificate qualificate | 226 / 240, inclusa Italia builtin |
| Unità DEM UNKNOWN | 13 marittime + 1 Rockall |
| ZIP nuovi OSM | 773.221.157 byte |
| SQLite nuovi OSM | 2.904.727.552 byte |
| ZIP runtime totali, incluse alternative | 993.169.096 byte |
| Record nazionali alternativi, non da sommare come luoghi distinti | 45.596 |
| Nodi originali verificati, nessun arrotondamento | 2.152.069 |
| Query 10/20/100 km | 810 PASS |
| Campioni automatici tipo × anchor | 30.635 |
| Verifiche umane/sul campo | 0; non simulate |
| Test tooling | 104 PASS; 0 fallimenti/errori/skipped |


READY riguarda sottoinsiemi verificati, **non la completezza di ogni paese o la precisione assoluta**. Tutte le 90 unità POI esterne del perimetro A hanno un pacchetto qualificato; Italia builtin invariata. Restano 14 unità DEM UNKNOWN, con motivi documentati; non si inventano quote. Conservate tutte le 7 categorie e 40 identità di tipo, anche quando un tipo non ha record ammessi.

## Licenze e indipendenza

I nuovi OSM derivano autonomamente da OpenStreetMap e sono distribuiti sotto [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/), con attribuzione © OpenStreetMap contributors, database machine-readable e trasformazioni documentate. Nessuna decisione GeoNames entra nella selezione, classificazione, coordinate o paese dei nuovi POI. La gratuità non elimina obblighi di attribuzione/share-alike.

Le fonti nazionali r2/r3 mantengono le proprie licenze e sono **alternative separate**: il futuro reader seleziona UNA sorgente per unità, non unisce automaticamente OSM e dataset nazionali. Serve la capability `SOURCE_LAYER_SELECTION_V1`. Il formato è BIV-GEODATA-V1; le quote sconosciute rimangono NULL/UNKNOWN.

## Verificare e rigenerare

- [Contratto dei dati](BIV_GEODATA_V1.md)
- [Distribuzione e verifica firma/hash](DISTRIBUTION.md)
- [Qualità, conteggi per paese/tipo, esclusioni e limiti](OSM_ONLY_QUALITY_R4.md)
- [Ricetta di rigenerazione e aggiornamento](OSM_ONLY_REBUILD.md)
- [Report machine-readable](completion-report.json)
- [Snapshot e qualificazione licenze](source-snapshots.json)

`osm-rebuild-tools.zip` negli Assets r4 comprende codice, piani e snapshot minimo del Vaticano senza metadati dei contributori. Non contiene chiavi private, token, log o dati del telefono. Il fingerprint pubblico della chiave catalogo è `1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd`: la fiducia va stabilita da un canale indipendente, non soltanto dalla chiave scaricata dallo stesso server.

## App Android

Android 161 / 1.0.17 non viene modificata da questa pubblicazione. I pacchetti sono pronti come dati, ma richiedono il futuro loader Android compatibile; non sono automaticamente caricati dall'app attuale. Nessun APK/AAB è generato qui. Ulteriori prove sul campo e integrazione del loader sono attività distinte.
