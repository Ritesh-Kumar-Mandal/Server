from fastapi import APIRouter, Depends, status
from server import schemas
from sqlalchemy.orm import Session
from server.repository import user
from typing import List
from server.utils import dbUtil


router = APIRouter(
    prefix="/user",
    tags=['User'],
    dependencies=[Depends(dbUtil.get_db)]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request: schemas.CreateUser, db: Session = Depends(dbUtil.get_db)):
    return user.create(request, db)

@router.get('/', response_model=List[schemas.ShowUser])
def all(db: Session = Depends(dbUtil.get_db)):
    return user.get_all_user_profile(db)