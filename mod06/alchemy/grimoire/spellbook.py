def record_spell(spell_name: str, ingredients: str) -> str:
    from . import validator as v
    validation_result = v.validate_ingredients(ingredients)
    if "INVALID" in validation_result:
        return f"Spell rejected: {spell_name} {validation_result}"
    return f"Spell recorded: {spell_name}, Ingredients: {validation_result}"
