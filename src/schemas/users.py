from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
    name: str = Field(max_length=255)
    phone: str = Field(max_length=15)

    class Config:
        orm_mode = True


class UserCreateSchema(UserBaseSchema):
    password: str = Field(min_length=8)


class UserListSchema(UserBaseSchema):
    ...
