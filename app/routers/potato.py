from pydantic import BaseModel
#from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter

class Potato(BaseModel):
    id: int
    color: str
    mass: float

#app = FastAPI()
router = MemoryCRUDRouter(schema=Potato)
#app.include_router(router)