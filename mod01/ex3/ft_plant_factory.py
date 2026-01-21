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
    print("=== Plant Factory Output ===")
    plants = [
        Plant(plant="Rose", height_cm=int(25), age_days=30),
        Plant(plant="Oak", height_cm=200, age_days=365),
        Plant(plant="Cactus", height_cm=5, age_days=90),
        Plant(plant="Sunflower", height_cm=80, age_days=45),
        Plant(plant="Fern", height_cm=15, age_days=120)
    ]
    for plant in plants:
        print(f"Created: {plant.plant} ({plant.height_cm}cm, {plant.age_days} days)")

    print(f"Total plants created: {len(plants)}")
    return 0

if __name__ == "__main__":
    main()