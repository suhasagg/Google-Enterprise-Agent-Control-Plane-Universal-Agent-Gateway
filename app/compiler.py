import networkx as nx
def compile_plan(p):
 keys={s.key for s in p.steps}
 if len(keys)!=len(p.steps):raise ValueError("duplicate step")
 g=nx.DiGraph()
 for s in p.steps:
  g.add_node(s.key)
  for d in s.depends_on:
   if d not in keys:raise ValueError("missing dependency")
   g.add_edge(d,s.key)
 if not nx.is_directed_acyclic_graph(g):raise ValueError("cycle")
 return g
