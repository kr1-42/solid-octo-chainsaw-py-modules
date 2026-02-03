from sys import stderr as bob


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        with open("lost_archive.txt", "r") as f:
            _ = f.read()
    except (FileNotFoundError, IOError, PermissionError):
        print(
            "CRISIS ALERT: Attempting access to 'lost_archive.txt'...",
            "RESPONSE: Security protocols deny access",
            "STATUS: Crisis handled, security maintained\n",
            file=bob,
            sep="\n"
        )

    try:
        with open("classified_vault.txt", "r") as f:
            _ = f.read()
    except (FileNotFoundError, IOError, PermissionError):
        print(
            "CRISIS ALERT: Attempting access to 'classified_vault.txt'...",
            "RESPONSE: Security protocols deny access",
            "STATUS: Crisis handled, security maintained\n",
            file=bob,
            sep="\n"
        )
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as f:
            _ = f.read()
            print(
                "SUCCESS: Archive recovered",
                "- ``Knowledge preserved for humanity''"
            )
    except (FileNotFoundError, IOError, PermissionError):
        print("ERROR: Unable to access 'standard_archive.txt'", file=bob)

    print(
        "STATUS: Normal operations resumed\n",
        "All crisis scenarios handled successfully. Archives secure.",
        sep="\n"
    )


if __name__ == "__main__":
    main()
