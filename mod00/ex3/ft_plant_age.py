def ft_plant_age():
    x = int(input("Enter plant age in days: "))
    if x > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

def main() -> int:
    ft_plant_age()

if __name__ == "__main__":
    main()