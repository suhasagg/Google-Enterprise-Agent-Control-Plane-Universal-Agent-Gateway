from pydantic import BaseModel,Field
from typing import Any,Literal
class Goal(BaseModel):tenant_id:str;principal_id:str;goal:str;context:dict[str,Any]=Field(default_factory=dict)
class Capability(BaseModel):id:str;name:str;kind:Literal["agent","mcp","rest","grpc","skill"];description:str;endpoint:str="";protocol:str="local";risk:Literal["READ","WRITE","HIGH"]="READ";tags:list[str]=Field(default_factory=list);version:str="1"
class Step(BaseModel):key:str;capability:str;depends_on:list[str]=Field(default_factory=list);input:dict[str,Any]=Field(default_factory=dict);risk:Literal["READ","WRITE","HIGH"]="READ"
class Plan(BaseModel):objective:str;steps:list[Step]
class Principal(BaseModel):tenant_id:str;principal_id:str;agent_id:str;spiffe_id:str;roles:list[str]=Field(default_factory=list);attributes:dict[str,Any]=Field(default_factory=dict)
