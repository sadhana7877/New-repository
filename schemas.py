from pydantic import BaseModel, EmailStr

# Schema for POST /users
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# Schema for GET /users response
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # needed to return SQLAlchemy objects as JSON
