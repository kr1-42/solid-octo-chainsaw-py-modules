from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda *args, **kwargs: (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs)
    )


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs):
        modified_args = (
            (args[0], args[1] * multiplier) + args[2:]
            if len(args) > 1
            else args
        )
        return base_spell(*modified_args, **kwargs)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda *args, **kwargs: (
        spell(*args, **kwargs)
        if condition(*args, **kwargs)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda *args, **kwargs: [
        spell(*args, **kwargs) for spell in spells
    ]


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def lightning_bolt(target: str, power: int) -> str:
        return f"Lightning bolt strikes {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def is_night(target: str, power: int) -> bool:
        return power > 5

    combined_spell = spell_combiner(fireball, heal)
    amplified_spell = power_amplifier(fireball, 3)
    conditional_spell = conditional_caster(is_night, fireball)
    sequence_spell = spell_sequence([fireball, lightning_bolt])

    print("Testing spell combiner...")
    print("Combined spell result:", combined_spell("Dragon", 10))
    print("\nTesting power amplifier...")
    print("Original: Fireball with 10 power")
    print(amplified_spell("Dragon", 10))
    print("\nTesting conditional caster...")
    print("High power (7):", conditional_spell("Dragon", 7))
    print("Low power (3):", conditional_spell("Dragon", 3))
    print("\nTesting spell sequence...")
    print("Spell sequence:", sequence_spell("Dragon", 10))
