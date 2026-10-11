"""Standalone portable reader/checksum check. Requires cryptography for Ed25519 verification."""
import pathlib,json,hashlib,base64,zipfile,sqlite3,sys
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(4194304),b''):h.update(block)
    return h.hexdigest()
def verify(folder,pinned_fingerprint=None):
    folder=pathlib.Path(folder);data=(folder/'manifest.json').read_bytes();manifest=json.loads(data);sig=json.loads((folder/'manifest.signature.json').read_text());key=json.loads((folder/'signing-public-key.json').read_text());public=base64.b64decode(key['public_key_base64'])
    fingerprint=hashlib.sha256(public).hexdigest()
    if pinned_fingerprint and fingerprint!=pinned_fingerprint:raise ValueError('SIGNER_NOT_PINNED_KEY')
    if fingerprint!=key['fingerprint_sha256'] or hashlib.sha256(data).hexdigest()!=sig['sha256']:raise ValueError('MANIFEST_OR_SIGNER_DIGEST')
    Ed25519PublicKey.from_public_bytes(public).verify(base64.b64decode(sig['signature_base64']),data)
    if manifest['format']!='BIV-GEODATA-V1' or manifest['schema_version']!=1:raise ValueError('MANIFEST_CONTRACT')
    for supporting in manifest['supporting_files']:
        if pathlib.Path(supporting['name']).name!=supporting['name']:raise ValueError('SUPPORTING_PATH')
        p=folder/supporting['name']
        if sha(p)!=supporting['sha256'] or p.stat().st_size!=supporting['bytes']:raise ValueError('SIGNED_SUPPORTING_IDENTITY')
    for line in (folder/'checksums.sha256').read_text().splitlines():
        digest,name=line.split('  ',1)
        if pathlib.Path(name).name!=name or sha(folder/name)!=digest:raise ValueError('FILE_CHECKSUM:'+name)
    for a in manifest['assets']:
        path=folder/a['archive_name']
        if path.name!=a['archive_name'] or sha(path)!=a['archive_sha256'] or path.stat().st_size!=a['archive_bytes']:raise ValueError('ASSET_IDENTITY')
        with zipfile.ZipFile(path) as z:
            if z.testzip() is not None:raise ValueError('ZIP_CRC')
            if z.getinfo('data.sqlite').file_size!=a['database_bytes']:raise ValueError('DB_UNCOMPRESSED_SIZE')
            meta=json.loads(z.read('metadata.json'));database=z.read('data.sqlite')
            if meta['state']!='READY' or not meta['release_ready'] or not all(meta['gates'].values()):raise ValueError('INNER_NOT_READY')
            if hashlib.sha256(database).hexdigest()!=a['database_sha256']:raise ValueError('DB_HASH')
        c=sqlite3.connect(':memory:')
        try:
            c.deserialize(database);c.execute('pragma query_only=on')
            if c.execute('pragma integrity_check').fetchone()[0]!='ok' or c.execute('pragma foreign_key_check').fetchall():raise ValueError('DB_INTEGRITY')
            if c.execute('pragma user_version').fetchone()[0]!=1 or c.execute('pragma application_id').fetchone()[0]!=0x42495647:raise ValueError('READER_SCHEMA')
            m=dict(c.execute('select * from metadata'))
            if m['format']!='BIV-GEODATA-V1' or m['kind']!=a['kind']:raise ValueError('READER_KIND')
        finally:c.close()
    return manifest
if __name__=='__main__':
    manifest=verify(pathlib.Path(__file__).resolve().parent,sys.argv[1] if len(sys.argv)>1 else None);print('RELEASE_LOCAL_VERIFIED',len(manifest['assets']),manifest['distribution_state'])
