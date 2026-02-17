import alchemy.transmutation

if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")
    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.stone_to_gem()}")
    print("\ntesting Absolute Imports (from advanced.py):")
    print(
        f"philosophers_stone(): {alchemy.transmutation.philosophers_stone()}"
        )
    print(f"elixir_of_life(): {alchemy.transmutation.elixir_of_life()}\n")
    print("Testing package access:")
    print(
        "alchemy.transmutation.lead_to_gold(): "
        f"{alchemy.transmutation.lead_to_gold()}\n"
        "alchemy.transmutation.philosophers_stone():"
        f"{alchemy.transmutation.philosophers_stone()}\n"
    )
