class SecurePlant:
    """A plant class with protected data and validation to prevent corruption."""
    
    def __init__(self, plant: str, height_cm: int, age_days: int) -> None:
        """Initialize a secure plant with validation."""
        self._plant = plant
        self._height_cm = 0
        self._age_days = 0
        
        # Use setters to validate initial values
        self.set_height(height_cm)
        self.set_age(age_days)
    
    def set_height(self, height_cm: int) -> bool:
        """Set plant height with validation. Returns True if successful, False otherwise."""
        if height_cm < 0:
            print(f"Error: Cannot set negative height ({height_cm}cm) for {self._plant}")
            return False
        self._height_cm = height_cm
        return True
    
    def get_height(self) -> int:
        """Safely retrieve plant height."""
        return self._height_cm
    
    def set_age(self, age_days: int) -> bool:
        """Set plant age with validation. Returns True if successful, False otherwise."""
        if age_days < 0:
            print(f"Error: Cannot set negative age ({age_days} days) for {self._plant}")
            return False
        self._age_days = age_days
        return True
    
    def get_age(self) -> int:
        """Safely retrieve plant age."""
        return self._age_days
    
    def get_plant_name(self) -> str:
        """Safely retrieve plant name."""
        return self._plant
    
    def get_info(self) -> str:
        """Return formatted information about the plant's current status."""
        return f"{self._plant}: {self._height_cm}cm, {self._age_days} days old"
    
    def grow(self, cm: int) -> bool:
        """Increase plant height safely."""
        if cm < 0:
            print(f"Error: Cannot grow by negative amount ({cm}cm)")
            return False
        return self.set_height(self._height_cm + cm)
    
    def age(self, days: int) -> bool:
        """Increase plant age safely."""
        if days < 0:
            print(f"Error: Cannot age by negative amount ({days} days)")
            return False
        return self.set_age(self._age_days + days)


def main() -> int:
    print("=== Garden Security System ===\n")
    
    # Create a secure plant
    rose = SecurePlant(plant="Rose", height_cm=25, age_days=30)
    print("Initial state:")
    print(rose.get_info())
    
    print("\n--- Testing Valid Operations ---")
    
    # Valid operations
    rose.grow(5)
    print(f"After growing 5cm: {rose.get_info()}")
    
    rose.age(7)
    print(f"After aging 7 days: {rose.get_info()}")
    
    print("\n--- Testing Invalid Operations (Protection) ---")
    
    # Attempt to set negative height
    print("\nAttempting to set height to -10cm:")
    rose.set_height(-10)
    print(f"Height remains: {rose.get_height()}cm")
    
    # Attempt to set negative age
    print("\nAttempting to set age to -5 days:")
    rose.set_age(-5)
    print(f"Age remains: {rose.get_age()} days")
    
    # Attempt to grow by negative amount
    print("\nAttempting to grow by -3cm:")
    rose.grow(-3)
    print(f"Height remains: {rose.get_height()}cm")
    
    # Attempt to age by negative amount
    print("\nAttempting to age by -10 days:")
    rose.age(-10)
    print(f"Age remains: {rose.get_age()} days")
    
    print("\n--- Testing Multiple Plants ---")
    
    # Create multiple plants
    plants = [
        SecurePlant(plant="Sunflower", height_cm=80, age_days=45),
        SecurePlant(plant="Cactus", height_cm=15, age_days=120),
    ]
    
    for plant in plants:
        print(plant.get_info())
    
    # Try to corrupt a plant
    print("\nAttempting to corrupt Sunflower data:")
    plants[0].set_height(-50)  # This will fail
    plants[0].set_age(-100)    # This will fail
    
    print(f"Sunflower data is safe: {plants[0].get_info()}")
    
    return 0


if __name__ == "__main__":
    main()
