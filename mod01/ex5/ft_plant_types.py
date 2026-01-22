class Plant:
    def __init__(self, plant: str, height_cm: int, age_days: int) -> None:
        self.plant = plant
        self.height_cm = height_cm
        self.age_days = age_days


class Flower(Plant):
    def __init__(self, plant: str, height_cm: int, age_days: int, petal_color: str) -> None:
        super().__init__(plant, height_cm, age_days)
        self.petal_color = petal_color

    def bloom(self) -> str:
        return f"{self.plant} is blooming beautifully!"


class Tree(Plant):
    def __init__(self, plant: str, height_cm: int, age_days: int, trunk_diameter_cm: float) -> None:
        super().__init__(plant, height_cm, age_days)
        self.trunk_diameter_cm = trunk_diameter_cm

    def produce_shade(self) -> str:
        shade_area = int((self.trunk_diameter_cm / 100) ** 2 * 3.14159 * 10)
        return f"{self.plant} provides {shade_area} square meters of shade"


class Vegetable(Plant):
    def __init__(self, plant: str, height_cm: int, age_days: int, harvest_season: str) -> None:
        super().__init__(plant, height_cm, age_days)
        self.harvest_season = harvest_season

    def nutritional_info(self) -> str:
        return f"{self.plant} is rich in vitamin C"


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    print(f"{rose.plant} ({type(rose).__name__}): {rose.height_cm}cm, {rose.age_days} days, {rose.petal_color} color")
    print(rose.bloom())

    oak = Tree("Oak", 500, 1825, 50)
    print(f"{oak.plant} ({type(oak).__name__}): {oak.height_cm}cm, {oak.age_days} days, {int(oak.trunk_diameter_cm)}cm diameter")
    print(oak.produce_shade())

    tomato = Vegetable("Tomato", 80, 90, "summer")
    print(f"{tomato.plant} ({type(tomato).__name__}): {tomato.height_cm}cm, {tomato.age_days} days, {tomato.harvest_season} harvest")
    print(tomato.nutritional_info())


if __name__ == "__main__":
    ft_plant_types()
