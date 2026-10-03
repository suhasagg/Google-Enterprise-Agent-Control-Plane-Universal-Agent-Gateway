async def local_agent(c,payload):
 if c=="research":return {"status":"SUCCEEDED","evidence":["registry://reference"]}
 if c=="coding":return {"status":"SUCCEEDED","candidate_patch":{"summary":"reference candidate","files":["example.py"]}}
 if c=="data":return {"status":"SUCCEEDED","analysis":{"rows":100,"result":"reference"}}
 return {"status":"SUCCEEDED"}
