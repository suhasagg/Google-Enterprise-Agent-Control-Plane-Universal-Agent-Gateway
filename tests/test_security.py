from app.security import action_hash,spiffe
def test_hash():assert action_hash({"b":2,"a":1})==action_hash({"a":1,"b":2})
def test_spiffe():assert spiffe("t","a").startswith("spiffe://")
