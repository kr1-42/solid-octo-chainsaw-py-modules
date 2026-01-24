# ft_garden_analytics.py

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(self.name, "grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print("Added", plant.name, "to", self.owner + "'s garden")

    def grow_all(self):
        print(self.owner, "is helping all plants grow...")
        for p in self.plants:
            p.grow()


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def count_types(self, plants):
            regular = 0
            flowering = 0
            prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        def total_growth(self, plants):
            return len(plants)

    def __init__(self):
        self.gardens = []
        self.stats = GardenManager.GardenStats()

    def add_garden(self, garden):
        self.gardens.append(garden)
        GardenManager.total_gardens += 1

    @staticmethod
    def validate_height(h):
        return h > 0

    @classmethod
    def create_garden_network(cls):
        return cls.total_gardens


# === DEMO ===
print("=== Garden Management System Demo ===")

manager = GardenManager()

alice = Garden("Alice")
bob = Garden("Bob")

manager.add_garden(alice)
manager.add_garden(bob)

oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

alice.add_plant(oak)
alice.add_plant(rose)
alice.add_plant(sunflower)

alice.grow_all()

print("=== Alice's Garden Report ===")
for p in alice.plants:
    if isinstance(p, PrizeFlower):
        print("-", p.name + ":", str(p.height) + "cm,", p.color,
              "flowers (blooming), Prize points:", p.points)
    elif isinstance(p, FloweringPlant):
        print("-", p.name + ":", str(p.height) + "cm,", p.color,
              "flowers (blooming)")
    else:
        print("-", p.name + ":", str(p.height) + "cm")

regular, flowering, prize = manager.stats.count_types(alice.plants)
print("Plants added:", len(alice.plants),
      "Total growth:", manager.stats.total_growth(alice.plants), "cm")
print("Plant types:", regular, "regular,", flowering,
      "flowering,", prize, "prize flowers")

print("Height validation test:",
      GardenManager.validate_height(10))

print("Total gardens managed:",
      GardenManager.create_garden_network())
