from app.registry import all_caps
def route(q,k=5):
 a=set(q.lower().split()); scored=[]
 for c in all_caps():
  b=set((c.name+" "+c.description+" "+" ".join(c.tags)).lower().split());scored.append((len(a&b)/max(1,len(a|b)),c))
 return [c for _,c in sorted(scored,key=lambda x:x[0],reverse=True)[:k]]
