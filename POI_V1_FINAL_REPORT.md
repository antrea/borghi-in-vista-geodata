# Database europei dei luoghi v1.0

Snapshot POI qualificato e verificato delle fonti disponibili, distribuito gratuitamente. 94 pacchetti: 90 OSM con 2,645,886 record in 55 paesi/territori, più quattro alternative nazionali con 45.596 record da non sommare come luoghi distinti. Italia builtin, Android 161 e DEM restano invariati. Le limitazioni delle fonti sono parte della distribuzione, non una promessa di censimento perfetto.

## Risultati richiesti

| Domanda | Esito |
|---|---|
| Pacchetti definitivi | 94; 56 rigenerati, 34 OSM e 4 nazionali riusati senza modifiche |
| Luoghi | 2,645,886 OSM; 45.596 nelle alternative indipendenti |
| Esame dei tipi | Tutte le 7 categorie, 40 identità e 2200 celle paese/tipo |
| MOUNTAIN / SANCTUARY | MOUNTAIN 0, nessun candidato individuale con anchor qualificato; SANCTUARY 6 documentati |
| Anomalie | 7.088 sospetti decisi; 31 esclusioni confermate, 585 casi trattenuti, 534 riclassificazioni |
| Coordinate | Tutti i record OSM confrontati con identità/versione/geometria originali; coordinate mantenute identiche; quote NULL |
| Copertura insufficiente | MOUNTAIN e SANCTUARY restano limitati dalle evidenze; aree grandi, conflitti e altri candidati non qualificati esclusi; vedere matrice |
| GitHub | URL immutabili di tutti i pacchetti nel manifest; stato pubblicazione verificato nel receipt locale dopo upload |
| Manifest e licenze | Ed25519, SHA-256, ODbL con attribuzione, alternative nazionali separate; CRC e SQLite verificati |
| Produzione conclusa | Sì per questo snapshot delle fonti qualificate, non per un censimento esaustivo di ogni luogo europeo |

## Controlli

1095 query a 10/20/100 km, incluse 42 prove transfrontaliere; 30798 campioni automatici tipo/anchor; 148 test verdi. Verifiche umane o sul campo: zero. I confini sono di pianificazione, non catastali. L'incertezza areale è un budget di rappresentazione ≤250 m, non una precisione GNSS certificata.

`qualification-decisions.json` conserva tutti gli ID, motivi ed evidenze fuori dagli ZIP runtime. Il singolo MOUNTAIN r4 è una catena montuosa secondo l'autorità turistica greca: escluso, non sostituito da vette duplicate. I sei santuari hanno evidenza istituzionale sullo stesso edificio. Le chiese generiche e i soli nomi non sono sufficienti.

I 30 `razed=yes` sono stati rimossi dagli SQLite effettivi. Gli oggetti dismessi o abbandonati ancora attestati come strutture fisiche, cave o rovine sono mantenuti; non sono automaticamente demoliti. I casi religiosi irrisolti e gli insediamenti senza abitazione/resti attestati rimangono in HOLD, fuori dai pacchetti finali.

## Uso e aggiornamenti

Gli archivi nuovi sono negli Assets della release `geodata-europe-v1.0`; quelli invariati restano nelle release precedenti e sono referenziati. Selezionare una sola fonte per unità, mai unione automatica OSM/nazionale. Verificare firma e hash, installare in staging e conservare il rollback. ID stabili, revisione nuova per byte nuovi. Il futuro loader Android è un'attività distinta.

Leggere [ricetta e criteri](POI_V1_REBUILD.md), [contratto](BIV_GEODATA_V1.md), [ODbL](https://opendatacommons.org/licenses/odbl/1-0/) e [attribuzione OSM](https://www.openstreetmap.org/copyright). I DEM mantengono la loro distribuzione precedente e non sono nel presente catalogo POI.
