import sys


def length(s: str) -> int:
    count = 0
    for _ in s:
        count += 1
    return count


def startswith(prefix: str, string: str) -> bool:
    if length(prefix) > length(string):
        return False
    for i in range(length(prefix)):
        if prefix[i] != string[i]:
            return False
    return True


def secure_extraction() -> None:
    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r", encoding="utf-8") as vault:
            for line in vault:
                line = line.rstrip("\n")
                if not line:
                    continue
                if startswith("[CLASSIFIED]", line):
                    print(line)
                else:
                    print(f"[CLASSIFIED] {line}")
    except FileNotFoundError:
        print("[ALERT] Classified vault not found", file=sys.stderr)
    except OSError:
        print("[ALERT] Classified vault access failure", file=sys.stderr)


def secure_preservation() -> None:
    print("SECURE PRESERVATION:")
    try:
        with open("preserved_protocols.txt", "w", encoding="utf-8") as vault:
            vault.write("New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")
    except OSError:
        print("[ALERT] Preservation vault write failure", file=sys.stderr)


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    secure_extraction()
    secure_preservation()

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
