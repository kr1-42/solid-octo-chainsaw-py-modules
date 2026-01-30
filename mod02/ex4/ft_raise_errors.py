class PlantError(Exception):
    """Raised when there is an issue with a plant."""
    pass


def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check plant health and raise errors for invalid conditions."""
    if not plant_name:
        raise PlantError("Plant name cannot be empty!")
    if water_level > 10:
        raise PlantError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise PlantError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    return f"Plant '{plant_name}' is healthy!"


def main():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 8, 6))
    except PlantError as e:
        print(f"Error: {e}\n")

    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 8, 6))
    except PlantError as e:
        print(f"Error: {e}\n")

    print("Testing bad water level...")
    try:
        print(check_plant_health("rose", 15, 6))
    except PlantError as e:
        print(f"Error: {e}\n")

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("daisy", 5, 0))
    except PlantError as e:
        print(f"Error: {e}\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    main()
