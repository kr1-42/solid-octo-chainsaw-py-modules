from typing import Any, Dict, Optional
from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical

class EliteCard(Card, Combatable, Magical):
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "rarity": self.rarity,
            "combat_stats": f"Attack: {self.attack}, Defense: {self.defense}",
            "magic_stats": f"Spell Power: {self.spell_power}, Mana Cost: {self.mana_cost}",
        }
