import math
from sys import argv


def create_spawn_point(x: float, y: float, z: float) -> tuple:
    """Create a 3D spawn point position (x, y, z)."""
    return (x, y, z)


def calculate_distance(point1: tuple, point2: tuple) -> float:
    """
    Calculate 3D Euclidean distance between two points.
    Formula: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def demonstrate_tuple_unpacking(coordinates: tuple) -> None:
    """Show off tuple unpacking magic - like unwrapping presents!"""
    print("Unpacking demonstration:")
    x, y, z = coordinates
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def length(iter: list) -> int:
    """Return the length of an iterable."""
    count = 0
    for _ in iter:
        count += 1
    return count


def main() -> int:
    """Main function to demonstrate the 3D coordinate system."""
    print("=== Game Coordinate System ===")
    if length(argv) == 2:
        try:
            x = tuple(float(arg) for arg in argv[1].split(','))
        except ValueError:
            print("Error: Invalid command line arguments for coordinates.")
            return 1
    elif length(argv) == 4:
        try:
            x = (
                float(argv[1]),
                float(argv[2]),
                float(argv[3])
                )
        except ValueError:
            print("Error: Invalid command line arguments for coordinates.")
            return
    elif length(argv) == 1:
        x = (10, 20, 5)
    pos1 = create_spawn_point(x[0], x[1], x[2])
    print(f"Position created: {pos1}")
    origin = (0, 0, 0)
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1:.2f}")
    demonstrate_tuple_unpacking(pos1)
    return 0


if __name__ == "__main__":
    main()
