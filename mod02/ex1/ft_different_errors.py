def valtest():
    try:
        _ = int("forty two")
    except ValueError as ve:
        print(f"Caught ValueError: {ve}")


def zerotest():
    try:
        _ = 1 / 0
    except ZeroDivisionError as zde:
        print(f"Caught ZeroDivisionError: {zde}")


def filetest():
    f = None
    try:
        f = open("non_existent_file_no_like_actually_i_dont_exist.txt", "r")
        _ = f.read()
    except FileNotFoundError as fnfe:
        print(f"Caught FileNotFoundError: {fnfe}")
    finally:
        if f is not None:
            f.close()


def keytest():
    sample_dict = {"rose": "red", "sunflower": "yellow"}
    try:
        _ = sample_dict["tulip"]
    except KeyError as ke:
        print(f"Caught KeyError: {ke}")


def test_all_errors():
    print("\n=== Testing All 4 Errors with One Except Block ===\n")

    errors_to_test = [
        ("ValueError", lambda: int("forty two")),
        ("ZeroDivisionError", lambda: 1 / 0),
        ("FileNotFoundError", lambda: open("non_existent_file.txt", "r")),
        ("KeyError", lambda: {"rose": "red"}["tulip"])
    ]

    for error_name, error_func in errors_to_test:
        try:
            print(f"Testing {error_name}...")
            error_func()
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, KeyError) as e:
            print(f"Caught {type(e).__name__}: {e}\n")


def garden_operations():
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    valtest()
    print("\nTesting ZeroDivisionError...")
    zerotest()
    print("\nTesting FileNotFoundError...")
    filetest()
    print("\nTesting KeyError...")
    keytest()
    print("\nTesting multiple errors together...")
    test_all_errors()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
