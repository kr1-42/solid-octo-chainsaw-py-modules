class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass

class PlantError(GardenError):
    """Raised when there is an issue with planting."""
    pass

class WaterError(GardenError):
    """Raised when there is an issue with watering."""
    pass


def test_all():
    print("=== Testing All Garden Errors with One Except Block ===\n")

    errors_to_test = [
        ("GardenError", lambda: (_ for _ in ()).throw(GardenError("Issue with planting!"))),
        ("GardenError", lambda: (_ for _ in ()).throw(GardenError("Issue with watering!")))
    ]

    for error_name, error_func in errors_to_test:
        try:
            print(f"Testing {error_name}...")
            error_func()
        except GardenError as e:
            print(f"Caught {type(e).__name__}: {e}\n")


def plant_test():
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print(e)
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print(e)
    test_all()

if __name__ == "__main__":
    plant_test()
