from typing import Any, Dict, Optional

from ex0.Card import Card


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
        effect: str,
    ):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.effect = effect

    def play(
        self,
        game_state: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    def resolve_effect(self, targets: list) -> str:
        if self.effect_type == "damage":
            return f"{self.name} deals damage to {', '.join(targets)}."
        if self.effect_type == "heal":
            return f"{self.name} heals {', '.join(targets)}."
        if self.effect_type == "buff":
            return f"{self.name} buffs {', '.join(targets)}."
        if self.effect_type == "debuff":
            return f"{self.name} debuffs {', '.join(targets)}."
        return f"{self.name} has an unknown effect type: {self.effect_type}."
