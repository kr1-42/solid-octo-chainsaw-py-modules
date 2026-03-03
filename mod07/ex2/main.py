from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")
    elite = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Legendary",
        attack_power=5,
        defense_power=3,
        spell_power=4,
        mana_pool=10,
    )
    print("\nEliteCard capabilities:")
    ability_groups = {
        "Card": {"play", "get_card_info", "is_playable"},
        "Combatable": {"attack", "defend", "get_combat_stats"},
        "Magical": {"cast_spell", "channel_mana", "get_magic_stats"},
    }

    for group_name, abilities in ability_groups.items():
        card_methods = {
            method for method in dir(elite)
            if not method.startswith("_")
        }
        filtered = sorted(card_methods & abilities)
        print(f"- {group_name}: {filtered}")

    print(f"\nPlaying {elite.name} (Elite Card):")

    print("\nCombat phase:")
    attack_result = elite.attack("Enemy")
    print(f"Attack result: {attack_result}")

    defense_result = elite.defend(5)
    print(f"Defense result: {defense_result}")

    # Magic phase
    print("\nMagic phase:")
    spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")

    mana_result = elite.channel_mana(3)
    print(f"Mana channel: {mana_result}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
