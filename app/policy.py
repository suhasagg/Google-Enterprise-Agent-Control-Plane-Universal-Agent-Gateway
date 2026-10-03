def decide(principal,cap,step):
 if step.risk=="HIGH" or (cap and cap.risk=="HIGH"):return "REQUIRE_APPROVAL"
 if "blocked" in principal.attributes.get("labels",[]):return "DENY"
 return "ALLOW"
