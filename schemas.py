from pydantic import BaseModel

class SAddMachinery(BaseModel):
    brand: str
    model: str
    yearManufacture: str
    type: str
    vin: str
    stateNumber: str
    status: str | None = None

class SMachinery(SAddMachinery):
    id: int