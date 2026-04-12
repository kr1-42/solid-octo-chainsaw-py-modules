from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulate(power: int) -> int:
        nonlocal total
        total += power
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value) -> None:
        memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())

    counter_b = mage_counter()
    print("counter_b call 1:", counter_b())

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print("Base 100, add 20:", accumulator(20))
    print("Base 100, add 30:", accumulator(30))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))
