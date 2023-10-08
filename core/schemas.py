from typing import Optional, TypeVar, Dict
from pydantic import BaseModel, Field

T = TypeVar('T')

class ResponseSchema(BaseModel):
    code: int
    status: str
    message: Optional[str] = None
    result: Optional[T] = None

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
