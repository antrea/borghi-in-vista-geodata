"""Portable signed multi-release catalog verifier; never assumes missing files pass."""
from pathlib import Path
import json,hashlib,base64,zipfile,sqlite3,sys
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as source:
        for data in iter(lambda:source.read(4194304),b''):h.update(data)
    return h.hexdigest()

def verify(folder,pin,asset_directories=()):
    folder=Path(folder);data=(folder/'manifest.json').read_bytes();catalog=json.loads(data)
    public=json.loads((folder/'signing-public-key.json').read_text());signature=json.loads((folder/'manifest.signature.json').read_text())
    raw=base64.b64decode(public['public_key_base64'])
    if not pin or hashlib.sha256(raw).hexdigest()!=pin or public['fingerprint_sha256']!=pin:raise ValueError('EXTERNAL_TRUST_PIN_REQUIRED_OR_WRONG')
    if hashlib.sha256(data).hexdigest()!=signature['sha256']:raise ValueError('CATALOG_HASH')
    Ed25519PublicKey.from_public_bytes(raw).verify(base64.b64decode(signature['signature_base64']),data)
    if (catalog['format'],catalog['schema_version'])!=('BIV-GEODATA-V1',1):raise ValueError('CATALOG_SCHEMA')
    if len({a['id'] for a in catalog['assets']})!=len(catalog['assets']):raise ValueError('DUPLICATED_PACKAGE_ID')
    for entry in catalog['supporting_files']:
        if Path(entry['name']).name!=entry['name']:raise ValueError('SUPPORTING_PATH')
        p=folder/entry['name']
        if sha(p)!=entry['sha256'] or p.stat().st_size!=entry['bytes']:raise ValueError('SIGNED_SUPPORTING_HASH')
    for line in (folder/'checksums.sha256').read_text().splitlines():
        digest,name=line.split('  ',1)
        if Path(name).name!=name or sha(folder/name)!=digest:raise ValueError('LOCAL_RELEASE_CHECKSUM')
    verified=[];unavailable=[]
    for asset in catalog['assets']:
        name=asset['archive_name']
        if Path(name).name!=name or asset['state']!='READY':raise ValueError('ASSET_PATH_OR_STATE')
        expected=f"https://github.com/antrea/borghi-in-vista-geodata/releases/download/{asset['release_tag']}/{name}"
        if asset['url']!=expected:raise ValueError('ASSET_VERSIONED_URL')
        options=[p/name for p in [folder,*map(Path,asset_directories)] if (p/name).exists()]
        if not options:unavailable.append(name);continue
        path=options[0]
        if path.stat().st_size!=asset['archive_bytes'] or sha(path)!=asset['archive_sha256']:raise ValueError('ASSET_HASH')
        with zipfile.ZipFile(path) as z:
            if z.testzip() is not None:raise ValueError('ZIP_CRC')
            data=z.read('data.sqlite');meta=json.loads(z.read('metadata.json'))
            if len(data)!=asset['database_bytes'] or hashlib.sha256(data).hexdigest()!=asset['database_sha256']:raise ValueError('DATABASE_HASH')
            if meta['state']!='READY' or not meta['release_ready'] or not all(meta['gates'].values()):raise ValueError('INNER_READY_GATE')
        c=sqlite3.connect(':memory:');c.deserialize(data)
        try:
            if c.execute('pragma integrity_check').fetchone()[0]!='ok' or c.execute('pragma foreign_key_check').fetchall():raise ValueError('DATABASE_INTEGRITY')
            if c.execute('pragma application_id').fetchone()[0]!=0x42495647 or c.execute('pragma user_version').fetchone()[0]!=1:raise ValueError('DATABASE_SCHEMA')
            metadata=dict(c.execute('select * from metadata'))
            if metadata['kind']!=asset['kind']:raise ValueError('DATABASE_KIND')
        finally:c.close()
        verified.append(name)
    return {'catalog':catalog,'verified_local_assets':verified,'not_locally_verified':unavailable,'signature_verified':True}

if __name__=='__main__':
    if len(sys.argv)<2:raise SystemExit('Provide independently trusted SHA-256 public-key fingerprint, then optional asset cache folders.')
    result=verify(Path(__file__).resolve().parent,sys.argv[1],sys.argv[2:])
    print('SIGNED_CATALOG_PASS',len(result['verified_local_assets']),'local ZIPs verified;',len(result['not_locally_verified']),'remote ZIPs NOT verified by this local run')
