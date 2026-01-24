class Plant:
    def __init__(self, plant: str, height_cm: int, age_days: int) -> None:
        self.plant = plant
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, cm: int) -> None:
        """Increase plant height by specified centimeters."""
        self.height_cm += cm

    def age(self, days: int) -> None:
        """Increase plant age by specified days."""
        self.age_days += days

    def get_info(self) -> str:
        """Return formatted information about the plant's current status."""
        return f"{self.plant}: {self.height_cm}cm, {self.age_days} days old"


def main() -> int:
    # Create multiple plants to simulate
    plants = [
        Plant(plant="Rose", height_cm=25, age_days=30),
        Plant(plant="Sunflower", height_cm=80, age_days=45),
        Plant(plant="Cactus", height_cm=15, age_days=120)
    ]

    print("=== Week of Growth Simulation ===\n")

    # Day 1 - Initial state
    print("--- Day 1 (Initial State) ---")
    for plant in plants:
        print(plant.get_info())
    daily_growth = {
        "Rose": 1,
        "Sunflower": 1,
        "Cactus": 1
    }

    for day in range(2, 8):
        print(f"\n--- Day {day} ---")
        for plant in plants:
            # Each plant grows by its daily growth rate
            plant.grow(daily_growth[plant.plant])
            # Each plant ages by 1 day
            plant.age(1)
            print(plant.get_info())

    return 0


if __name__ == "__main__":
    main()
