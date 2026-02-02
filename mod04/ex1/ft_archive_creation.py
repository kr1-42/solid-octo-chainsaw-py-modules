def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    try:
        with open("new_discovery.txt", "w") as f:
            print("Storage unit created successfully...\n")
            f.write(
                "[ENTRY 001] New quantum algorithm discovered\n" +
                "[ENTRY 002] Efficiency increased by 347%\n" +
                "[ENTRY 003] Archived by Data Archivist trainee\n"
            )
            print("Inscribing preservation data...")
            print(
                "[ENTRY 001] New quantum algorithm discovered\n" +
                "[ENTRY 002] Efficiency increased by 347%\n" +
                "[ENTRY 003] Archived by Data Archivist trainee\n"
            )
    except IOError:
        print("ERROR: Unable to create storage unit")
        return
    print(
        "Data inscription complete. Storage unit sealed.\n" +
        "Archive 'new_discovery.txt' ready for long-term preservation."
    )


if __name__ == "__main__":
    main()
