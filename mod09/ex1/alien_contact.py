from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    VISIT = "visit"
    SIGNAL = "signal"
    INTERACTION = "interaction"

class AlienContact(BaseModel):
    contact_id: str
    timestamp: datetime
    location: str
    contact_type:
