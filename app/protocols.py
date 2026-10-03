from app.config import settings
import httpx
async def invoke(cap,payload,p):
 if cap.protocol in {"mcp","a2a","rest"} and getattr(settings,cap.protocol+"_mode")=="mock":return {"protocol":cap.protocol,"target":cap.id,"status":"SUCCEEDED","result":{"echo":payload}}
 async with httpx.AsyncClient(timeout=20) as c:return (await c.post(cap.endpoint,json=payload,headers={"x-agent-spiffe":p.spiffe_id})).json()
