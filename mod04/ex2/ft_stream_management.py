import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    id = input("Input Stream active. Enter archivist ID: ")
    rep = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {id}: {rep}")
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr
          )
    print("[STANDARD] Data transmission complete")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
