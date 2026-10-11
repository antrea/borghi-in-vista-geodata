# Borghi in Vista — Pacchetti geografici europei

Repository pubblico per la distribuzione dei pacchetti **BIV-GEODATA-V1**, verificati tramite un audit indipendente dei file prodotti.

## Prima distribuzione: solo dati altimetrici, copertura parziale

[Scarica la release con catalogo firmato](https://github.com/antrea/borghi-in-vista-geodata/releases/tag/geodata-eu-core-20261009-r1).

- **135 pacchetti DEM validati**, circa 209 MB compressi complessivi.
- Modello di superficie Copernicus GLO-90 (**DSM**), coordinate orizzontali WGS84 e quote riferite a EGM2008.
- Ogni archivio contiene il database SQLite, la copertura, i metadati, i riferimenti alle fonti e le informazioni originali di licenza.
- Le quote sconosciute hanno una maschera di validità esplicita. **UNKNOWN non significa livello del mare, terreno piatto o visuale libera.**
- I 14 pacchetti DEM pianificati senza alcun campione noto non vengono distribuiti.
- I candidati europei relativi ai punti di interesse (**POI**) **non sono pubblicati**: restano aperti i controlli semantici, di licenza e di revisione. Questa non è una banca dati completa dei luoghi europei.
- Il database italiano già incluso nell'app rimane invariato e non viene redistribuito qui.

Il catalogo firmato `manifest.json` distingue i pacchetti disponibili da quelli non disponibili o ancora in lavorazione. La copertura descrive l'inventario delle celle: non garantisce che ogni campione altimetrico sia noto. Non viene dichiarata una precisione topografica né una verifica umana sul campo già completata.

## Verifica prima dell'installazione

Il catalogo usa una chiave Ed25519 dedicata. Impronta SHA-256 della chiave pubblica:

`1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd`

Verifica questa impronta tramite un canale attendibile indipendente. Scaricare la chiave pubblica e il catalogo dalla stessa fonte non attendibile non basta a garantirne l'autenticità.

Scarica i file della release in un'unica cartella. Con Python 3.12 o successivo e il pacchetto `cryptography` installato:

```sh
python verify_release.py 1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd
```

La verifica controlla firma, dimensioni, hash dei file compressi e dei database estratti, CRC degli archivi, integrità SQLite, schema e requisiti dello stato `READY`. Un aggiornamento deve essere preparato e verificato in una posizione temporanea prima di sostituire l'ultima installazione valida.

## Documentazione e compatibilità

- [Contratto del formato dati](BIV_GEODATA_V1.md)
- [Distribuzione, verifica e procedura di caricamento](DISTRIBUTION.md)
- [Release pubblicate](https://github.com/antrea/borghi-in-vista-geodata/releases)

La build Android 161 **non è stata modificata** e non supporta ancora il download o la lettura di questi pacchetti. Questo repository distribuisce dati destinati a un futuro lettore compatibile: non contiene una nuova release dell'app Android.

## Licenze e riservatezza

I dati altimetrici vengono distribuiti secondo i termini originali Copernicus GLO-90 inclusi in ogni archivio, con attribuzione della fonte. Le altre fonti non condividono automaticamente questa licenza: i candidati POI restano esclusi fino al superamento dei propri controlli. Consulta `LICENSES.txt`, il documento originale di licenza, i metadati e `sources.json` di ciascun pacchetto.

Non sono inclusi il codice sorgente dell'app, la chiave privata di firma, credenziali, log del telefono, posizione dell'utente, fotografie, registri grezzi di importazione, pacchetti POI intermedi o database di quarantena. Gli archivi dei dati sono allegati alle release, non salvati nella cronologia Git. Le release pubblicate sono immutabili: ogni correzione ai dati richiede una nuova release firmata.
