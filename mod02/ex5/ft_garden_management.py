class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when there is an issue with a plant."""
    pass


class WaterError(GardenError):
    """Raised when there is an issue with watering."""
    pass


class GardenManager:
    """Manages a garden with plants, watering, and health checks."""

    def __init__(self):
        self.plants = {}
        self.water_tank = 100

    def add_plant(self, name, water_level, sunlight_hours):
        """Add a plant to the garden with validation."""
        if not name:
            raise PlantError("Plant name cannot be empty!")
        if water_level > 10:
            raise PlantError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise PlantError(
                        f"Sunlight hours {sunlight_hours} is too low (min 2)"
                            )

        self.plants[name] = {
            "water": water_level,
            "sun": sunlight_hours
        }

    def water_plants(self):
        """Water all plants with cleanup using finally."""
        try:
            print("Opening watering system")
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")
                self.water_tank -= 5
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name):
        """Check the health of a specific plant."""
        if plant_name not in self.plants:
            raise PlantError(f"Plant '{plant_name}' not found in garden")

        plant = self.plants[plant_name]
        water = plant["water"]
        sun = plant["sun"]

        if water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")

        return f"{plant_name}: healthy (water: {water}, sun: {sun})"


def test_garden_management():
    """Test the garden management system with all error handling."""
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
        print("Added tomato successfully")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("lettuce", 6, 6)
        print("Added lettuce successfully")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("", 5, 5)
        print("Added plant successfully")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    try:
        manager.water_plants()
    except GardenError as e:
        print(f"Error watering: {e}")

    print("Checking plant health...")
    try:
        result = manager.check_plant_health("tomato")
        print(result)
    except GardenError as e:
        print(f"Error checking tomato: {e}")

    try:
        manager.plants["lettuce"]["water"] = 15
        result = manager.check_plant_health("lettuce")
        print(result)
    except GardenError as e:
        print(f"Error checking lettuce: {e}")

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
