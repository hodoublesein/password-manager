import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    """Generate a random password"""
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    return "".join(random.choice(characters) for _ in range(length))
