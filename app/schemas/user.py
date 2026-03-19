from pydantic import BaseModel, EmailStr 

# Shared properties
class UserBase(BaseModel):
    email:EmailStr


# Client registration request
class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id:str

    class Config:
        from_attributes = True