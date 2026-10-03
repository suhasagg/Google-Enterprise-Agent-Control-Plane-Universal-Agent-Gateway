import networkx as nx
from app.compiler import compile_plan
from app.registry import get_cap
from app.policy import decide
from app.model_armor import inspect_text
from app.protocols import invoke
from app.agents import local_agent
from app.security import action_hash
class Runtime:
 async def execute(self,pl,p,approved=None):
  approved=set(approved or []);g=compile_plan(pl);r={}
  for k in nx.topological_sort(g):
   s=next(x for x in pl.steps if x.key==k)
   if s.capability=="human.approval":
    h=action_hash({"step":s.model_dump(),"deps":{d:r.get(d) for d in s.depends_on}});r[k]={"status":"APPROVED" if k in approved else "WAITING_APPROVAL","action_hash":h}
    if k not in approved:break
    continue
   cap=get_cap(s.capability)
   if not cap:r[k]={"status":"FAILED","error":"unknown capability"};break
   armor=inspect_text(str(s.input))
   if not armor["allowed"]:r[k]={"status":"BLOCKED","findings":armor["findings"]};break
   d=decide(p,cap,s)
   if d=="DENY":r[k]={"status":"DENIED"};break
   if d=="REQUIRE_APPROVAL" and k not in approved:r[k]={"status":"WAITING_APPROVAL","action_hash":action_hash(s.model_dump())};break
   payload={"input":s.input,"dependencies":{x:r.get(x) for x in s.depends_on}}
   r[k]=await local_agent(cap.id,payload) if cap.protocol=="local" else await invoke(cap,payload,p)
  return r
