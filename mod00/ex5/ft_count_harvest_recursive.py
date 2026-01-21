def ft_count_harvest_recursive_helper(x: int, y: int = 1):
    if y <= x:
        print(f"day {y}")      
        ft_count_harvest_recursive_helper(x, y + 1)
    else:
        print("Harvest time!")

def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))
    ft_count_harvest_recursive_helper(x )

def main() -> int:
    ft_count_harvest_recursive()

if __name__ == "__main__":
    main()