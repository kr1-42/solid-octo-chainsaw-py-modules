def main():
    players = [
        {"name": "alice", "score": 2300, "active": True, "region": "north"},
        {"name": "bob", "score": 1800, "active": True, "region": "east"},
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "region": "central",
        },
        {"name": "diana", "score": 2050, "active": False, "region": "north"},
        {"name": "edgar", "score": 950, "active": False, "region": "west"},
    ]

    achievements = {
        "alice": {
            "first_kill",
            "level_10",
            "boss_slayer",
            "collector",
            "explorer",
        },
        "bob": {"first_kill", "level_10", "treasure_hunter"},
        "charlie": {
            "first_kill",
            "level_10",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
            "treasure_hunter",
            "survivor",
        },
        "diana": {"first_kill", "level_10"},
        "edgar": {"first_kill"},
    }

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    high_scorers = [
        player["name"] for player in players if player["score"] > 2000
    ]
    doubled_scores = [player["score"] * 2 for player in players]
    active_players = [player["name"] for player in players if player["active"]]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {player["name"]: player["score"] for player in players}
    score_categories = {
        "high": len([p for p in players if p["score"] >= 2200]),
        "medium": len([p for p in players if 1500 <= p["score"] < 2200]),
        "low": len([p for p in players if p["score"] < 1500]),
    }
    achievement_counts = {
        name: len(badges) for name, badges in achievements.items()
    }
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {player["name"] for player in players}
    unique_achievements = {
        badge for badge_set in achievements.values() for badge in badge_set
    }
    active_regions = {
            player["region"] for player in players if player["active"]
        }
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(unique_players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(player_scores.values()) / len(player_scores)
    top_player = max(players, key=lambda player: player["score"])
    top_name = top_player["name"]
    top_score = top_player["score"]
    top_achievements = achievement_counts.get(top_name, 0)
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.1f}")
    print(
        f"Top performer: {top_name} ({top_score} points, "
        f"{top_achievements} achievements)"
    )


if __name__ == "__main__":
    main()
