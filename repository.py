from database import new_session, MachineryTable
from schemas import SAddMachinery, SMachinery
from sqlalchemy import select

class MachineryRepository:
    @classmethod
    async def add_one(cls, machinery: SAddMachinery) -> int:
        async with new_session() as session:
            machinery_dict = machinery.model_dump()
            new_machinery = MachineryTable(**machinery_dict)
            session.add(new_machinery)
            await session.flush()
            await session.commit()
            print(new_machinery.id)
            return new_machinery.id

    @classmethod
    async def find_all(cls) -> list[SMachinery]:
        async with new_session() as session:
            query = select(MachineryTable)
            result = await session.execute(query)
            machinery_models = result.scalars().all()
            machinery_schemas = [
                SMachinery.model_validate(machinery_model.__dict__) for machinery_model in machinery_models
            ]
            return machinery_schemas

