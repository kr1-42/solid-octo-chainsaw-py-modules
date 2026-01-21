class Plant:
    def __init__(self, plant: str, height_cm: int, age_days: int) -> None:
        self.plant = plant
        self.height_cm = height_cm
        self.age_days = age_days

def main() -> int:
    plants = Plant(plant="Rose", height_cm=25, age_days=30), Plant(plant="Sunflower", height_cm=80, age_days=45), GardenData(plant="Cactus", height_cm=15, age_days=120)

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.plant}: {plant.height_cm}cm, {plant.age_days} days old")
    return 0

if __name__ == "__main__":
    main()