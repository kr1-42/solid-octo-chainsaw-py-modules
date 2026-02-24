import random
from typing import Union

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Concrete factory creating fantasy-themed cards."""

    CREATURES = {
        "dragon": ("Fire Dragon", 5, "Rare", 6, 5),
        "goblin": ("Goblin Warrior", 2, "Common", 3, 2),
    }

    SPELLS = {
        "fireball": (
            "Lightning Bolt", 3, "Common",
            "damage", "Deals 4 damage",
        ),
    }

    ARTIFACTS = {
        "mana_ring": (
            "Mana Ring", 2, "Uncommon",
            3, "Restores 2 mana per turn",
        ),
    }

    def create_creature(
        self,
        name_or_power: Union[str, int, None] = None,
    ) -> CreatureCard:
        """Create a fantasy creature card."""
        if isinstance(name_or_power, str):
            key = name_or_power.lower()
            if key in self.CREATURES:
                args = self.CREATURES[key]
                return CreatureCard(*args)
        if isinstance(name_or_power, int):
            return CreatureCard(
                "Custom Creature", name_or_power,
                "Common", name_or_power, name_or_power,
            )
        key = random.choice(list(self.CREATURES.keys()))
        return CreatureCard(*self.CREATURES[key])

    def create_spell(
        self,
        name_or_power: Union[str, int, None] = None,
    ) -> SpellCard:
        """Create a fantasy spell card."""
        if isinstance(name_or_power, str):
            key = name_or_power.lower()
            if key in self.SPELLS:
                args = self.SPELLS[key]
                return SpellCard(*args)
        if isinstance(name_or_power, int):
            return SpellCard(
                "Custom Spell", name_or_power,
                "Common", "damage",
                f"Deals {name_or_power} damage",
            )
        key = random.choice(list(self.SPELLS.keys()))
        return SpellCard(*self.SPELLS[key])

    def create_artifact(
        self,
        name_or_power: Union[str, int, None] = None,
    ) -> ArtifactCard:
        """Create a fantasy artifact card."""
        if isinstance(name_or_power, str):
            key = name_or_power.lower()
            if key in self.ARTIFACTS:
                args = self.ARTIFACTS[key]
                return ArtifactCard(*args)
        if isinstance(name_or_power, int):
            return ArtifactCard(
                "Custom Artifact", name_or_power,
                "Common", name_or_power,
                "Custom effect",
            )
        key = random.choice(list(self.ARTIFACTS.keys()))
        return ArtifactCard(*self.ARTIFACTS[key])

    def create_themed_deck(self, size: int) -> dict:
        """Create a fantasy-themed deck of given size."""
        deck = {
            "creatures": [],
            "spells": [],
            "artifacts": [],
        }
        for _ in range(size):
            deck["creatures"].append(self.create_creature())
            deck["spells"].append(self.create_spell())
            deck["artifacts"].append(self.create_artifact())
        return deck

    def get_supported_types(self) -> dict:
        """Return supported card types."""
        return {
            "creatures": list(self.CREATURES.keys()),
            "spells": list(self.SPELLS.keys()),
            "artifacts": list(self.ARTIFACTS.keys()),
        }
