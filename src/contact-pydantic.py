from pydantic import BaseModel, EmailStr
from typing import Optional

class Contact(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    tags: list[str] = []