# Distribuzione BIV-GEODATA-V1

Repository autorizzato: https://github.com/antrea/borghi-in-vista-geodata . Gli ZIP runtime sono allegati alle Releases, non alla cronologia Git. I registri privati di importazione, i checkpoint e la chiave privata non sono distribuibili.

## Revisione r2 e riuso immutabile

La revisione `geodata-eu-core-20261012-r2` è una **distribuzione parziale**, non l'intera Europa completata:

- 135 DEM READY già pubblicati nella release `geodata-eu-core-20261009-r1`, con URL e byte originali immutati;
- 2 POI READY da fonte ufficiale swisstopo (Svizzera e Liechtenstein), 12.630 punti qualificati;
- nessuna distribuzione dei candidati misti OSM/GeoNames con compatibilità di licenza ancora non stabilita;
- 13 unità DEM senza terra rilevata nelle due fonti costiere verificate, nei limiti della loro risoluzione;
- 1 unità con evidenza di isola ma sorgente altimetrica assente; UNKNOWN non è terreno libero;
- Italia builtin invariata e non redistribuita.

Non ricopiare i DEM sotto r2. Il manifest firmato contiene URL versionati per entrambi i tag. La visibilità del catalogo sul ramo principale viene promossa soltanto dopo pubblicazione e verifica HTTPS di tutti i nuovi asset. Un'interruzione lascia la precedente revisione utilizzabile; un nuovo caricamento riprende esclusivamente file con identiche dimensioni e SHA-256. Nessun clobber, cancellazione o modifica di una release immutabile.

## Verifica indipendente

Python 3.12+ e `cryptography` sono necessari. Scaricare i 13 file della release r2 nella stessa cartella e, separatamente, i 135 ZIP DEM r1 in una cartella cache. Eseguire:

```sh
python verify_catalog.py 1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd /percorso/cache-dem-r1
```

Il fingerprint va ottenuto da un canale indipendente attendibile. Il tool verifica la firma Ed25519, i file di supporto firmati, checksum, ZIP/CRC, hash/dimensioni dei database, integrità e schema SQLite, stato e gate READY. I file assenti vengono dichiarati **NOT verified**, mai promossi a PASS. Il vecchio `verify_release.py` rimane riferito esclusivamente alla release r1.

## Futuro reader Android

Staging privato → verifica ZIP/hash/schema/capability → promozione atomica → conservazione della versione precedente per rollback. Le quote Copernicus sono DSM GLO-90 in EGM2008, non DTM né quote topografiche garantite. Maschera UNKNOWN obbligatoria, inclusi campioni di mare e celle con sorgente assente. L'interpolazione che tocca UNKNOWN deve restare conservativa.

Android 161 resta invariato: **non implementa ancora il downloader né questo contratto dei pacchetti**. I dati non richiedono trasformazioni server-side aggiuntive, ma richiedono un futuro reader compatibile. Ogni fonte mantiene termini e attribuzioni separati, inclusi negli archivi. Nessuna verifica umana sul campo o percentuale di precisione viene dichiarata.

## Revisione OSM autonoma r4

Il catalogo r4 aggiunge nuovi pacchetti OSM autonomi sotto ODbL senza pubblicare la derivazione mista storica. I 135 DEM r1 e i quattro pacchetti nazionali r2/r3 mantengono URL, tag, byte e licenze originali. I nuovi ID `-osm` sono preferiti per le unità qualificate; il futuro loader deve scegliere UNA sola sorgente per unità, con capability `SOURCE_LAYER_SELECTION_V1`. Non unire automaticamente le alternative nazionali con OSM.

Per verificare r4, scaricare i file della nuova release e fornire al verificatore anche le tre cartelle cache r1/r2/r3:

```sh
python verify_catalog.py 1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd /cache/r1 /cache/r2 /cache/r3
```

`completion-report.json` espone i conteggi effettivi e le unità ancora non READY. `OSM_ONLY_QUALITY_R4.md` distingue audit tecnico, attendibilità dei tag, precisione sconosciuta e copertura parziale. `OSM_ONLY_REBUILD.md` e `osm-rebuild-tools.zip` documentano la rigenerazione. La promozione del ramo principale avviene solo dopo download pubblico e SHA-256 di TUTTI i nuovi file, senza alterare le release precedenti.
