from alchemy.grimoire import record_spell as rs
from alchemy.grimoire import validate_ingredients as vi


if __name__ == "__main__":
    print("Testing validate_ingredients:")
    print(vi("fire"))
    print(vi("lightning"))
    print("\nTesting record_spell:")
    print(rs("Flame Burst", "fire air"))
    print(rs("Thunder Strike", "lightning"))
