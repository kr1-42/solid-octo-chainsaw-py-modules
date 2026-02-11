import alchemy.elements
from alchemy.elements import create_fire
from alchemy.elements import create_water, create_earth
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion as b

if __name__ == "__main__":
    print("=== Transmutation Mastery ===\n")
    print("Method 1 - full module import:")
    print("alchemy.elements.create_fire():" +
          f"{alchemy.elements.create_fire()}\n")
    print("Method 2 - specific function import:")
    print("create_water():" + f"{create_water()}\n")
    print("Method 3 - aliased import:")
    print("heal():" + f"{heal()}\n")
    print("Method 4 - Multiple imports:")
    print("create_earth():" + f"{create_earth()}")
    print("create_fire():" + f"{create_fire()}")
    print("strength_potion():" + f"{b()}\n")
    print("All import transmutation methods mastered!")
