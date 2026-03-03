from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck
from .SpellCard import SpellCard


class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def build_sample_deck() -> Deck:
    deck = Deck()
    spell = SpellCard(
        name="Lightning Bolt",
        cost=3,
        rarity="Common",
        effect_type="damage",
        effect="Deal 3 damage to target",
    )
    artifact = ArtifactCard(
        name="Mana Crystal",
        cost=2,
        rarity="Rare",
        durability=3,
        effect="Permanent: +1 mana per turn",
    )
    creature = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Epic",
        attack=7,
        health=6,
    )

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)
    return deck


if __name__ == "__main__":
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*50}")
    print(" === DataDeck Deck Builder ===")
    print(f"{'='*50}{Colors.END}\n")

    print(
        f"{Colors.CYAN}Building deck with" +
        f"different card types...{Colors.END}\n"
        )

    deck = build_sample_deck()
    stats = deck.get_deck_stats()
    print(f"{Colors.BOLD}{Colors.BLUE}Deck Stats:{Colors.END}")
    for key, value in stats.items():
        print(f"  {Colors.GREEN}• {key}:{Colors.END} {value}")

    print(
        f"\n{Colors.BOLD}{Colors.YELLOW}Drawing and" +
        f" playing cards:{Colors.END}\n"
        )
    while True:
        card = deck.draw_card()
        if card is None:
            break

        card_type = card.__class__.__name__.replace("Card", "")
        print(f"{Colors.BOLD}{Colors.CYAN}Drew:"
              f"{card.name} ({card_type}){Colors.END}")
        result = card.play(game_state={})
        print(f"{Colors.GREEN}Play result:{Colors.END}")
        for key, value in result.items():
            print(f"  {Colors.YELLOW}• {key}:{Colors.END} {value}")
        print()

    print(f"{Colors.BOLD}{Colors.HEADER}Polymorphism in action:" +
          f" Same interface, different card behaviors!{Colors.END}\n")
