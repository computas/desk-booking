from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
from bson import ObjectId
from utils.helper import generate_object_id


class Desk(BaseModel):
    id: ObjectId = Field(default_factory=generate_object_id, alias="_id")
    name: str = Field(...)
    location: str = Field(...)
    description: Optional[str] = Field(...)
    booked_slots: List[datetime] = Field(...)

    class Config:
            allow_population_by_field_name = True
            schema_extra = {
                "example": {
                    "id": "60e81d3c7fba5a5ed5db5b5c",
                    "name": "Desk 1",
                    "location": "2nd floor, BigQuery",
                    "description": "A quiet desk with a view",
                    "booked_slots": [
                        "2023-03-16T11:00:00",
                        "2023-03-18T14:00:00"
                    ]
                }
            }

class DeskUpdate(BaseModel):
    id: ObjectId 
    booked_slots: List[datetime]

    class Config:
        schema_extra = {
            "example": {
                "id": "60e81d3c7fba5a5ed5db5b5c",
                "booked_slots": [
                        "2023-03-16T11:00:00",
                        "2023-03-18T14:00:00"
                    ]
            }
        }