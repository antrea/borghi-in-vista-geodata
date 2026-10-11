"""No publication by default. gh CLI owns authentication; credentials never enter artifacts."""
import argparse,pathlib,json,subprocess,sys,time
from verify_release import verify,sha
def run(args,json_result=False):
    p=subprocess.run(['gh',*args],check=False,capture_output=True,text=True)
    if p.returncode:raise RuntimeError('GITHUB_CLI_FAILED:'+str(args[:3])) # no token/response body logging
    return json.loads(p.stdout) if json_result else p.stdout
def all_assets(target,release_id):
    pages=run(['api',f'repos/{target}/releases/{release_id}/assets?per_page=100','--paginate','--slurp'],True)
    return [asset for page in pages for asset in page]

def find_release(target,tag):
    # An unpublished draft may have no tag ref yet: GET releases/tags/{tag} can 404.
    pages=run(['api',f'repos/{target}/releases?per_page=100','--paginate','--slurp'],True)
    matches=[release for page in pages for release in page if release['tag_name']==tag]
    if len(matches)>1:raise ValueError('DUPLICATE_RELEASE_TAG')
    return matches[0] if matches else None
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--dry-run',action='store_true');parser.add_argument('--publish-authorized',action='store_true');parser.add_argument('--pin',required=True);args=parser.parse_args();folder=pathlib.Path(__file__).resolve().parent
    m=verify(folder,args.pin);cfg=json.loads((folder/'github-config.json').read_text());owner=cfg['owner'];tag=cfg['tag'];repo=cfg['repository']
    if cfg['owner']!=m['github']['owner'] or tag!=m['github']['tag'] or repo!=m['github']['repository']:raise ValueError('CONFIG_NOT_SIGNED_MANIFEST')
    files=sorted(p for p in folder.iterdir() if p.is_file());print('DRY_RUN' if args.dry_run or not args.publish_authorized else 'EXPLICITLY_AUTHORIZED_DRAFT_UPLOAD',len(files),'assets',sum(p.stat().st_size for p in files),'bytes')
    if args.dry_run or not args.publish_authorized:
        print('OWNER_NOT_CONFIGURED' if not owner else 'TARGET '+owner+'/'+repo+' '+tag);print('NO_NETWORK_PUBLICATION_PERFORMED');return
    if not owner:raise ValueError('OWNER_REQUIRED_NEW_SIGNED_CATALOG_REVISION')
    target=owner+'/'+repo
    # Do not create repositories or mutate an already stable release.
    p=subprocess.run(['gh','release','view',tag,'-R',target,'--json','isDraft,assets'],capture_output=True,text=True)
    if p.returncode:run(['release','create',tag,'-R',target,'--draft','--title',tag,'--notes','BIV-GEODATA-V1 signed assets; see manifest and licenses.'])
    else:
        if not json.loads(p.stdout)['isDraft']:raise ValueError('STABLE_RELEASE_IS_IMMUTABLE_NEW_TAG_REQUIRED')
    release=find_release(target,tag)
    if release is None:raise ValueError('DRAFT_RELEASE_NOT_VISIBLE')
    if not release['draft']:raise ValueError('RELEASE_NOT_DRAFT')
    existing={a['name']:a for a in all_assets(target,release['id'])}
    if set(existing)-{p.name for p in files}:raise ValueError('UNKNOWN_REMOTE_ASSET')
    for path in files:
        old=existing.get(path.name)
        if old:
            if old.get('digest')!='sha256:'+sha(path) or old['size']!=path.stat().st_size:raise ValueError('EXISTING_ASSET_UNVERIFIED_OR_MISMATCH_NEVER_CLOBBER')
            print('EXACT_REMOTE_ASSET_SKIP',path.name);continue
        run(['release','upload',tag,str(path),'-R',target]);time.sleep(1)
    after=find_release(target,tag)
    if after is None:raise ValueError('UPLOADED_RELEASE_NOT_VISIBLE')
    for a in all_assets(target,after['id']):
        path=folder/a['name']
        if a.get('digest')!='sha256:'+sha(path) or a['size']!=path.stat().st_size:raise ValueError('REMOTE_POST_UPLOAD_VERIFICATION')
    print('DRAFT_UPLOAD_VERIFIED_STABLE_PUBLICATION_REQUIRES_SEPARATE_OPERATOR_ACTION')
if __name__=='__main__':main()
