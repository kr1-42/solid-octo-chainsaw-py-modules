"""Vault Security Protocol - secure file operations with context managers."""

import sys
from pathlib import Path


CLASSIFIED_PATH = Path(__file__).resolve().parents[1] / "ex0" / "classified_data.txt"
PRESERVE_PATH = Path(__file__).resolve().parent / "preserved_protocols.txt"


def secure_extraction() -> None:
	print("SECURE EXTRACTION:")
	try:
		with CLASSIFIED_PATH.open("r", encoding="utf-8") as vault:
			for line in vault:
				line = line.rstrip("\n")
				if not line:
					continue
				if line.startswith("[CLASSIFIED]"):
					print(line)
				else:
					print(f"[CLASSIFIED] {line}")
	except FileNotFoundError:
		print("[ALERT] Classified vault not found", file=sys.stderr)
	except OSError:
		print("[ALERT] Classified vault access failure", file=sys.stderr)


def secure_preservation() -> None:
	print("SECURE PRESERVATION:")
	try:
		with PRESERVE_PATH.open("w", encoding="utf-8") as vault:
			vault.write("New security protocols archived\n")
		print("[CLASSIFIED] New security protocols archived")
	except OSError:
		print("[ALERT] Preservation vault write failure", file=sys.stderr)


def main() -> None:
	print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
	print("Initiating secure vault access...")
	print("Vault connection established with failsafe protocols")

	secure_extraction()
	secure_preservation()

	print("Vault automatically sealed upon completion")
	print("All vault operations completed with maximum security.")


if __name__ == "__main__":
	main()
