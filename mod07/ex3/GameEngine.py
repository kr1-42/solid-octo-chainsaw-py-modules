from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    """Game orchestrator combining factory and strategy."""

    def __init__(self):
        """Initialize the game engine."""
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy,
    ) -> None:
        """Configure engine with a factory and strategy."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """Simulate a game turn using configured strategy."""
        if not self.factory or not self.strategy:
            return {"error": "Engine not configured"}

        creature = self.factory.create_creature("dragon")
        goblin = self.factory.create_creature("goblin")
        spell = self.factory.create_spell("fireball")
        self.hand = [creature, goblin, spell]
        self.cards_created += len(self.hand)

        hand_str = [
            f"{c.name} ({c.cost})" for c in self.hand
        ]
        print(f"Hand: {hand_str}")

        actions = self.strategy.execute_turn(
            self.hand, self.battlefield,
        )
        self.turns_simulated += 1
        self.total_damage += actions.get("damage_dealt", 0)

        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": actions,
        }

    def get_engine_status(self) -> dict:
        """Get current engine status report."""
        strategy_name = ""
        if self.strategy:
            strategy_name = self.strategy.get_strategy_name()
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
