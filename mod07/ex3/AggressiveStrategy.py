from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Concrete aggressive strategy prioritizing damage."""

    def execute_turn(
        self, hand: list, battlefield: list
    ) -> dict:
        """Execute an aggressive turn: play low-cost cards first."""
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        mana_available = 10
        cards_played = []
        total_damage = 0

        for card in sorted_hand:
            if card.cost <= mana_available:
                cards_played.append(card.name)
                mana_available -= card.cost
                total_damage += card.cost + 3

        targets = self.prioritize_targets(
            battlefield if battlefield else ["Enemy Player"]
        )

        return {
            "cards_played": cards_played,
            "mana_used": 10 - mana_available,
            "targets_attacked": targets,
            "damage_dealt": total_damage,
        }

    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        return "AggressiveStrategy"

    def prioritize_targets(
        self, available_targets: list
    ) -> list:
        """Prioritize direct enemy attacks."""
        if not available_targets:
            return ["Enemy Player"]
        return available_targets
