from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=3, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_seconds: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=0, le=100)
    message_recieved: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC", 0, 2):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL \
                and self.is_verified is False:
            raise ValueError("Physical contacts must be verified")
        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise \
                ValueError(
                    "Telepathic contacts must have at least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_recieved is None:
            raise ValueError("Strong signals must have a message received")
        return self

def main():
    print("Creating a valid alien contact...\n")
    contact = AlienContact(
        contact_id="AC12345",
        timestamp=datetime(2026, 4, 1, 12, 0),
        location="Sector 7G",
        contact_type=ContactType.RADIO,
        signal_strength=5.5,
        duration_seconds=300,
        witness_count=2,
        message_recieved="glorbz gazorb berzong zorp",
        is_verified=True
    )

    print("Alien Contact Information")
    print("-" * 25)
    for field_name, value in contact.model_dump().items():
        print(f"{field_name}: {value}")

    print(
        "\nAttempting to create an invalid",
        " contact (unverified physical contact)...\n"
        )
    try:
        AlienContact(
            contact_id="AC54321",
            timestamp=datetime(2026, 4, 2, 14, 30),
            location="Sector 9X",
            contact_type=ContactType.PHYSICAL,
            signal_strength=8.0,
            duration_seconds=600,
            witness_count=5,
            message_recieved=None,
            is_verified=False
        )
    except ValueError as error:
        print("Validation error message:")
        print(error.errors()[0]['msg'])


if __name__ == "__main__":
    main()
