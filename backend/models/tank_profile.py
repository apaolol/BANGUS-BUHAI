from datetime import date
from typing import Optional
from sqlmodel import Field, SQLModel


# 1. Base / Input Schema (What the client sends in JSON when creating a tank)
class CreateTankProfile(SQLModel):
    name: str
    volume_ml: float
    capacity: float
    growth_stage: str


# 2. Database Model (Inherits tank fields + adds DB metadata)
class TankProfile(CreateTankProfile, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date_added: date = Field(default_factory=date.today)

    model_config = {"populate_by_name": True, "serialize_in_order": True}