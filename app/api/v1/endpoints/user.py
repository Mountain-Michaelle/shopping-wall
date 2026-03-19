
from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session

from app.db.deps import get_db 
from app.models.user import User
from app.schemas.user import UserCreate, UserOut



router = APIRouter() 

@router.post("/create", response_model=UserOut)
def create_user(user:UserCreate, db:Session = Depends(get_db)):
    db_user = User(email=user.email, hashed_password=user.password)
    db.add(get_db)
    db.commit()
    db.refresh(db_user)

    return db_user