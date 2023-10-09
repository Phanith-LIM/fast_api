import uuid
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from core import get_db, ResponseSchema, JWTBearer, JWTRepo
from .entity import Users
from .repositorys import UserRepo

router = APIRouter(
    prefix="/Users",
    tags=["Users"],
    responses={422: {"description": "Validation Error"}},
)

@router.get("/users", dependencies=[Depends(JWTBearer())], summary=None, name='GET', operation_id='users')
async def get_user(db: Session = Depends(get_db)):
    _user = UserRepo.get_all(db, Users)
    return ResponseSchema(code=200, status="S", result=_user).model_dump(exclude_none=True)

@router.get("/user", dependencies=[Depends(JWTBearer())], summary=None, name='GET', operation_id='user')
async def get_user_by_id(_token: str = Depends(JWTBearer()), db: Session = Depends(get_db)):
    _user_id = JWTRepo.decode_token(_token.replace("Bearer ", ""))
    _user_id = uuid.UUID(_user_id)
    _user = UserRepo.get_by_id(db, Users, _user_id)
    return ResponseSchema(code=200, status="S", result=_user).model_dump(exclude_none=True)
