def main() -> int:
    players = {
            "alice": {
                    "first_kill",
                    "level_10",
                    "treasure_hunter",
                    "speed_demon",
            },
            "bob": {
                    "first_kill",
                    "level_10",
                    "boss_slayer",
                    "collector",
            },
            "charli": {
                    "level_10",
                    "treasure_hunter",
                    "boss_slayer",
                    "speed_demon",
                    "perfectionist",
            },
    }
    print("=== Achievement Tracker System ===\n")
    for player, achievements in players.items():
        print(
                f"Player: {player} "
                f"Achievements: "
                f"{achievements}"
        )
    print("=== Achievement Analytics ===\n")
    print(
            "all unique achievements: "
            f"{set().union(*players.values())}"
            "\ntotal unique achievements: "
            f"{len(set().union(*players.values()))}\n"
    )
    print(
            "common achievements: "
            f"{set.intersection(*players.values())}"
    )
    achievement_counts = {}
    for achievements in players.values():
        for achievement in achievements:
            achievement_counts[achievement] = (
                    achievement_counts.get(achievement, 0) + 1
                )
    rare_achievements = {
            achievement
            for achievement, count in achievement_counts.items()
            if count == 1
    }
    print(
            "rare achievements (1 player): "
            f"{rare_achievements}\n"
    )
    print(
            "alice vs bob common: "
            f"{players['alice'].intersection(players['bob'])}"
    )
    print(
            "alice unique: "
            f"{players['alice'].difference(players['bob'], players['charli'])}"
    )
    print(
            "bob unique: "
            f"{players['bob'].difference(players['alice'], players['charli'])}"
    )
    return 0


if __name__ == "__main__":
    main()
