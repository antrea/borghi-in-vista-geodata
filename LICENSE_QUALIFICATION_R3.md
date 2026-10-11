# Licenze e completamento dei dati europei

Borghi in Vista e i pacchetti geografici sono gratuiti. La revisione r3 aggiunge due database nazionali britannici autonomi sotto Open Government Licence 3.0. I database misti OSM/GeoNames rimangono sospesi per i requisiti specifici descritti sotto: la gratuità non elimina gli obblighi sulle fonti.

## Provenienza dei candidati sospesi

Il replay di tutti i database intermedi identifica 296.589 candidati non pubblicati: 292.001 nodi e 4.588 way OSM. Nome e coordinate provengono da OSM, ma tutti i record ammessi dipendono anche dalla corroborazione GeoNames. In 1.480 casi questa corroborazione determina il paese e in tre casi la scelta del vertice fisico della way. La deduplicazione e la selezione precedono l'esportazione; cancellare le colonne di provenienza non annulla queste dipendenze.

Anche `scripts/import_osm.py` usa GeoNames per ammettere alcuni nodi vicini alla costa e per scegliere il paese fra coperture sovrapposte. Il ledger di 8.142.134 osservazioni non è quindi una copia neutra e completa di tutti i possibili POI OSM indipendenti. Gli snapshot PBF e i checkpoint delle importazioni concluse restano conservati.

Questi fatti sono verificati da `audit_withheld_provenance.py`. Il report locale conserva i conteggi per pacchetto, la prova della sorgente e i campioni. La pubblicazione non include i database misti sospesi.

## Distribuzione ODbL della derivazione esistente

La prima soluzione è praticabile per una derivazione OSM le cui ulteriori fonti siano compatibili. La [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/) richiede, fra l'altro, le notifiche di licenza, il rispetto della condivisione della banca dati derivata e l'accesso machine-readable alla derivazione o alle modifiche. Rendere pubblico l'intero SQLite e la ricetta di produzione permetterebbe di soddisfare il requisito di accesso della sezione 4.6. Non risolve da solo la compatibilità delle componenti aggiuntive prevista dalla sezione 4.4(d).

Il [README ufficiale del dump GeoNames](https://download.geonames.org/export/dump/readme.txt) indica CC BY 4.0. Le condizioni di attribuzione e sulle misure tecnologiche efficaci della [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) restano applicabili anche ai diritti sulle componenti usate. La [posizione OSMF sulla compatibilità](https://osmfoundation.org/wiki/Licence/Licence_Compatibility) e il suo [modello di autorizzazione CC BY 4.0](https://osmfoundation.org/wiki/Licence/Waiver_and_Permission_Templates/Cover_letter_and_waiver_template_for_CC_BY_4.0) individuano attribuzione e misure tecnologiche come punti da chiarire per l'integrazione in ODbL. Quel modello non è una waiver già concessa da GeoNames a questo progetto.

Non si conclude che ogni possibile combinazione sia vietata. Si conclude che questa specifica combinazione non ha ancora una base di compatibilità dimostrata. Un vecchio messaggio informale del forum, relativo a un diverso contesto, non viene promosso ad autorizzazione corrente per i dump congelati.

### Quesito preciso per il titolare o un parere legale

La banca dati contiene nomi e coordinate OSM ed è selezionata, assegnata al paese e in parte ancorata mediante il dump GeoNames CC BY 4.0. Si propone di pubblicare gratuitamente l'intero database derivato sotto ODbL 1.0, senza DRM, con attribuzione separata GeoNames, snapshot identificati tramite SHA-256 e materiali per riprodurre la trasformazione. È sufficiente questo schema a rispettare simultaneamente CC BY 4.0 2(a)(5)(B), 3 e 4 e ODbL 4.4(d), 4.6, 4.7(b) e 4.8, incluse le redistribuzioni downstream? Oppure serve una permission/waiver del titolare GeoNames che confermi attribuzione e misure tecnologiche secondo il modello OSMF?

Prima di pubblicare i 296.589 record serve una risposta qualificata per questo schema concreto oppure un'autorizzazione scritta del titolare. Nessuna richiesta di autorizzazione è stata inviata automaticamente; nessuna waiver viene inventata. Non basta una dichiarazione che entrambe le fonti siano open data.

## Derivazione realmente basata solo su OSM

È una seconda strada possibile sotto ODbL, ma non equivale a filtrare il vecchio ledger o a togliere il campo GeoNames. Richiede una nuova derivazione dai PBF già congelati, con ammissione, paese, scelta dell'anchor e controllo semantico indipendenti da GeoNames. Non richiede di scaricare di nuovo gli originali né di rifare le importazioni già concluse.

La presenza di un QID OSM non dimostra da sola identità, tipo e coordinate. Usare proprietà Wikidata CC0 come validazione richiederebbe prima controlli di identità geografica e provenienza, senza promuovere il QID del comune a una frazione o a un monumento. Non si attiva questa sostituzione in modo indiscriminato e non si abbassano i gate solo per aumentare i record READY.

## Soluzione nazionale applicata

La r3 applica la terza opzione: [OS Open Names](https://www.ordnancesurvey.co.uk/products/os-open-names), distribuito dall'API pubblica ufficiale Ordnance Survey e verificato contro il checksum del produttore. Il prodotto comprende la Gran Bretagna, non l'Irlanda del Nord. Lo snapshot CSV congelato è di 103.259.564 byte, SHA-256 `6175912f1a3be7fffe556b4621a8d0686f1ea145e20ca61ce2b115a75a9bd69f`.

La licenza è [Open Government Licence 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), con le dichiarazioni originali Ordnance Survey, Royal Mail e National Statistics conservate integralmente negli archivi. Il diritto di riutilizzo viene applicato al prodotto nazionale così licenziato, non inferito da un confronto con OSM. I database britannici non sono mescolati con i dati OSM/GeoNames.

La selezione usa soltanto tipo esplicito, nome, identificativo e punto della fonte nazionale e il perimetro congelato Natural Earth. I campi `SAME_AS_GEONAMES` e DBpedia non sono usati né copiati. Questo non presume che il produttore nazionale non abbia mai consultato fonti esterne; si basa sulla licenza del suo prodotto.

Sono ammessi esclusivamente City, Town, Village, Hamlet, Waterfall e Coastal Headland. Other Settlement, Suburban Area, Hill Or Mountain e oggetti areali senza geometria/anchor adeguati non diventano nuove classi arbitrarie. Il punto originale OS viene trasformato con OSTN15 da EPSG:27700 a EPSG:4326; non viene sostituito con il centro di un bounding box. Quote, popolazione e incertezza di rilievo non qualificate rimangono NULL. La precisione nominale dell'operazione di coordinate non è una garanzia di precisione del punto geografico.

Ogni SQLite conserva identità stabile della fonte, versione/hash/URL, codice di tipo originale, regola di selezione, punto di griglia originale e prova della trasformazione. Il database derivato completo, le attribuzioni originali e il testo OGL sono machine-readable negli ZIP pubblici. Tutte le sette categorie e i quaranta tipi restano nel contratto: i tipi assenti da questa fonte non sono riempiti artificialmente.

## Indipendenza dei livelli

I database ufficiali swisstopo, i nuovi database OS Open Names e il terreno Copernicus hanno selezioni autonome e licenze proprie. Condividere un catalogo o una classificazione del prodotto non implica di per sé un join delle rispettive banche dati.

I POI OSM ammessi grazie a GeoNames non diventerebbero invece livelli indipendenti soltanto spostando le due fonti in file diversi. Le [linee guida OSMF sulle banche dati collettive](https://osmfoundation.org/wiki/Licence/Community_Guidelines/Collective_Database_Guideline_Guideline) e sui [livelli orizzontali](https://osmfoundation.org/wiki/Licence/Community_Guidelines/Horizontal_Map_Layers_-_Guideline) non giustificano la rimozione di una dipendenza effettiva di selezione o deduplicazione. Per un futuro lettore va mantenuta l'indipendenza, senza sostituzioni e cross-source deduplication non qualificate.

## Geometrie e terreno ancora incompleti

Le 202.116 relazioni areali completate sono state classificate. Il confronto con i punti nazionali già selezionati trova 95 riscontri nome/tipo/punto interno a poligono fisico non amministrativo. Questo audit non modifica la selezione nazionale e non aggiunge righe areali al runtime. Un riscontro geometrico non certifica riconoscibilità sul panorama. Gli altri label/centroidi restano sospesi; 297 occorrenze non assemblabili sono conservate, senza geometria sintetica.

I 135 DEM READY della r1 restano immutati. Tredici ulteriori unità non mostrano terra nelle due fonti costiere controllate, nei limiti della risoluzione; non è prova che ogni microisola sia assente. `dem-eu-07-10` contiene evidenza di Rockall, ma le celle GLO-90 e GLO-30 N57W014 interrogate restituiscono 404. Serve una fonte altimetrica disponibile, licenziata e con datum qualificato. UNKNOWN non diventa quota zero.

## Aggiornamenti e limiti della distribuzione

Ogni nuova revisione conserva sorgenti/hash, ID e classificazioni, include licenze originali, supera replay indipendente e installazione portabile staged con rollback e viene firmata Ed25519. Le release r1/r2 non vengono sovrascritte; gli URL sono versionati. Il catalogo distingue READY, WITHHELD, builtin e terreno UNKNOWN. Il prodotto e i dati sono gratuiti, senza entitlement geografico.

La r3 è un avanzamento concreto della distribuzione, non il completamento di tutti i POI europei. Nessuna verifica umana sul campo o percentuale di precisione viene inventata. Android 161 non è modificato e non contiene ancora il lettore/download di questi pacchetti.
