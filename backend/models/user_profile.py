from sqlmodel import SQLModel, Field
from typing import Optional
#not aDDING TABLE= TRUE RESULTS IN server error (iunternal)
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)   
    name: str
    email: str  

    model_config = {"populate_by_name": True, "serialize_in_order": True}
