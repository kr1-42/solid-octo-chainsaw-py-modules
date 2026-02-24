from pydantic import BaseModel, Field
from typing import Optional

class AlienContact(BaseModel):
    contact_id: str
    timestamp: datetime
    location: str
    contact_type: 
