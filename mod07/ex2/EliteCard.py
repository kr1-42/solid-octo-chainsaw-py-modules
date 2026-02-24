from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Elite card with Card + Combatable + Magical."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense_power: int,
        spell_power: int,
        mana_pool: int,
    ):
        """Initialize an EliteCard with combat and magical attributes."""
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.spell_power = spell_power
        self.mana_pool = mana_pool
        self.current_mana = 0

    def play(self, game_state: dict) -> dict:
        """Play the card into the game state."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "rarity": self.rarity,
            "combat_stats": self.get_combat_stats(),
            "magic_stats": self.get_magic_stats(),
        }

    def attack(self, target) -> dict:
        """Attack a target with melee damage."""
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""
        damage_blocked = min(self.defense_power, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        still_alive = damage_taken <= 100  # Assuming 100 HP for demo
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": still_alive,
        }

    def get_combat_stats(self) -> dict:
        """Get combat statistics."""
        return {
            "attack": self.attack_power,
            "defense": self.defense_power,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on multiple targets."""
        mana_used = self.spell_power
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> dict:
        """Channel mana for spellcasting."""
        self.current_mana += amount
        capped_mana = min(self.current_mana, self.mana_pool)
        return {
            "channeled": amount,
            "total_mana": capped_mana,
        }

    def get_magic_stats(self) -> dict:
        """Get magical statistics."""
        return {
            "spell_power": self.spell_power,
            "current_mana": self.current_mana,
            "mana_pool": self.mana_pool,
        }
