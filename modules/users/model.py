from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    password: str
    email: str
    phone_number: str
    first_name: str
    last_name: str


class UserLogin(BaseModel):
    username: str
    password: str
