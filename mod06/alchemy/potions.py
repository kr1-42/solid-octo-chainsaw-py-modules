import alchemy.elements
from alchemy.elements import create_fire
from alchemy.elements import create_water, create_earth, create_air


def healing_potion():
    fire_result = alchemy.elements.create_fire()
    water_result = create_water()
    return "Healing Potion brewed with" \
        f"{fire_result} and {water_result}"


def strength_potion():
    earth_result = " " + create_earth()
    fire_result = create_fire()
    return "Strength Potion brewed with" \
        f"{earth_result} and {fire_result}"


def invisibility_potion():
    air_result = create_air()
    water_result = create_water()
    return "Invisibility Potion brewed with" \
        f"{air_result} and {water_result}"


def wisdom_potion():
    earth_result = create_earth()
    air_result = create_air()
    fire_result = create_fire()
    water_result = create_water()
    all_four_results = f"all elements: {earth_result}, {air_result}," + \
        f" {fire_result}, and {water_result}"
    return "Wisdom Potion brewed with " + all_four_results
