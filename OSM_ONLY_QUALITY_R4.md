# Qualità dei pacchetti OSM autonomi r4

## Verdetto e copertura

90 nuovi pacchetti OSM sono READY per **sottoinsiemi qualificati**, non per un censimento completo o una precisione misurata sul campo. Tutte le unità POI esterne del piano sono state processate; l'Italia incorporata resta invariata. Le aree e i record in revisione non sono promossi per raggiungere artificialmente la completezza.

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


## Indipendenza e licenza

La selezione è ricostruita da tag, identità, geometrie e versioni originali OSM. Nessun identificativo, nome, feature code, coordinata, ranking o paese GeoNames determina l'ammissione. Solo dopo l'audit finale viene confrontata la copertura con i 296.589 candidati misti storici; quell'elenco non è input della selezione. Le importazioni precedenti rimangono conservate.

I database OSM sono offerti completi, machine-readable, gratuitamente sotto [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/) con [attribuzione OpenStreetMap](https://www.openstreetmap.org/copyright), provenienza, trasformazioni e toolkit. La gratuità non elimina obblighi di licenza. I quattro dataset nazionali sono alternative indipendenti, non dati fusi nella derivazione OSM. Questo non sostiene che OSM stesso non abbia mai importato altre fonti: si usa il database offerto dal suo titolare sotto la relativa licenza.

## Anchor e significato della precisione

| Metodo | Record |
|---|---|
| ORIGINAL_OSM_NODE | 2.152.069 |
| PHYSICAL_LINE_MIDPOINT_WITH_EXTENT_UNCERTAINTY | 4.153 |
| PHYSICAL_POINT_ON_SURFACE_WITH_EXTENT_UNCERTAINTY | 490.280 |


I punti OSM restano identici agli originali WGS84, ma l'accuratezza del rilievo è sconosciuta. Per geometrie fisiche piccole si usa un punto sulla superficie o il punto medio di una linea qualificata, mai un centroide automatico. Il budget massimo di 250 m e l'incertezza pari all'estensione sono **incertezza rappresentativa**, non accuratezza misurata. Il futuro reader deve tenerne conto, specialmente per oggetti vicini. Aree maggiori senza punto originale qualificato restano in revisione. Gli edifici amministrativi/aree di insediamenti non diventano un nucleo abitato. Tutte le quote OSM runtime sono NULL: nessun datum o quota viene inventato.

I confini Natural Earth congelati sono pubblico dominio, non catastali. La tolleranza costiera di 0,05° è solo assegnazione con paese unico, non uno spostamento dell'anchor. Per il Vaticano, il confine originale OSM relazione 36989/versione 117 corregge la copertura cartografica troppo piccola; è usato solo per il paese e non come POI. Snapshot, area e hash sono documentati. La fonte pubblica sanitizzata è distinta dalla risposta HTTP originale e ne conserva l'hash di provenienza; l'URL Overpass non restituisce direttamente i byte del JSON canonico.

## Audit effettivamente eseguito

Su ogni file finale: integrity_check, foreign_key_check, schema/application_id, 7 categorie e 40 identità di tipo, NFC, ID globali/numerici senza collisioni, coordinate finite, assenza di quote non qualificate, provenienza/licenza, replay completo contro il registro sorgente, controlli negativi indipendenti su commercio/insediamenti amministrativi/basiliche/ponti/residenze, anchor all'interno della geometria e limiti di estensione. Tre centri per pacchetto × 10/20/100 km confrontano RTree con scansione completa geodetica WGS84. Campionamento deterministico per tipo × metodo di anchor, non verifica umana.

Il replay indipendente degli originali PBF/risposta OSM verifica 2.152.069 punti con tolleranza zero. Le geometrie sono riassemblate dalle cache originali reference-complete senza usare stato/paese/categoria storici. 4.418 equivalenze registrano membership label OSM esplicita o un unico punto omonimo dello stesso tipo all'interno della stessa piccola geometria; non si deduplica per sola vicinanza/nome.

Ogni ZIP passa CRC/hash e installazione staged verificata. Il catalogo è firmato Ed25519. La pubblicazione richiede verifica di tutti i nuovi download HTTPS pubblici prima di promuovere il catalogo principale; r1/r2/r3 non sono sovrascritte. Non è stato eseguito un rebuild integrale su una seconda macchina né un test Android: non sono dichiarati PASS.

## Esclusioni e casi in revisione

| Stato nel registro autonomo | Record |
|---|---|
| ACCEPTED | 2.646.502 |
| DEDUPLICATED | 4.418 |
| REJECTED | 101.715 |
| REVIEW | 2.078.340 |


I conteggi seguenti sono decisioni del registro autonomo, non un'affermazione che ogni record in revisione sia un errore di OSM. Oggetti senza tipo pertinente, non nominati o fuori perimetro sono conteggiati separatamente nei tally della lettura; i tally delle sorgenti sovrapposte non sono un censimento univoco.

| Stato | Motivo | Record |
|---|---|---|
| DEDUPLICATED | EXPLICIT_SOURCE_LABEL_NODE_IDENTITY | 3.669 |
| DEDUPLICATED | SAME_SMALL_PHYSICAL_OBJECT_ORIGINAL_NODE_PREFERRED | 749 |
| REJECTED | ADMINISTRATIVE_AREA_NOT_PHYSICAL_POI | 96.504 |
| REJECTED | ADMINISTRATIVE_OR_INDUSTRIAL_NOT_PHYSICAL_SETTLEMENT | 2.489 |
| REJECTED | COMMERCIAL_OVERLAP_NOT_A_PRODUCT_POI | 2.213 |
| REJECTED | DESTROYED_ENTITY | 338 |
| REJECTED | NOT_INDEPENDENT_SETTLEMENT | 157 |
| REJECTED | HUNTING_OR_RESOURCE_PROTECTION_NOT_NATURE_RESERVE | 14 |
| REVIEW | LOCALITY_NOT_EVIDENCE_OF_PHYSICAL_HABITATION | 1.565.812 |
| REVIEW | EXTENT_EXCEEDS_250M_REPRESENTATION_BUDGET | 268.452 |
| REVIEW | SETTLEMENT_POLYGON_NOT_PHYSICAL_NUCLEUS | 120.752 |
| REVIEW | GENERIC_WORKS_OR_SMALL_TOWER_NOT_LANDMARK | 41.589 |
| REVIEW | GENERIC_HISTORIC_STATUS_UNSPECIFIED | 35.552 |
| REVIEW | STRUCTURED_TYPE_CONFLICT | 27.706 |
| REVIEW | ABANDONED_SETTLEMENT_VISIBLE_REMAINS_NOT_ATTESTED | 11.101 |
| REVIEW | PROTECTED_AREA_PURPOSE_NOT_QUALIFIED | 6.327 |
| REVIEW | GEOMETRY_TYPE_NOT_QUALIFIED_FOR_ANCHOR | 1.044 |
| REVIEW | SAME_VERSION_SOURCE_CONFLICT | 5 |


## Distribuzione per categoria e tipo

| Categoria | Record |
|---|---|
| HISTORY_CULTURE | 132.202 |
| MOUNTAINS_LANDSCAPE | 328.704 |
| NATURE_PANORAMA | 150.042 |
| RELIGIOUS | 288.608 |
| SEA_WATER | 153.696 |
| SETTLEMENTS | 1.567.785 |
| SPECIAL | 25.465 |


| Tipo stabile | Categoria | Record OSM |
|---|---|---|
| ARCHAEOLOGICAL_SITE | HISTORY_CULTURE | 57.244 |
| BASILICA | RELIGIOUS | 91 |
| BAY | SEA_WATER | 29.688 |
| BEACH | SEA_WATER | 13.905 |
| CAPE | SEA_WATER | 14.736 |
| CASTLE | HISTORY_CULTURE | 33.350 |
| CAVE | NATURE_PANORAMA | 32.465 |
| CHURCH | RELIGIOUS | 284.027 |
| CITY | SETTLEMENTS | 1.243 |
| DAM | SPECIAL | 4.720 |
| FORTRESS | HISTORY_CULTURE | 3.454 |
| GEOLOGICAL_FORMATION | MOUNTAINS_LANDSCAPE | 14.095 |
| GHOST_TOWN | SPECIAL | 110 |
| HAMLET | SETTLEMENTS | 700.629 |
| HILL | MOUNTAINS_LANDSCAPE | 6.548 |
| HISTORIC_BRIDGE | HISTORY_CULTURE | 1.448 |
| HISTORIC_RESIDENCE | HISTORY_CULTURE | 12.962 |
| HISTORIC_SITE | HISTORY_CULTURE | 5.529 |
| ISLAND | SEA_WATER | 54.279 |
| ISOLATED_DWELLING | SETTLEMENTS | 529.577 |
| LAKE | SEA_WATER | 26.812 |
| LARGE_INFRASTRUCTURE | SPECIAL | 10.594 |
| LIGHTHOUSE | SEA_WATER | 2.342 |
| LOCALITY | SETTLEMENTS | 766 |
| MONASTERY | RELIGIOUS | 4.490 |
| MONUMENT | HISTORY_CULTURE | 17.833 |
| MOUNTAIN | MOUNTAINS_LANDSCAPE | 1 |
| MOUNTAIN_PASS | MOUNTAINS_LANDSCAPE | 11.618 |
| NATURE_RESERVE | NATURE_PANORAMA | 6.262 |
| PARK | NATURE_PANORAMA | 75.524 |
| PEAK | MOUNTAINS_LANDSCAPE | 292.482 |
| QUARRY_MINE | SPECIAL | 10.041 |
| RUIN_TOWER | HISTORY_CULTURE | 382 |
| SANCTUARY | RELIGIOUS | 0 |
| TOWN | SETTLEMENTS | 15.739 |
| VALLEY | MOUNTAINS_LANDSCAPE | 3.101 |
| VIEWPOINT | NATURE_PANORAMA | 35.791 |
| VILLAGE | SETTLEMENTS | 319.831 |
| VOLCANO | MOUNTAINS_LANDSCAPE | 859 |
| WATERFALL | SEA_WATER | 11.934 |


SANCTUARY non ha record qualificati in questo snapshot: l'identità e i test restano presenti, ma non si rinominano chiese generiche per riempire il tipo. I poligoni e i sottotipi ambigui restano in revisione.

## Distribuzione geografica

| ISO territorio/paese | Pacchetti OSM | Record |
|---|---|---|
| AD | 1 | 359 |
| AL | 1 | 8.356 |
| AT | 1 | 67.538 |
| AX | 1 | 1.063 |
| AZ | 1 | 556 |
| BA | 1 | 17.714 |
| BE | 1 | 18.373 |
| BG | 1 | 15.781 |
| BY | 1 | 28.177 |
| CH | 1 | 34.578 |
| CZ | 1 | 43.633 |
| DE | 2 | 232.258 |
| DK | 1 | 23.798 |
| EE | 1 | 11.417 |
| ES | 2 | 215.511 |
| FI | 4 | 50.010 |
| FO | 1 | 1.008 |
| FR | 4 | 657.564 |
| GB | 2 | 127.057 |
| GE | 1 | 253 |
| GG | 1 | 239 |
| GI | 1 | 88 |
| GR | 1 | 35.992 |
| HR | 1 | 46.006 |
| HU | 1 | 22.336 |
| IE | 1 | 16.976 |
| IM | 1 | 559 |
| IS | 1 | 5.030 |
| JE | 1 | 313 |
| KZ | 1 | 567 |
| LI | 1 | 109 |
| LT | 1 | 25.650 |
| LU | 1 | 1.722 |
| LV | 1 | 78.054 |
| MC | 1 | 50 |
| MD | 1 | 2.635 |
| ME | 1 | 8.396 |
| MK | 1 | 3.375 |
| MT | 1 | 908 |
| NL | 1 | 14.975 |
| NO | 8 | 110.483 |
| PL | 1 | 157.477 |
| PT | 1 | 39.419 |
| RO | 1 | 31.825 |
| RS | 1 | 14.375 |
| RU | 18 | 174.133 |
| SE | 2 | 195.786 |
| SI | 1 | 24.019 |
| SJ | 1 | 1.297 |
| SK | 1 | 24.194 |
| SM | 1 | 241 |
| TR | 1 | 5.055 |
| UA | 2 | 46.437 |
| VA | 1 | 19 |
| XK | 1 | 2.758 |


## DEM e residui

I 135 DEM r1 restano immutati. L'audit congelato di continuità ha verificato 1.314 bordi cross-pack; l'halo conservativo 100 km + slack è passato su 601.134 campioni, senza celle mancanti nell'inventario. È una verifica di copertura/continuità, non una garanzia di tutte le quote. Le 13 unità marittime restano UNKNOWN ai limiti delle fonti costiere.

Per dem-eu-07-10/Rockall, il raster Skadi alternativo ha 207 campioni positivi nella finestra e massimo 3 m, ma non dimostra datum, landmask o accuratezza specifica dell'isola. GEBCO 15 arcsec è troppo grossolano senza prova specifica; OS Terrain 50 non ha copertura Rockall/datum compatibile verificati. Nessuna alternativa è stata promossa. UNKNOWN non significa quota zero o terreno libero.

## Mantenibilità e limiti dichiarati

Identità `osm:node/way/relation` stabili, revisione immutabile, hash delle fonti, regole deterministiche e checkpoint. Gli aggiornamenti devono confrontare identità/tipo/coordinate con la revisione precedente. Il toolkit e le prove rendono il processo verificabile; il writer nativo può differire su altra toolchain e il rebuild integrale su un secondo host resta non verificato. La chiave privata non è distribuita. Una seconda copia cifrata DPAPI, conservata separatamente dagli artefatti pubblici, è stata realmente creata e riaperta, con verifica della firma e dello stesso fingerprint pubblico; richiede però il contesto DPAPI dell'account Windows corrente. Il backup portabile richiede una password scelta dal titolare. Test di round-trip/tamper/password errata verificano quel meccanismo, non l'esistenza di un backup portabile non ancora creato.

Android 161/1.0.17 è invariata e non incorpora ancora il futuro downloader/reader. Non sono stati prodotti APK o AAB. READY dei dati non è una dichiarazione di integrazione nell'app.
