import sys


def main():
    print("=== command quest ===\n")
    if len(sys.argv) == 1:
        print("No arguments provided, diocan!1!11!\n")
    program_name = sys.argv[0] + "\n"
    print("Program name:", program_name)
    if len(sys.argv) >= 1:
        print("arguments received: ", len(sys.argv) - 1)
    for arg in sys.argv:
        print("arg: ", arg)
    print("total arguments: ", len(sys.argv))


if __name__ == "__main__":
    main()
