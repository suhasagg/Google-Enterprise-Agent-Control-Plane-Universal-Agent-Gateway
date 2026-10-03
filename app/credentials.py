import hashlib,time
def broker(p,target,scopes):
 seed=f"{p.spiffe_id}:{target}:{','.join(scopes)}:{int(time.time()/300)}"
 return {"credential_handle":"cred_"+hashlib.sha256(seed.encode()).hexdigest()[:20],"expires_in":300,"scopes":scopes}
