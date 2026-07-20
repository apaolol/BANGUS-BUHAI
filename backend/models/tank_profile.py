from sqlmodel import SQLModel, Field
from typing import Optional

class TankProfile(SQLModel, table=True): #makes db from pydantic models
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    volume_ml: float
    capacity: float
    growth_stage: str
    date_added: str