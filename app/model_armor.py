BLOCK=["ignore previous instructions","reveal system prompt","exfiltrate secret","steal credentials"]
def inspect_text(t):
 hits=[x for x in BLOCK if x in t.lower()]
 return {"allowed":not hits,"findings":hits}
