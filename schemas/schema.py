from pydantic import BaseModel

class User_shema(BaseModel):
    id: int
    t1: str
    t2: str
    t3:str
    t4:str
