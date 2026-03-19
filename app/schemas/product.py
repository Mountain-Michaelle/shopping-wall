from pydantic import BaseModel


class ProductBase(BaseModel):
    name:str
    price:float 



class ProductCreate(ProductBase):
    pass 


class ProductOut(ProductBase):
    int: str
    store_id: str

    class Config:
        from_attributes = True 