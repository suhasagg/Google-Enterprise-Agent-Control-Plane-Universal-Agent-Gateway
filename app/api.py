from fastapi import APIRouter,Depends
from app.security import auth
from app.domain import Goal
from app.registry import all_caps
from app.router import route
from app.service import execute
router=APIRouter(prefix="/v1",dependencies=[Depends(auth)])
@router.get("/registry")
async def registry():return [x.model_dump() for x in all_caps()]
@router.get("/discover")
async def discover(q:str):return [x.model_dump() for x in route(q)]
@router.post("/goals")
async def goals(g:Goal):return await execute(g)
