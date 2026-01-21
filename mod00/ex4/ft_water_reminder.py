def ft_water_reminder():
    x = int(input("Days since last watering: "))
    if x > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

def main() -> int:
    ft_water_reminder()

if __name__ == "__main__":
    main()