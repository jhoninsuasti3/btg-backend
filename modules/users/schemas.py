from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    balance: float

class UserResponse(BaseModel):
    uuid: str
    email: EmailStr
    balance: float
