from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    username: str
    age: int
