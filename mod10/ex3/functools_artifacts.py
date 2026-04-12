import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    op_func = operations[operation]
    return functools.reduce(op_func, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create partial applications of base enchantment"""
    flaming_enchant = functools.partial(
        base_enchantment, power=50, element="fire"
    )
    frozen_enchant = functools.partial(
        base_enchantment, power=50, element="ice"
    )
    lightning_enchant = functools.partial(
        base_enchantment, power=50, element="lightning"
    )

    return {
        "flaming": flaming_enchant,
        "frozen": frozen_enchant,
        "lightning": lightning_enchant,
    }


def memoized_fibonacci(n: int) -> int:
    """Calculate nth Fibonacci number with memoization"""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Create single dispatch spell system"""

    @functools.singledispatch
    def dispatch_spell(spell_input: Any) -> str:
        return "Unknown spell type"

    @dispatch_spell.register(int)
    def _(damage: int) -> str:
        return f"{damage} damage"

    @dispatch_spell.register(str)
    def _(enchantment: str) -> str:
        return enchantment

    @dispatch_spell.register(list)
    def _(spells: list) -> str:
        return f"{len(spells)} spells"

    return dispatch_spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return f"{element} {target} (power: {power})"

    enchants = partial_enchanter(base_enchant)
    print(enchants["flaming"](target="Sword"))
    print(enchants["frozen"](target="Shield"))
    print(enchants["lightning"](target="Staff"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(498)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher([1, 2, 3])}")
    print(f"Unknown spell type: {dispatcher(3.14)}")
