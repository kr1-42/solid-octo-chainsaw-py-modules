def splitlines(s: str) -> list[str]:
    lines = []
    current_line = ""
    for char in s:
        if char == "\n":
            lines.append(current_line)
            current_line = ""
        else:
            current_line += char
    lines.append(current_line)
    return lines


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        with open("ancient_fragment.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("ERROR: Storage vault not found")
        return
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    for line in splitlines(content):
        print(line)
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
