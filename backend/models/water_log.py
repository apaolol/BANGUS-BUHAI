from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class WaterLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key= True)
    tank_id: int = Field(foreign_key="tankprofile.id")
    temperature: float 
    pH: float
    turbidity: float
    recorded_at: datetime = Field(default_factory=datetime.now)

    model_config = {"populate_by_name": True, "serialize_in_order": True}