from .Card import Card


class CreatureCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = self.validate(attack)
        self.health = self.validate(health)

    def play(self, game_state=None):
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    @staticmethod
    def validate(h: int):
        if h < 0:
            raise ValueError("card value cannot be negative.")
        return h
