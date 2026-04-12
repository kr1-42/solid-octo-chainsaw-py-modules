import time
import functools
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints execution time"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates power level"""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Determine which arg is power: for methods it's args[2],
            # for functions it's args[0]
            power_arg_index = 2 if len(args) > 2 else 0
            if len(args) > power_arg_index:
                power = args[power_arg_index]
                if power < min_power:
                    return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that retries on exception"""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    time.sleep(0.6)  # Simulate delay between attempts
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )

        return wrapper

    return decorator


class MageGuild:
    """Guild class with static and instance methods"""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validate mage name: 3+ chars, only letters and spaces"""
        return len(name) >= 3 and all(
            c.isalpha() or c.isspace() for c in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with power validation"""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def concrete():
        time.sleep(0.1)
        return "Calcium silicate hydrate (C-S-H)"

    molecule = concrete()
    print(f"Concrete molecule: {molecule}")

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def unreliable_spell():
        raise Exception("Magic failed!")

    result = unreliable_spell()
    print(result)

    print("\nTesting MageGuild...")
    guild = MageGuild()

    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("Yo"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))
