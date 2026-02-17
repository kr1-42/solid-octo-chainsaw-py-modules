def validate_ingredients(ingredients: str) -> str:
    right_cases = "fire", "water", "earth", "air"
    ingredient_list = ingredients.lower().split()
    for ingredient in ingredient_list:
        if ingredient not in right_cases:
            return f"{ingredients} INVALID"
    return ingredients + " VALID"
