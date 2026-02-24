import pydantic
from datetime import datetime as DateTime
from pydantic import model_validator

class SpaceStation(pydantic.BaseModel):
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: DateTime
    is_operational: bool=True
    notes: str | None
    @model_validator(mode='after')
    def validate_fields(self):
        if self.station_id == "":
            raise ValueError("Station ID cannot be empty.")
        if len(self.station_id) > 10 or len(self.station_id) < 3:
            raise ValueError("Station ID must be between 3 and 10 characters.")
        if self.name == "":
            raise ValueError("Name cannot be empty.")
        if len(self.name) > 50:
            raise ValueError("Name cannot exceed 50 characters.")
        if len(self.name) < 1:
            raise ValueError("Name must be at least 1 character long.")
        if self.crew_size < 0 or self.crew_size > 20:
            raise ValueError("Crew size must be between 0 and 20.")
        if self.power_level < 0.0 or self.power_level > 100.0:
            raise ValueError("Power level must be between 0.0 and 100.0.")
        if self.oxygen_level < 0.0 or self.oxygen_level > 100.0:
            raise ValueError("Oxygen level must be between 0.0 and 100.0.")
        if self.last_maintenance > DateTime.now():
            raise ValueError("Last maintenance date cannot be in the future.")
        if self.notes is not None and len(self.notes) > 200:
            raise ValueError("Notes cannot exceed 200 characters.")
        return self

def main():
    station = SpaceStation(
        station_id="SS-001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=DateTime(2024, 5, 1, 12, 0),
        is_operational=True,
        notes="All systems nominal."
    )
    for field in SpaceStation.model_fields: # Access model_fields from the class, not instance
        value = getattr(station, field)
        print(f"{field}: {value}")
    print("\n" + "-" * 50 + "\n")
    print("\nAttempting to create an invalid space station...")
    try:
        invalid_station = SpaceStation(
            station_id="SS-002",
            name="",
            crew_size=-1,
            power_level=150.0,
            oxygen_level=-10.0,
            last_maintenance=DateTime(2024, 5, 1, 12, 0),
            is_operational=True,
            notes="This station has invalid data."
        )
    except pydantic.ValidationError as e:
        print("Validation error occurred:")
        for error in e.errors():
            print(f"Error Type: {error['type']}")
            print(f"Location: {error['loc']}")
            print(f"Message: {error['msg']}")
    except ValueError as e:
        print(f"Value error occurred: {e}")
    print("\n" + "-" * 50 + "\n")
    print("\nCreating a space station with future maintenance date...")
    try:
        future_station = SpaceStation(
            station_id="SS-003",
            name="Future Station",
            crew_size=4,
            power_level=75.0,
            oxygen_level=80.0,
            last_maintenance=DateTime(2027, 1, 1, 12, 0), # Future date
            is_operational=True,
            notes="This station has a future maintenance date."
        )
    except (pydantic.ValidationError, ValueError) as e:
        print("Validation error occurred:")
        print(e)
    print("\n" + "-" * 50 + "\n")
    print("Testing edge cases for crew size...")
    try:
        edge_station = SpaceStation(
            station_id="SS-004",
            name="Edge Case Station",
            crew_size=20, # Maximum valid crew size
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=DateTime(2024, 5, 1, 12, 0),
            is_operational=True,
            notes="Testing maximum crew size."
        )
        print("Edge case station created successfully:")
        print(edge_station)
    except pydantic.ValidationError as e:
        print("Validation error occurred:")
        for error in e.errors():
            print(f"Error Type: {error['type']}")
            print(f"Location: {error['loc']}")
            print(f"Message: {error['msg']}")
    except ValueError as e:
        print(f"Value error occurred: {e}")
    print("\n" + "-" * 50 + "\n")
    print("Testing edge cases for power level...")
    try:
        edge_station = SpaceStation(
            station_id="SS-005",
            name="Power Edge Station",
            crew_size=5,
            power_level=100.0, # Maximum valid power level
            oxygen_level=50.0,
            last_maintenance=DateTime(2024, 5, 1, 12, 0),
            is_operational=True,
            notes="Testing maximum power level."
        )
        print("Edge case station created successfully:")
        print(edge_station)
    except pydantic.ValidationError as e:
        print("Validation error occurred:")
        for error in e.errors():
            print(f"Error Type: {error['type']}")
            print(f"Location: {error['loc']}")
            print(f"Message: {error['msg']}")
    except ValueError as e:
        print(f"Value error occurred: {e}")
    print("\n" + "-" * 50 + "\n")
    print("Testing edge cases for oxygen level...")
    try:
        edge_station = SpaceStation(
            station_id="SS-006",
            name="Oxygen Edge Station",
            crew_size=5,
            power_level=50.0,
            oxygen_level=100.0, # Maximum valid oxygen level
            last_maintenance=DateTime(2024, 5, 1, 12, 0),
            is_operational=True,
            notes="Testing maximum oxygen level."
        )
        print("Edge case station created successfully:")
        print(edge_station)
    except pydantic.ValidationError as e:
        print("Validation error occurred:")
        for error in e.errors():
            print(f"Error Type: {error['type']}")
            print(f"Location: {error['loc']}")
            print(f"Message: {error['msg']}")
    except ValueError as e:
        print(f"Value error occurred: {e}")

if __name__ == "__main__":
    main()
