from app.domain import Plan,Step
def plan(g):
 x=g.goal.lower()
 if "code" in x or "repository" in x:return Plan(objective=g.goal,steps=[Step(key="research",capability="research"),Step(key="code",capability="coding",depends_on=["research"],risk="WRITE"),Step(key="approval",capability="human.approval",depends_on=["code"],risk="HIGH")])
 if "data" in x or "sql" in x:return Plan(objective=g.goal,steps=[Step(key="research",capability="research"),Step(key="analyze",capability="data",depends_on=["research"])])
 return Plan(objective=g.goal,steps=[Step(key="research",capability="research"),Step(key="delegate",capability="a2a.specialist",depends_on=["research"])])
