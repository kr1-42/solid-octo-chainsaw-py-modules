from datetime import datetime

from pydantic import BaseModel, Field, ValidationError, model_validator


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)

    @model_validator(mode="after")
    def validate_maintenance_date(self) -> "SpaceStation":
        if self.last_maintenance > datetime.now():
            raise ValueError("last_maintenance cannot be in the future")
        return self


def main() -> None:
    print("Creating a valid space station...\n")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=7,
        power_level=88.5,
        oxygen_level=96.2,
        last_maintenance=datetime(2026, 3, 1, 9, 30),
        notes="Routine checks completed successfully.",
    )

    print("Station Information")
    print("-" * 20)
    for field_name, value in station.model_dump().items():
        print(f"{field_name}: {value}")

    print("\nAttempting to create an invalid station (crew_size > 20)...\n")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Mars Relay",
            crew_size=25,
            power_level=80.0,
            oxygen_level=90.0,
            last_maintenance=datetime(2026, 2, 10, 15, 0),
            notes="Invalid example for validation demo.",
        )
    except ValidationError as error:
        print("Validation error message:")
        print(error.errors()[0]['msg'])


if __name__ == "__main__":
    main()
