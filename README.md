# Borghi in Vista — Pacchetti geografici europei gratuiti

Borghi in Vista è un'app Android **100% gratuita**. Anche i pacchetti geografici sono gratuiti: nessun acquisto, abbonamento o entitlement sui dati.

## Pacchetti disponibili

[**Catalogo firmato r3 e nuovi pacchetti Gran Bretagna**](https://github.com/antrea/borghi-in-vista-geodata/releases/tag/geodata-eu-core-20261012-r3). Gli ZIP sono negli **Assets delle Releases**, non nelle cartelle del codice.

| Fonte e territorio | Pacchetti | Record | Download |
| --- | ---: | ---: | --- |
| Terreno Copernicus GLO-90 DSM | 135 | 208.719.093 byte ZIP | [DEM r1](https://github.com/antrea/borghi-in-vista-geodata/releases/tag/geodata-eu-core-20261009-r1) |
| swisstopo Svizzera | 1 | 12.594 | [Svizzera r2](https://github.com/antrea/borghi-in-vista-geodata/releases/download/geodata-eu-core-20261012-r2/poi-ch-eu-core-20261012-r2.zip) |
| swisstopo Liechtenstein | 1 | 36 | [Liechtenstein r2](https://github.com/antrea/borghi-in-vista-geodata/releases/download/geodata-eu-core-20261012-r2/poi-li-eu-core-20261012-r2.zip) |
| OS Open Names Gran Bretagna, unità 0 | 1 | 21.220 | [Gran Bretagna 0 r3](https://github.com/antrea/borghi-in-vista-geodata/releases/download/geodata-eu-core-20261012-r3/poi-gb-0-eu-core-20261012-r3.zip) |
| OS Open Names Gran Bretagna, unità 1 | 1 | 11.746 | [Gran Bretagna 1 r3](https://github.com/antrea/borghi-in-vista-geodata/releases/download/geodata-eu-core-20261012-r3/poi-gb-1-eu-core-20261012-r3.zip) |

Il catalogo comprende **139 pacchetti READY**, con **45.596 POI pubblicati**. Riusa i 137 pacchetti immutabili r1/r2 senza ricostruirli né duplicarli. La copertura POI è un **sottoinsieme qualificato**, non tutta Europa e non un censimento completo dei tre territori. La fonte britannica non copre l'Irlanda del Nord.

I 32.966 nuovi punti provengono esclusivamente da OS Open Names: City, Town, Village, Hamlet, Waterfall e Coastal Headland. Tutti sono riletti dalla fonte originale, con un'operazione di coordinate indipendente e 120 campioni automatici stratificati. Il controllo non è una verifica umana sul panorama. Ambiguità Hill Or Mountain, oggetti areali senza anchor qualificato e attività commerciali improprie non vengono ammessi per aumentare artificialmente la copertura.

## Licenze e provenienza

I database britannici sono distribuiti come derivazioni autonome sotto **Open Government Licence 3.0**, con le attribuzioni originali OS, Royal Mail e National Statistics e il testo di licenza dentro ogni ZIP. Non usano selezioni, join o deduplicazioni OSM/GeoNames. I campi di collegamento GeoNames/DBpedia del prodotto nazionale non sono usati né copiati.

I pacchetti svizzeri sono attribuiti a swisstopo; i DEM mantengono i termini originali Copernicus inclusi nei singoli archivi. Ogni SQLite conserva origine, identificativi, versione e hash della fonte, regola di tipo, metodo di anchor e condizioni di licenza. Il contratto mantiene sette categorie e quaranta tipi; non implica che ogni fonte fornisca record validi per tutti i tipi.

**296.589 candidati OSM/GeoNames rimangono non pubblicati**. Tutti dipendono da GeoNames nell'ammissione; alcuni anche nell'assegnazione del paese o nella scelta del vertice. Pubblicare il derivato sotto ODbL e renderlo gratuito non dimostra da solo la compatibilità delle ulteriori componenti CC BY 4.0. La questione precisa e le alternative sono in [Licenze e completamento](LICENSE_QUALIFICATION_R3.md) e nel [report machine-readable](license-qualification.json). Nessuna autorizzazione del titolare viene inventata e la provenienza non viene rimossa per simulare un'origine OSM-only.

## Terreno e geometrie

Il terreno è un modello di superficie **DSM GLO-90**, non DTM, con coordinate WGS84 e quote EGM2008. I campioni ignoti hanno una maschera esplicita: **UNKNOWN non significa quota zero o visuale libera**. Le quote POI non qualificate restano NULL.

Tredici unità aggiuntive non mostrano terra nelle due fonti costiere controllate, nei limiti della risoluzione. Una unità, `dem-eu-07-10`, contiene evidenza di Rockall ma le celle GLO-90/GLO-30 N57W014 non sono disponibili. Nessun DEM vuoto o quota inventata viene pubblicato. I label e centroidi di aree non qualificati non diventano automaticamente punti AR.

## Verifica del catalogo e rollback

Firma Ed25519, impronta SHA-256 della chiave pubblica:

`1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd`

L'impronta deve essere verificata tramite un canale attendibile indipendente. Scaricare chiave e catalogo dalla stessa fonte non attendibile non basta a garantirne l'autenticità.

Scarica tutti i file della r3 in una cartella, i 135 ZIP r1 e i due ZIP r2 in cartelle cache. Con Python 3.12+ e `cryptography`, esegui dalla cartella r3:

```sh
python verify_catalog.py 1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd /cache-r1 /cache-r2
```

Il controllo verifica firma, checksum, CRC, hash e integrità SQLite, schema e gate READY. Gli archivi mancanti sono **non verificati**, non PASS. La sostituzione di un database va preparata e verificata in una posizione temporanea, promossa atomicamente e accompagnata da una copia precedente per rollback. Le release sono immutabili: una modifica ai dati richiede nuova versione, nuovo hash e nuovo catalogo firmato.

## Documentazione e compatibilità Android

- [Contratto BIV-GEODATA-V1](BIV_GEODATA_V1.md)
- [Distribuzione](DISTRIBUTION.md)
- [Inventario](completion-report.json)
- [Tutte le release](https://github.com/antrea/borghi-in-vista-geodata/releases)

**Android 161 rimane invariato e non supporta ancora il download e la lettura di questi pacchetti.** I dati sono disponibili per un futuro lettore compatibile; questo repository non contiene una nuova versione dell'app.

Non sono pubblicati codice Android, chiavi private, credenziali, dati del telefono, fotografie, coordinate utente, ledger grezzi o pacchetti intermedi sospesi.
