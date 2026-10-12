# Rigenerazione dei pacchetti OSM europei

I nuovi database sono una derivazione autonoma di OpenStreetMap, distribuita gratuitamente sotto ODbL 1.0. I candidati misti storici non sono input della selezione. GeoNames non determina nomi, tipi, coordinate, appartenenza geografica o ammissione.

## Sorgenti congelate e ripresa

Gli snapshot Geofabrik originali, con URL, SHA-256 e dimensione, sono elencati in `sources.json` dentro ciascun ZIP. Il perimetro A usa il piano geografico già congelato, derivato da Natural Earth, pubblico dominio. I confini non sono confini catastali. Una tolleranza costiera di 0,05 gradi è consentita solo con un unico paese candidato; non sposta le coordinate. Le situazioni costiere o transfrontaliere ambigue sono escluse.

`derive_osm_only.py` legge i nodi direttamente dagli originali e riutilizza esclusivamente identità, tag e WKB originali degli indici di way/relation già completi. Non legge dai registri storici stato, categoria, anchor corretto, paese o corrispondenza GeoNames. Le geometrie mancanti o incomplete restano escluse. Le copie originali e i registri storici non vengono riscritti. Il nuovo registro `osm-only.sqlite` ha checkpoint separati per sorgente e tipo di entità, legati agli hash di sorgente, regole e perimetro.

Per riprodurre localmente, installare Python con pyosmium, shapely, pyproj e cryptography, disporre degli originali e degli indici documentati, quindi eseguire nell'ordine:

Toolchain congelata usata qui: Python 3.12.14, pyosmium 4.1.1, Shapely 2.2.0, pyproj 3.8.0, cryptography 50.0.2, Windows x64. La ricostruzione integrale su una seconda macchina non è stata eseguita e non è dichiarata PASS. Le prove di ripresa e gli hash dei pacchetti riguardano la workstation di produzione.

```text
python scripts/derive_osm_only.py
python scripts/complete_osm_original_geometry.py
python scripts/qualify_vatican_original.py
python scripts/dedup_osm_only.py
python scripts/replay_osm_original.py
python scripts/package_osm_only.py
python scripts/audit_osm_only.py
```

Questi programmi producono e verificano gli SQLite. Firma del catalogo e pubblicazione sono operazioni del titolare della chiave, separate dal toolkit pubblico; `osm_catalog.py` e le credenziali non sono inclusi nello ZIP di ricostruzione.

### Vaticano: correzione documentata di copertura

Il poligono Natural Earth del Vaticano nel piano congelato è troppo piccolo per il territorio reale. Un'integrazione OSM originale, datata 2026-10-09, qualifica il confine amministrativo di livello 2, relazione 36989, **solo per l'appartenenza al paese**. Il piano originale e l'Italia incorporata non cambiano. `osm-country-overrides.json` documenta geometria, versione, area e hash.

Il toolkit include lo snapshot di tutti gli oggetti interrogati nella piccola finestra, con sole proprietà necessarie e senza campi di contributori/contatto; non è una lista preselezionata dei POI ammessi. Il replay di produzione confronta i punti con la risposta originale congelata e verifica il suo hash. Quella risposta con metadati dei contributori resta locale. Su una macchina nuova si può rigenerare il database dal sottoinsieme pubblico congelato; per ripetere il controllo indipendente sulla risposta originale occorre reacquisirla/documentare l'equivalenza semantica. Non è stato inventato un PASS di questo replay su una seconda macchina.

Le dipendenze e gli indici sono cache di elaborazione, non dati geografici aggiunti. I programmi di trasformazione, il piano geografico e la tassonomia congelata sono disponibili nell'asset `osm-rebuild-tools.zip`. I database finali completi sono liberamente scaricabili e soddisfano l'offerta machine-readable della derivazione; non occorre distribuire oltre 40 GB di snapshot per ottenere i database finali.

Su una macchina nuova, `reference_cache_recipe.py --rebuild` ricostruisce gli indici originali in una directory vuota usando gli snapshot e il piano machine-readable `osm-reference-plan.json`. Il piano contiene esclusivamente ID OSM originali e prove di cache: non è l'elenco di POI ammessi e non contiene corrispondenze GeoNames. Il builder non sovrascrive indici esistenti. Una differenza di byte del writer nativo va ispezionata come differenza di toolchain; non viene dichiarata una riproduzione esatta. La ripresa nella workstation attuale usa gli indici già completi e non riesegue questa costruzione.

## Classificazione e anchor

I 40 tipi e le 7 categorie sono quelli della build Android 161. La classificazione usa tag strutturati, non parole nei nomi. Tag specifici sono sufficienti per nodi ordinari; strutture religiose o storiche ambigue richiedono tag di stato più specifici. Un hotel, ristorante, negozio o parcheggio con tag sovrapposti non viene automaticamente trasformato in un borgo, castello, monumento o parco. Quartieri e aree amministrative non diventano nuclei abitati. Un santuario non è dedotto dal solo tag generico shrine.

Un nodo conserva il punto WGS84 originale. L'accuratezza di rilievo non è nota e non viene inventata. Per geometrie fisiche limitate a 250 m di estensione, un punto interno o il punto medio di una linea qualificata è ammesso con incertezza rappresentativa pari all'estensione: non è accuratezza di rilievo e non è un centroide. Il budget di 250 m è una scelta conservativa di rappresentazione, non una garanzia AR. Oggetti maggiori senza punto OSM qualificato restano in revisione. Le quote rimangono NULL finché il datum non è qualificato.

## Identità e aggiornamenti

Le identità `osm:node:<id>`, `osm:way:<id>` e `osm:relation:<id>` rimangono distinte. I numeri derivati SHA-256 non dipendono dai nomi. La sovrapposizione di snapshot dello stesso elemento mantiene la versione più recente; una discordanza alla stessa versione va in revisione. Omonimi non vengono deduplicati per nome. Cross-source equivalence non è presunta.

I nuovi ID di pacchetto terminano in `-osm`; i quattro pacchetti nazionali r2/r3 rimangono immutati e autonomi. Il catalogo specifica la selezione di UNA sorgente per unità: il futuro loader non deve unire automaticamente dataset alternativi. Serve la capability `SOURCE_LAYER_SELECTION_V1`, da implementare nel futuro loader prima dell'uso. Questo evita duplicazioni e cambiamenti silenziosi di identità tra fonti. Il formato SQLite resta BIV-GEODATA-V1, con tabella aggiuntiva `source_geometry` ignorabile dai lettori conformi.

Ogni aggiornamento richiede una nuova revisione immutabile, confronto delle identità/tipi/coordinate con la revisione precedente, nuova qualificazione e manifest Ed25519 firmato. Non sovrascrivere pacchetti pubblicati. La copia privata è staged e verificata; conservare una copia valida per rollback.

## Obblighi e limiti

[OSM copyright](https://www.openstreetmap.org/copyright) richiede attribuzione e disponibilità sotto ODbL delle derivazioni. Il [testo ODbL](https://opendatacommons.org/licenses/odbl/1-0/) disciplina notice, share-alike e accesso machine-readable. Gli ZIP comprendono attribuzione e URI della licenza. La gratuità non elimina questi obblighi. I futuri prodotti che usano i dati devono mantenere l'attribuzione appropriata; Android 161 non viene modificata in questa fase.

READY indica un sottoinsieme tecnicamente e semanticamente qualificato, non un censimento completo del paese, una precisione assoluta o una verifica umana. Quote sconosciute e DEM mancanti rimangono UNKNOWN, mai terreno libero o quota zero.
