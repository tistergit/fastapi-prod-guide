from pydantic import BaseModel


class NotFoundException(BaseModel):
    detail: str = "Not Found"
    
class UserModel(BaseModel):
    id: int
    name: str
    email: str