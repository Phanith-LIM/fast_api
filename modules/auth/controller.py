from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from passlib.context import CryptContext
from core import get_db, JWTRepo, TokenResponse, ResponseSchema
from modules.users import Users, UserRepo, UserModel, UserLogin

router = APIRouter(
    prefix="/Authentications",
    tags=["Authentications"],
    responses={422: {"description": "Validation Error"}},
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/signup', summary=None, name='POST', operation_id='signup')
async def signup(user: UserModel, db: Session = Depends(get_db)):
    try:
        _user = (
            Users(
                username=user.username,
                email=user.email,
                phone_number=user.phone_number,
                password=pwd_context.hash(user.password),
                first_name=user.first_name,
                last_name=user.last_name
            )
        )
        UserRepo.insert(db, _user)
        return ResponseSchema(code=200, status="S").model_dump(exclude_none=True)
    except Exception as error:
        print(error.args)
        return ResponseSchema(code=500, status="E").model_dump(exclude_none=True)


@router.post('/login', summary=None, name='POST', operation_id='login')
async def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        _user = UserRepo.find_by_username(db, Users, user.username)

        if not pwd_context.verify(user.password, _user.password):
            return ResponseSchema(code=400, status="Bad Request", message="Invalid password").model_dump(
                exclude_none=True)

        token = JWTRepo.generate_token({"sub": _user.username, "id": str(_user.id)})
        return ResponseSchema(
            code=200,
            status="S",
            result=TokenResponse(access_token=token, token_type="Bearer")).model_dump(exclude_none=True)
    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ResponseSchema(
            code=500,
            status="Internal Server Error",
            message="Internal Server Error").model_dump(exclude_none=True)
