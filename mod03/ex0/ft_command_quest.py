import sys


def main() -> int:
    print("=== command quest ===\n")
    if len(sys.argv) == 1:
        print("No arguments provided, diocan!1!11!\n")
        return 1
    program_name = sys.argv[0] + "\n"
    print("Program name:", program_name)
    if len(sys.argv) >= 1:
        print("arguments received: ", len(sys.argv) - 1)
    for arg in sys.argv:
        print("arg: ", arg)
    print("total arguments: ", len(sys.argv))
    return 0


if __name__ == "__main__":
    main()
