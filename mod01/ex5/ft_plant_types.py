class Plant:
    def __init__(self, plant: str, height_cm: int, age_days: int) -> None:
        self.plant = plant
        self.height_cm = height_cm
        self.age_days = age_days


class Tree(Plant):
    def __init__(self, plant: str, height_cm: int, age_days: int, trunk_width: float) -> None:
        super().__init__(plant, height_cm, age_days)
        self.trunk_width = trunk_width

class Flower(Plant):
    def __init__(self, plant: str, height_cm: int, age_days: int, petal_color: str) -> None:
        super().__init__(plant, height_cm, age_days)
        self.petal_color = petal_color
    def bloom(self) -> str:
        return f"The {self.plant} is blooming with {self.petal_color} petals!"
    