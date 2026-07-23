from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# Base schema for client input (keeps requests clean by omitting DB-generated fields like ID and tank_id)
class CreateWaterLog(SQLModel):
    temperature: float 
    pH: float
    turbidity: float


# Database table model — inherits water metrics from CreateWaterLog and adds relational/DB fields
class WaterLog(CreateWaterLog, table=True):
    id: Optional[int] = Field(default=None, primary_key= True)
    tank_id: int = Field(foreign_key="tankprofile.id")
    recorded_at: datetime = Field(default_factory=datetime.now)

    model_config = {"populate_by_name": True, "serialize_in_order": True}