from abc import ABC, abstractmethod


class Combatable(ABC):
    """Abstract interface for combat abilities."""

    @abstractmethod
    def attack(self, target) -> dict:
        """Attack a target and return combat result."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Get combat statistics."""
        pass
