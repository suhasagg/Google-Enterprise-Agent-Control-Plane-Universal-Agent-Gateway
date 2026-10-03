from app.domain import Capability
CAPS=[
 Capability(id="research",name="Research Agent",kind="agent",description="Evidence-oriented research",tags=["research","knowledge"]),
 Capability(id="coding",name="Coding Agent",kind="agent",description="Candidate code generation",risk="WRITE",tags=["code","engineering"]),
 Capability(id="data",name="Data Agent",kind="agent",description="Governed data analysis",tags=["sql","analytics"]),
 Capability(id="mcp.crm",name="CRM MCP",kind="mcp",description="CRM tool server",endpoint="mock://crm",protocol="mcp",risk="WRITE",tags=["crm"]),
 Capability(id="a2a.specialist",name="Specialist Agent",kind="agent",description="A2A specialist",endpoint="mock://specialist",protocol="a2a",tags=["delegate"]),
 Capability(id="rest.ticket",name="Ticket API",kind="rest",description="Ticket API",endpoint="mock://ticket",protocol="rest",risk="WRITE",tags=["support"])
]
def all_caps():return CAPS
def get_cap(cid):return next((x for x in CAPS if x.id==cid),None)
