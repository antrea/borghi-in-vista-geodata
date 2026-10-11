# BIV-GEODATA-V1 — contract 1

SQLite in deterministic ZIP Deflate. Content revision and schema version are independent. This format targets a future reader; Android 161 is deliberately unchanged and does not yet implement this pack/UNKNOWN-mask contract.

## Bundle

`data.sqlite`, `metadata.json`, `coverage.geojson`, `LICENSES.txt`, original license documents where necessary. No quarantine, source contributor metadata, private key, local path, raw importer ledger or diagnostics in a public asset.

SQLite: `user_version=1`, `application_id=0x42495647`, metadata `format=BIV-GEODATA-V1` and `kind=POI|DEM`. Unknown schema/required capability must fail closed. ZIP and decompressed SQLite SHA-256, sizes and license references are in the signed catalog. A failed stage never replaces a last good install. Keep a previous good database for explicit rollback; content updates may not silently migrate schemas.

## Identity / points

POI global string identities are source-qualified (`osm:node:<id>` or official source UUID). Numeric IDs use the frozen high-range SHA-256 62-bit scheme and are checked globally for collisions. Renames and coordinate revisions do not change IDs. Italian builtin IDs/assets remain untouched. Cross-source similarity is not automatic identity; unresolved duplicates stay outside release until qualified. Original source type code and classifier rule are separate columns.

Seven category and forty type identities are unchanged. `places` contains one primary local name, never a translation inferred from Wikidata. `place_names` contains source-attested `und`, `LOCALIZED_ATTESTED`, `OFFICIAL_LOCAL` and explicitly non-preferred aliases when supplied. Resolver: exact requested tag → base → verified local/und → original. No English universal toponym fallback, no name-based deduplication. QID does not authorize a display name or coordinates.

Horizontal CRS WGS84/EPSG:4326. Source node coordinates remain unmodified. Coordinate agreement is *not* survey accuracy. `horizontal_uncertainty_m=NULL` explicitly means no measured survey uncertainty; reader must not invent a precision figure. Areal features require a documented physical/polygon anchor; a point centroid alone is insufficient. Unqualified polygons and complex historical/religious status remain in separate audit, not runtime data. Runtime elevation is nullable: incompatible national/ellipsoidal heights are not silently converted to MSL.

## Terrain

`terrain_tiles(south,west,height_blob,validity_blob,...)` has 401×401 samples, row south-to-north, column west-to-east. WGS84; 9 arcseconds; floor quantization 1m; EGM2008; source GLO-90 is DSM, not bare-earth DTM. Longitude sampling of the source varies with latitude and is read from each raster's actual affine transform and width. No fixed 1200-column assumption at high latitude.

Height payload BIVT planar-predictor v1: 16-byte header, zig-zag uint16 residual byte planes and zlib. Validity payload: zlib of row-major packed bits, least-significant-bit first, 160801 meaningful bits. Mask 0 is UNKNOWN even if the associated encoded height is zero. A reader lacking this mask must reject the pack. Never substitute UNKNOWN with open/free terrain. Bilinear/visibility sampling touching UNKNOWN propagates UNKNOWN conservatively.

Shared boundary height and mask samples must be equal. A catalog coverage polygon is a tile inventory, **not** a claim that every point has known height. Known/unknown counts and absent-source diagnostics are explicit. The 100 km halo uses conservative enclosing rectangles derived from the WGS84 minimum metric radius, boundary chains with coordinate-length upper bound at most 1 km, and 500 m slack. The closure added 54 cells without changing the 149 package identities. All 601,134 boundary samples and all core-footprint polygons are covered by the tile inventory; this is not a claim of complete source height availability. Packages with no known sample are not READY.

## Distribution / signing

Dedicated Ed25519 catalog signing key, current-user Windows DPAPI encryption at rest, private folder excluded from Git/public delivery. Public key pinning is a future Android requirement. The public-key file downloaded from the same untrusted server is not by itself a trust anchor. Distribution is https://github.com/antrea/borghi-in-vista-geodata ; relative asset names and definitive HTTPS download URLs are both signed. Release tags are immutable; never alter published stable assets.

No network publication without separate explicit authorization. The authorized public repository is `antrea/borghi-in-vista-geodata`; no alternative repository is created. Publication verifies local checksums, refuses unknown/mismatched existing remote assets, resumes exact matches and never uses clobber. No authentication tokens embedded in files. Catalog r2 references the original immutable 135 DEM URLs from r1 and only two new, independently qualified swisstopo point packages. Assets are uploaded to a draft, verified, then published immutably. The main catalog pointer advances only after all new public HTTPS downloads have matching size/hash. Previously signed revisions remain available for rollback.

## Quality meanings

ACCEPTED is an evidence decision, not measured AR accuracy or human inspection. READY requires a nonempty runtime payload, complete technical final-file audit, source/identity/anchor/license gates and honest coverage limitations. Processing all planning units is distinct from exhausting every real-world POI. No artificial fill of missing types, no claim of 100% semantic recall, no invented human review.

## License separation

Copernicus GLO-90 follows its own original terms (the GLO-90 section, not restricted higher-resolution sections). OSM-derived data is subject to ODbL and attribution. GeoNames is CC BY 4.0; a combined derivative is **not automatically declared legally compatible**. OSM Foundation identifies CC BY attribution/technical-measures concerns. Mixed candidates remain pending legal compatibility unless the source-combination basis is resolved. This does not block independent terrain generation. Source ledgers are local, no provider permission or waiver is invented.
