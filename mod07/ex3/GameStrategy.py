from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract strategy interface for game turn execution."""

    @abstractmethod
    def execute_turn(
        self, hand: list, battlefield: list
    ) -> dict:
        """Execute a turn given hand and battlefield state."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of this strategy."""
        pass

    @abstractmethod
    def prioritize_targets(
        self, available_targets: list
    ) -> list:
        """Prioritize targets for attack."""
        pass
