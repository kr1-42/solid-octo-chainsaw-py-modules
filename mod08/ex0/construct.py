
import os
import sys


def in_virtual_environment() -> bool:
    """Check if the current Python environment is a virtual environment."""
    return sys.prefix != sys.base_prefix


def print_disconnected_message() -> None:
    """Print a message indicating the user is not in a virtual environment."""
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows")
    print("Then run this program again.")


def print_connected_message() -> None:
    """Print a message indicating the user is in a virtual environment."""
    env_path = sys.prefix
    env_name = os.path.basename(env_path.rstrip(os.sep))
    package_path = ""
    for path in sys.path:
        if path.startswith(env_path) and path.endswith("site-packages"):
            package_path = path
            break

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    print(package_path)


def main() -> None:
    """Main function to check virtual environment status and print messages."""
    if in_virtual_environment():
        print_connected_message()
    else:
        print_disconnected_message()


if __name__ == "__main__":
    main()
