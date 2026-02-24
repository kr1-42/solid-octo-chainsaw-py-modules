from abc import ABC, abstractmethod


class Magical(ABC):
    """Abstract interface for magical abilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel mana for spellcasting."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Get magical statistics."""
        pass
