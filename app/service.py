from app.domain import Principal
from app.security import spiffe
from app.planner import plan
from app.runtime import Runtime
async def execute(g):
 p=Principal(tenant_id=g.tenant_id,principal_id=g.principal_id,agent_id="supervisor",spiffe_id=spiffe(g.tenant_id,"supervisor"),roles=["agent_user"])
 pl=plan(g);return {"identity":p.model_dump(),"plan":pl.model_dump(),"results":await Runtime().execute(pl,p)}
