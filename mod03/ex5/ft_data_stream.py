import time


def event_stream(total_events):
    players = ["alice", "bob", "charlie", "dora", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]
    for event_id in range(1, total_events + 1):
        player = players[(event_id - 1) % len(players)]
        level = ((event_id * 7) % 20) + 1
        action = actions[(event_id - 1) % len(actions)]
        yield event_id, player, level, action


def fibonacci_stream(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def prime_stream(n):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main():
    total_events = 1000
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {total_events} game events...")

    total_processed = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    start_time = time.time()
    for event_id, player, level, act in event_stream(total_events):
        total_processed += 1
        if total_processed <= 3:
            print(f"Event {event_id}: Player {player} (level {level}) {act}")
        if level >= 10:
            high_level += 1
        if act == "found treasure":
            treasure_events += 1
        if act == "leveled up":
            level_up_events += 1
    end_time = time.time()
    print("...\n\n=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===\n")
    fib_first_10 = []
    for value in fibonacci_stream(10):
        fib_first_10.append(str(value))
    print("Fibonacci sequence (first 10): " + ", ".join(fib_first_10))
    prime_five = []
    for value in prime_stream(5):
        prime_five.append(str(value))
    print("Prime numbers (first 5): " + ", ".join(prime_five))


if __name__ == "__main__":
    main()
