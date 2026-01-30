import math


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


def parse_coordinates(coord_string: str) -> tuple:
    """
    Parse coordinate string like teleport commands.
    Accepts formats: "x,y,z" or "x y z"
    """
    coord_string = coord_string.strip()
    if ',' in coord_string:
        parts = coord_string.split(',')
    else:
        parts = coord_string.split()
    if len(parts) != 3:
        raise ValueError("Invalid format. Use 'x,y,z' or 'x y z'")
    return (float(parts[0]), float(parts[1]), float(parts[2]))


def demonstrate_tuple_unpacking(coordinates: tuple) -> None:
    """Show off tuple unpacking magic - like unwrapping presents!"""
    print("Unpacking demonstration:")
    x, y, z = coordinates
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main():
    """Main function to demonstrate the 3D coordinate system."""
    print("=== Game Coordinate System ===")

    pos1 = create_spawn_point(10, 20, 5)
    print(f"Position created: {pos1}")

    origin = (0, 0, 0)
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1:.2f}")

    print('Parsing coordinates: "3,4,0"')
    try:
        pos2 = parse_coordinates("3,4,0")
        print(f"Parsed position: {pos2}")
        dist2 = calculate_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {dist2:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

    print('Parsing invalid coordinates: "abc,def,ghi"')
    try:
        parse_coordinates("abc,def,ghi")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    demonstrate_tuple_unpacking(pos2)


if __name__ == "__main__":
    main()
