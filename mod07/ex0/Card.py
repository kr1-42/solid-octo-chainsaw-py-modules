from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        pass

    def get_card_info(self):
        return f"Name: {self.name}, Cost: {self.cost}, Rarity: {self.rarity}"

    def is_playable(self, player_mana: int) -> bool:
        return player_mana >= self.cost
