# Rigenerazione dei POI europei v1.0

La v1.0 contiene una revisione mirata dei POI OSM r4. Le sorgenti nazionali restano alternative indipendenti e i DEM sono fuori da questa revisione. I database derivati OSM sono disponibili gratuitamente in forma SQLite sotto ODbL 1.0, con attribuzione a OpenStreetMap contributors. Non sono imposti DRM o vincoli aggiuntivi.

## Input congelati

Il manifest r4 e gli archivi immutabili identificano il precedente contenuto mediante SHA-256. `source-snapshots.json` identifica gli originali pubblici. Il recipe completo di importazione originale rimane in `osm-rebuild-tools.zip` nella release r4. `poi-v1-rebuild-tools.zip` contiene la sola qualificazione aggiuntiva, i test, gli override sullo stesso ID/versione e i controlli sui file. Non servono GeoNames né dati del telefono.

`qualification-decisions.json` è il file machine-readable di tutte le decisioni sui 7.088 sospetti e sulle ulteriori riclassificazioni. Riporta ID originale, versione, motivazione, hash dei tag ed evidenza pertinente. I KEEP non sono modifiche al runtime; HOLD ed EXCLUDE non vengono distribuiti come luoghi. Questo registro è separato dagli ZIP runtime.

## Trasformazioni

1. Verificare manifest firmato r4, ZIP e database originali.
2. Conservare gli stessi ID numerici e originali OSM, nomi, coordinate e geometrie dei record mantenuti.
3. Escludere i 30 oggetti esplicitamente `razed=yes` e la catena montuosa erroneamente ammessa come montagna individuale.
4. Trattenere fuori dai pacchetti i conflitti religiosi non risolti e gli insediamenti abbandonati privi di attestazione di abitazione attuale o resti visibili. Non equiparare disuso/abbandono a demolizione.
5. Riclassificare le basiliche con status strutturato esplicito, gli insediamenti con rovine documentate e i santuari qualificati sullo stesso edificio. Nessuna inferenza dal nome; nessuna duplicazione PEAK/MOUNTAIN.
6. Copiare i database solo dei pacchetti interessati, applicare il delta, aggiornare gli indici, verificare SQLite e creare ZIP Deflate deterministici. Le quote restano NULL/UNKNOWN.
7. Eseguire `poi_v1_audit.py` e `poi_v1_borders.py`. Solo i candidati verificati diventano READY. Nessun registro intermedio entra nei cinque membri runtime degli ZIP.

La selezione può essere riprodotta direttamente dagli originali congelati oppure applicando le decisioni al r4 verificato. I byte SQLite/Deflate dipendono anche dalle versioni Python, SQLite e zlib: confrontare gli hash attesi; un toolchain diverso non autorizza a dichiarare identità binaria senza controllo.

## Aggiornamenti e rollback

Ogni cambiamento richiede nuova revisione e nuovi hash. Gli ID non dipendono dal nome o dalla classificazione. Un record trattenuto non viene rinumerato: conserva l'identità originale per un'eventuale successiva qualificazione. Installare in staging, verificare e promuovere atomicamente; conservare la copia precedente per rollback. Selezionare esattamente una sorgente per unità: non unire automaticamente OSM e alternative nazionali.

## Limiti

La v1.0 chiude lo snapshot qualificato delle fonti disponibili, non un censimento perfetto del mondo reale. MOUNTAIN resta vuoto: i candidati importati sono catene/massicci, conflitti semantici o geometrie troppo estese senza anchor qualificato. Le vette PEAK rimangono utilizzabili ma non sono duplicate come montagne. SANCTUARY contiene solo i riscontri espliciti qualificati; il resto rimane CHURCH/BASILICA, non santuario presunto. Gli anchor areali sono rappresentazioni limitate a 250 m di estensione, non certificazioni di precisione GPS. Le verifiche sono automatiche e documentali, non sul campo.

## Riferimenti

- [Licenza ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/)
- [Attribuzione OpenStreetMap](https://www.openstreetmap.org/copyright)
- [Disuso OSM](https://wiki.openstreetmap.org/wiki/Key:disused:)
- [Abbandono OSM](https://wiki.openstreetmap.org/wiki/Key:abandoned:)
- [Athamanika come catena montuosa, autorità turistica greca](https://www.visitgreece.gr/en/experiences/architecture/picturesque-villages/tzoumerka-mountain-chain)

Gli override conservano solo l'identificazione fattuale della funzione del luogo e il link all'evidenza, non fotografie o estratti delle pagine istituzionali.
