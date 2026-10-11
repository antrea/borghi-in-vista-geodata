# BIV-GEODATA-V1 distribution

Only the files in `GITHUB_RELEASE_READY/` are distributable. The signed catalog explicitly distinguishes READY assets, Italy builtin, blocked units and unfinished production. A partial catalog must never be described as complete Europe POI coverage. No audit database or signing private key is included.

The authenticated project owner is `antrea`. The public repository is https://github.com/antrea/borghi-in-vista-geodata . Catalogs contain definitive HTTPS asset URLs under its immutable release tags. The initial terrain subset is `geodata-eu-core-20261009-r1`. Do not edit a published manifest in place. New content needs a new release tag and signature. Publication state is verified from GitHub and recorded separately, not guessed from a field inside the signed catalog.

The standalone scripts require Python 3.12+, `cryptography` and, for an explicitly authorized upload only, GitHub CLI authenticated locally. Authentication is not copied into this delivery.

Local verification: `python verify_release.py 1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd`.

Upload simulation: `python upload_release.py --dry-run --pin 1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd`.

After owner configuration, a newly signed revision, and separate publication authorization: `python upload_release.py --publish-authorized --pin 1d19021c63713e5a1df784a25102fe277497353f81eb02afe4c5b44226607ccd`. This creates/resumes a **draft**, never overwrites unknown assets, verifies GitHub asset digests, and never publishes the draft automatically.

The future Android reader must pin the public key via an independently trusted app distribution. Downloading a key and manifest from the same untrusted endpoint is not authenticity. It must verify both compressed and database hashes, reader capabilities, schema, and validity masks before an atomic install, preserving the previous good database for rollback.

DEM is Copernicus GLO-90 DSM in EGM2008, not a DTM or survey-grade surface. Missing heights remain UNKNOWN, including sea or absent source cells. Tile coverage is not complete height availability. Height estimates touching UNKNOWN must not declare an unobstructed view. Android 161 is unchanged and cannot yet consume this new mask/pack contract.

Asset limits checked locally: fewer than 1000 files per release and each file strictly below 2 GiB. No undocumented storage quota is presumed.
