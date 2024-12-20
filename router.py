from fastapi import APIRouter
from typing import Annotated
from fastapi import FastAPI, Depends
from schemas import SAddMachinery, SMachinery
from repository import MachineryRepository


router = APIRouter(
    prefix="/machinery",
    tags=["техника"]
)

@router.get("")
async def get_machinery() -> list[SMachinery]:
    machinery_list = await MachineryRepository.find_all()
    return machinery_list

@router.post("")
async def add_machinery(machinery: Annotated[SAddMachinery, Depends()]):
    machinery_id = await MachineryRepository.add_one(machinery)
    return {"ok": True, "machinery_id": machinery_id}