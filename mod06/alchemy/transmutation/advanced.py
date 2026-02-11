from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    gold = lead_to_gold()
    potion = healing_potion()
    return f"Philosopher's Stone created with {gold} and {potion}"


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
