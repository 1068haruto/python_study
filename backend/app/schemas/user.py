from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, description="ユーザー名")
    password: str = Field(..., min_length=1, description="パスワード")


class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, description="更新するユーザー名")
    password: str | None = Field(None, min_length=1, description="更新するパスワード")


class UserOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class UserDeleteResponse(BaseModel):
    user_id: int