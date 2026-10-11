# Borghi in Vista — European geodata packs

Public distribution of independently checked **BIV-GEODATA-V1** data packages.

## Initial distribution: terrain only, partial coverage

[Download the signed release](https://github.com/antrea/borghi-in-vista-geodata/releases/tag/geodata-eu-core-20261009-r1).

- **135 validated DEM packages**, approximately 209 MB compressed in total.
- Copernicus GLO-90 **DSM**, WGS84 horizontal coordinates, EGM2008 heights.
- Each archive contains a SQLite runtime database, coverage, metadata, source references and original license information.
- Unknown elevations have an explicit validity mask. **UNKNOWN is never sea level, flat ground or unobstructed terrain.**
- 14 planned DEM packages with no known samples are not distributed.
- European POI candidates are **not published**: semantic, licensing and review gates remain open. This is not a complete European places database.
- Italy's existing built-in database is unchanged and is not redistributed here.

The signed `manifest.json` distinguishes available packages from unavailable and unfinished planning units. Coverage is a tile inventory, not a claim that every height sample is known. No survey precision or completed human field review is claimed.

## Verify before installing

The catalog uses a dedicated Ed25519 key. Public-key fingerprint:

`1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd`

Pin this fingerprint through an independently trusted channel; downloading a public key and its manifest from the same untrusted endpoint does not create a trust anchor.

Download the release assets to one directory. With Python 3.12+ and `cryptography` installed:

```sh
python verify_release.py 1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd
```

Verification checks signature, sizes, compressed and uncompressed hashes, archive CRC, SQLite integrity, schema and READY gates. An update must be staged and verified before replacing a last good installation.

## Documentation and compatibility

- [Data contract](BIV_GEODATA_V1.md)
- [Distribution, verification and operator upload workflow](DISTRIBUTION.md)
- [Published releases](https://github.com/antrea/borghi-in-vista-geodata/releases)

Android build 161 has **not** been modified and does not yet support downloading or reading these packages. This repository distributes data for a future compatible reader; it is not an Android app release.

## Licenses and privacy

Terrain is distributed under the original Copernicus GLO-90 terms included in each archive, with source attribution. Other data sources do not automatically share that license; POI candidates are withheld until their own gates pass. See each package's `LICENSES.txt`, original license document, metadata and `sources.json`.

No application source, signing private key, credentials, phone logs, user location, photographs, raw importer ledgers, intermediate POI bundles or quarantine databases are included. Large runtime archives are release assets, not Git objects. Published releases are immutable; corrections require a new signed release.
