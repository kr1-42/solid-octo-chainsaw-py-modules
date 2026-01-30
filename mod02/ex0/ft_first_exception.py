def test_temperature_input(temp: int):
    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")


def is_valid_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def check_temperature():
    print("=== Garden Temperature Checker ===")
    for _ in range(4):
        print()
        temp_str = input("testing temperature: ")
        if is_valid_int(temp_str):
            temp = int(temp_str)
        else:
            print(f"Error: {temp_str} is not a valid number")
            continue
        test_temperature_input(temp)
    print("\nAll temperature tests completed.")


if __name__ == "__main__":
    check_temperature()
