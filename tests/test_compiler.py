from app.planner import plan
from app.domain import Goal
from app.compiler import compile_plan
def test_compile():assert len(compile_plan(plan(Goal(tenant_id="t",principal_id="p",goal="code repository"))).nodes)==3
