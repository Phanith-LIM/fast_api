from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Request
from core.database import get_db, SECRET_KEY, ALGORITHM
from modules.users.entity import Users
from core.base import JWTBearer, JWTRepo
from core.schemas import ResponseSchema
from modules.users.repository import UserRepo
import jwt

router = APIRouter(
    prefix="/Users",
    tags=["Users"],
    responses={422: {"description": "Validation Error"}},
)


@router.get("/users", dependencies=[Depends(JWTBearer())], summary=None, name=' ')
async def get_user(db: Session = Depends(get_db)):
    _user = UserRepo.get_all(db, Users)
    return ResponseSchema(code=200, status="S", result=_user).model_dump(exclude_none=True)

@router.get("/user", dependencies=[Depends(JWTBearer())], summary=None, name=' ')
async def get_user_by_id(_token: str = Depends(JWTBearer()), db: Session = Depends(get_db)):
    _user_id = JWTRepo.decode_token(_token.replace("Bearer ", ""))
    _user = UserRepo.get_by_id(db, Users, _user_id)
    return ResponseSchema(code=200, status="S", result=_user).model_dump(exclude_none=True)
