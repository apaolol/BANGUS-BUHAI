from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)   
    name: str
    email: str
