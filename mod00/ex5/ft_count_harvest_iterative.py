def ft_count_harvest_iterative():
    x = int(input("Days until harvest: "))
    i = 0
    while i < x:
        print(f"day {i}")
        i += 1
    print("Harvest time!")

def main() -> int:
    ft_count_harvest_iterative()

if __name__ == "__main__":
    main()

