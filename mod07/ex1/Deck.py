import math
import random
from typing import Dict, List, Optional

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck:
    def _ensure_cards(self) -> None:
        if not hasattr(self, "_cards"):
            self._cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self._ensure_cards()
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        self._ensure_cards()
        for idx, card in enumerate(self._cards):
            if card.name == card_name:
                del self._cards[idx]
                return True
        return False

    def shuffle(self) -> None:
        self._ensure_cards()
        random.shuffle(self._cards)

    def draw_card(self) -> Optional[Card]:
        self._ensure_cards()
        if not self._cards:
            return None
        return self._cards.pop(0)

    def get_deck_stats(self) -> Dict[str, object]:
        self._ensure_cards()
        total_cards = len(self._cards)
        rarity_counts: Dict[str, int] = {}
        for card in self._cards:
            rarity_counts[card.rarity] = rarity_counts.get(card.rarity, 0) + 1

        creatures = sum(isinstance(card, CreatureCard) for card in self._cards)
        spells = sum(isinstance(card, SpellCard) for card in self._cards)
        artifacts = sum(isinstance(card, ArtifactCard) for card in self._cards)
        total_cost = sum(card.cost for card in self._cards)
        avg_cost = (
            float(math.ceil(total_cost / total_cards))
            if total_cards
            else 0.0
        )

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "rarity_counts": rarity_counts,
            "avg_cost": avg_cost,
        }
