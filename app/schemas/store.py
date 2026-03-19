from pydantic import BaseModel 

class StoreBase(BaseModel):
    name: str 


class StoreCreate(StoreBase):
    pass

class StoreOut(StoreBase):
    id: str
    owner_id: str

    class Config:
        from_attributes = True 