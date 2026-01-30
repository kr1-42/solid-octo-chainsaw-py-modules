def water_plants(plant_list):
	for plant in plant_list:
		if plant is None:
			print("Error: can't water none - invalid plant!\n")
			continue
		try:
			print(f"Watering {plant}...")
			if plant == "cactus":
				raise ValueError("Cacti need very little water!")
			print(f"{plant} has been watered.\n")
		except ValueError as e:
			print(f"Error: {e}\n")
		finally:
			print(f"Finished attempt to water {plant}.\n")

if __name__ == "__main__":
	plants = ["rose", "tulip", None, "sunflower"]
	water_plants(plants)
