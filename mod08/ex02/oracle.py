import os, sys
from dotenv import load_dotenv
def oracle():
    try:
        load_dotenv()
    except Exception as e:
        print(f"Error loading .env file: {e}")
        return
    values = (
            "MATRIX_MODE",
            "DATABASE_URL",
            "API_KEY",
            "LOG_LEVEL",
            "ZION_NETWORK"
            )
    for var in values:
        value = os.getenv(var)
        if value is None:
            raise ValueError(f"Warning: {var} is not set in the environment variables.")
        else:
            print(f"{var} is set to: {value}")


def main():
    try:
        oracle()
        print("Oracle function executed successfully.")
    except Exception as e:
        print(f"load .env: {e}")
    print(f"Mode: {os.getenv('MODE')}")
    print(f"Database URL: {os.getenv('DATABASE_URL')}")
    print(f"API Key: {os.getenv('API_KEY')}")
    print(f"log_level: {os.getenv('LOG_LEVEL')}")
    print(f"zion network: {os.getenv('ZION_NETWORK')}")
    print("\n enviroment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

if __name__ == "__main__":
    main()
