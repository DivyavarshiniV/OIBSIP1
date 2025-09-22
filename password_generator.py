import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    """Generate a random password."""
    characters = string.ascii_letters  # a-z + A-Z
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Simple Password Generator")

    try:
        length = int(input("Enter password length (default=12): ") or 12)
    except ValueError:
        print("❌ Invalid input. Using default length 12.")
        length = 12

    include_digits = input("Include digits? (y/n): ").lower() == "y"
    include_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, include_digits, include_symbols)
    print(f"\n✅ Generated Password: {password}")

if _name_ == "_main_":
    main()
