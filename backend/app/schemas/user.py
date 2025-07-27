from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None


class UserOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True