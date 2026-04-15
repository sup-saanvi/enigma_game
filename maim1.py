import string
import random

# --- Atbash "Enigma" core ---

ALPHABET = string.ascii_uppercase
ATBASH_MAP = {c: ALPHABET[::-1][i] for i, c in enumerate(ALPHABET)}
 
# --- Atbash "Enigma" core ---
 
def atbash_transform(text: str) -> str:
    """
    Apply Atbash cipher to the given text.
    Non-letters are kept as-is.
    """
    result = []
    for ch in text.upper():
        if ch in ATBASH_MAP:
            result.append(ATBASH_MAP[ch])
        else:
            result.append(ch)
    return "".join(result)

# --- Game utilities ---

SECRET_MESSAGES = [
    "ENIGMA",
    "ATBASH CIPHER",
    "PYTHON IS NOT FUN",
    "CRYPTOGRAPHY",
    "HELLO WORLD",
    "SECRET MESSAGE",
    "CODE BREAKER",
]
def encrypt_mode():
    print("\n--- Encrypt Mode ---")
    plaintext = input("Enter plaintext: ")
    ciphertext = atbash_transform(plaintext)
    print(f"Ciphertext (Atbash): {ciphertext}\n")

    
def decrypt_mode():
    print("\n--- Decrypt Mode ---")
    ciphertext = input("Enter ciphertext: ")
    plaintext = atbash_transform(ciphertext)
    print(f"Plaintext (Atbash): {plaintext}\n")


def game_mode():
    print("\n--- Game Mode: Break the Atbash ---")
    secret = random.choice(SECRET_MESSAGES)
    encrypted = atbash_transform(secret)
    print(f"Encrypted message: {encrypted}")
    guess = input("Your guess (plaintext): ").upper().strip()

    if guess == secret:
        print("Correct! You broke the code!\n")
    else:
        print(f"Not quite. The correct plaintext was: {secret}\n")
# main code for the game!

def main_menu():
    while True:
        print("=== Atbash Enigma Machine ===")
        print("1) Encrypt a message")
        print("2) Decrypt a message")
        print("3) Play guessing game")
        print("4) Quit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            encrypt_mode()
        elif choice == "2":
            decrypt_mode()
        elif choice == "3":
            game_mode()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main_menu()
