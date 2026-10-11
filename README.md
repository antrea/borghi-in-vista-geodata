# Borghi in Vista — Pacchetti geografici europei

Repository pubblico per la distribuzione dei pacchetti **BIV-GEODATA-V1**, verificati tramite un audit indipendente dei file prodotti.

## Pacchetti disponibili: copertura parziale, non tutta Europa

[**Ultimo catalogo firmato r2**](https://github.com/antrea/borghi-in-vista-geodata/releases/tag/geodata-eu-core-20261012-r2). Gli ZIP si trovano negli **Assets delle Releases**, non nelle cartelle del codice.

| Contenuto | Pacchetti | Record/dimensione | Dove scaricare |
| --- | ---: | --- | --- |
| Terreno Copernicus GLO-90 DSM | 135 | 208.719.093 byte ZIP | [Release DEM r1](https://github.com/antrea/borghi-in-vista-geodata/releases/tag/geodata-eu-core-20261009-r1) |
| Punti ufficiali Svizzera | 1 | 12.594 punti; 3.280.510 byte ZIP | [POI Svizzera](https://github.com/antrea/borghi-in-vista-geodata/releases/download/geodata-eu-core-20261012-r2/poi-ch-eu-core-20261012-r2.zip) |
| Punti ufficiali Liechtenstein | 1 | 36 punti; 78.062 byte ZIP | [POI Liechtenstein](https://github.com/antrea/borghi-in-vista-geodata/releases/download/geodata-eu-core-20261012-r2/poi-li-eu-core-20261012-r2.zip) |

Il catalogo r2 contiene **137 pacchetti READY**. Riusa gli URL immutabili dei 135 DEM r1: non sono stati ricostruiti né caricati due volte. I 12.630 POI nuovi sono un sottoinsieme ufficiale qualificato, non tutti i luoghi esistenti nei due paesi.

- **135 pacchetti DEM validati**, circa 209 MB compressi complessivi.
- Modello di superficie Copernicus GLO-90 (**DSM**), coordinate orizzontali WGS84 e quote riferite a EGM2008.
- Ogni archivio contiene il database SQLite, la copertura, i metadati, i riferimenti alle fonti e le informazioni originali di licenza.
- Le quote sconosciute hanno una maschera di validità esplicita. **UNKNOWN non significa livello del mare, terreno piatto o visuale libera.**
- Dei 14 pacchetti DEM senza campioni noti, due fonti costiere non rilevano terra in 13 unità, nei limiti della loro risoluzione. Una ulteriore unità contiene evidenza di una piccola isola, ma le sorgenti GLO-90 e GLO-30 interrogate non forniscono la cella. Nessun DEM vuoto o quota inventata viene pubblicato.
- Gli altri candidati europei POI **non sono pubblicati**: manca la qualificazione della compatibilità di licenza della combinazione OSM/GeoNames. I poligoni privi di anchor fisico qualificato non vengono trasformati automaticamente in punti AR. Questa non è una banca dati completa dei luoghi europei.
- Il database italiano già incluso nell'app rimane invariato e non viene redistribuito qui.

Il catalogo firmato `manifest.json` distingue i pacchetti disponibili da quelli non disponibili o ancora in lavorazione. La copertura descrive l'inventario delle celle: non garantisce che ogni campione altimetrico sia noto. Non viene dichiarata una precisione topografica né una verifica umana sul campo già completata.

## Verifica prima dell'installazione

Il catalogo usa una chiave Ed25519 dedicata. Impronta SHA-256 della chiave pubblica:

`1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd`

Verifica questa impronta tramite un canale attendibile indipendente. Scaricare la chiave pubblica e il catalogo dalla stessa fonte non attendibile non basta a garantirne l'autenticità.

Scarica i 13 file r2 nella stessa cartella e i 135 ZIP DEM r1 in una cartella cache. Con Python 3.12 o successivo e il pacchetto `cryptography` installato:

```sh
python verify_catalog.py 1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd /percorso/cache-dem-r1
```

La verifica controlla firma, dimensioni, hash dei file compressi e dei database estratti, CRC degli archivi, integrità SQLite, schema e requisiti dello stato `READY`. I file assenti vengono dichiarati **non verificati**, mai PASS. Un aggiornamento deve essere preparato e verificato in una posizione temporanea prima di sostituire l'ultima installazione valida, conservando il precedente database per rollback.

## Documentazione e compatibilità

- [Contratto del formato dati](BIV_GEODATA_V1.md)
- [Distribuzione, verifica e procedura di caricamento](DISTRIBUTION.md)
- [Release pubblicate](https://github.com/antrea/borghi-in-vista-geodata/releases)
- [Inventario della distribuzione parziale](completion-report.json)

La build Android 161 **non è stata modificata** e non supporta ancora il download o la lettura di questi pacchetti. Questo repository distribuisce dati destinati a un futuro lettore compatibile: non contiene una nuova release dell'app Android.

## Licenze e riservatezza

I dati altimetrici vengono distribuiti secondo i termini originali Copernicus GLO-90 inclusi in ogni archivio, con attribuzione della fonte. I nuovi punti POI ufficiali sono attribuiti a swisstopo; identità, nomi e coordinate sono verificati contro lo snapshot originale, senza quote o accuratezze di rilievo inventate. Le altre fonti non condividono automaticamente queste licenze: i candidati misti restano esclusi fino al superamento dei propri controlli. Consulta `LICENSES.txt`, il documento originale di licenza, i metadati e `sources.json` di ciascun pacchetto. Non si dichiara verifica umana sul campo né una percentuale di precisione.

Non sono inclusi il codice sorgente dell'app, la chiave privata di firma, credenziali, log del telefono, posizione dell'utente, fotografie, registri grezzi di importazione, pacchetti POI intermedi o database di quarantena. Gli archivi dei dati sono allegati alle release, non salvati nella cronologia Git. Le release pubblicate sono immutabili: ogni correzione ai dati richiede una nuova release firmata.
