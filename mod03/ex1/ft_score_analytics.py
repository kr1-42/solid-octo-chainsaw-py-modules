from sys import argv


def handle_print(case: str, scores=None) -> None:
    if case == "start":
        print("=== score analytics ===\n")
    elif case == "scores":
        print(f"Scores processed: {scores}\n")
        print(f"total players: {len(scores)}")
        print(f"total score: {sum(scores)}")
        print(f"average score: {sum(scores)/len(scores):.2f}")
        print(f"high score: {max(scores)}")
        print(f"low score: {min(scores)}")
        print(f"score range: {max(scores) - min(scores)}")


def process_scores() -> list[int]:
    scores = []
    for arg in argv[1:]:
        try:
            score = int(arg)
            if score < 0:
                print(f"Warning: Negative score '{score}' ignored.")
            else:
                scores.append(score)
        except ValueError:
            print(f"Warning: Non-integer value '{arg}' ignored.")
    return scores


def scores_check() -> int:
    if len(argv) == 1:
        print(
            "No scores provided. Usage:",
            "python3 ft_score_analytics.",
            "py <score1> <score2> ...<scoreN>\n",
            )
        return 1
    return 0


def main():
    handle_print("start")
    if scores_check() != 0:
        return
    scores = process_scores()
    handle_print("scores", scores)


if __name__ == "__main__":
    main()
