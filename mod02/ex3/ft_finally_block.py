def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("Testing normal watering...\n")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Testing with error...\n")
    water_plants(["tomato", None])
