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


if __name__ == "__main__":
    from .CreatureCard import CreatureCard

    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}")
    print("CREATURE CARD DEMONSTRATION")
    print(f"{'='*60}{Colors.END}\n")

    print(f"{Colors.BOLD}{Colors.CYAN}Creating Dragon Card:{Colors.END}")
    card1 = CreatureCard(
        name="Dragon", cost=7, rarity="Legendary",
        attack=5, health=10
    )
    print(f"{Colors.GREEN}✓ Card created successfully{Colors.END}\n")

    print(f"{Colors.BOLD}{Colors.BLUE}Card Information:{Colors.END}")
    print(f"  {Colors.YELLOW}• {card1.get_card_info()}{Colors.END}\n")

    print(f"{Colors.BOLD}{Colors.BLUE}Playing Card:{Colors.END}")
    print(f"  {Colors.YELLOW}• {card1.play()}{Colors.END}\n")

    print(f"{Colors.BOLD}{Colors.BLUE}Mana Availability Check:{Colors.END}")
    playable_10 = card1.is_playable(player_mana=10)
    playable_5 = card1.is_playable(player_mana=5)
    print(f"  {Colors.GREEN}• With 10 mana: {playable_10}{Colors.END}")
    mana_5_color = Colors.RED if not playable_5 else Colors.GREEN
    print(
        f"  {mana_5_color}• With 5 mana: {playable_5}{Colors.END}\n"
    )

    print(
        f"{Colors.BOLD}{Colors.CYAN}Testing Validation"
        f" (Negative Attack):{Colors.END}"
    )
    try:
        card2 = CreatureCard(
            name="Goblin", cost=3, rarity="Common",
            attack=-2, health=4
        )
        card2.get_card_info()
    except ValueError as e:
        print(f"  {Colors.RED}✗ Error caught: {e}{Colors.END}\n")

    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}\n")
