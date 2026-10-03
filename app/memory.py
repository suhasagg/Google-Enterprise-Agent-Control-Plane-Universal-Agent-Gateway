class SixLayerMemory:
 def __init__(self):self.layers={x:{} for x in ["working","session","episodic","semantic","entity","procedural"]}
 def put(self,l,k,v):self.layers[l].__setitem__(k,v)
 def get(self,l,k):return self.layers[l].get(k)
