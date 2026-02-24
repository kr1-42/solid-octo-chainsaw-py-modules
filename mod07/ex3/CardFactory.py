from abc import ABC, abstractmethod
from typing import Union

from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory interface for creating cards."""

    @abstractmethod
    def create_creature(
        self,
        name_or_power: Union[str, int, None] = None,
    ) -> Card:
        """Create a creature card."""
        pass

    @abstractmethod
    def create_spell(
        self,
        name_or_power: Union[str, int, None] = None,
    ) -> Card:
        """Create a spell card."""
        pass

    @abstractmethod
    def create_artifact(
        self,
        name_or_power: Union[str, int, None] = None,
    ) -> Card:
        """Create an artifact card."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck of cards."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Return supported card types and their options."""
        pass
