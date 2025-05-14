import secrets
import string

def generate_password(length, include_numbers, include_uppercase, include_lowercase, include_special):
    # Define the password characters
    character = ""

    # Default character set
    if not include_numbers and not include_uppercase and not include_lowercase and not include_special:
        character = string.ascii_letters + string.digits + string.punctuation

    # Generate the character set
    if include_numbers:
        character += string.digits
    if include_uppercase:
        character += string.ascii_uppercase
    if include_lowercase:
        character += string.ascii_lowercase
    if include_special:
        character += string.punctuation

    # Generate the password
    password = ''.join(secrets.choice(character) for i in range(length))

    return password
