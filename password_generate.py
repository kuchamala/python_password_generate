import random
import string

def generate_password(length=8, uppercase=True, lowercase=True, digits=True, punctuation=True):
    # Define the characters to use in the password
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if punctuation:
        characters += string.punctuation

    # Validate the password length
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))

    # Return the password
    return password

# Example usage
password_length = input("Enter password length: ")
while not password_length.isnumeric():
    password_length = input("Invalid input. Enter password length: ")
password_length = int(password_length)

uppercase = input("Use uppercase letters? (y/n): ").lower() == "y"
lowercase = input("Use lowercase letters? (y/n): ").lower() == "y"
digits = input("Use digits? (y/n): ").lower() == "y"
punctuation = input("Use punctuation? (y/n): ").lower() == "y"
import random
import string

def generate_password(length=8, uppercase=True, lowercase=True, digits=True, punctuation=True):
    # Define the characters to use in the password
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if punctuation:
        characters += string.punctuation

    # Validate the password length
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))

    # Return the password
    return password

# Example usage
while True:
    password_length = input("Enter password length: ")
    while not password_length.isnumeric():
        password_length = input("Invalid input. Enter password length: ")
    password_length = int(password_length)

    uppercase = input("Use uppercase letters? (y/n): ").lower() == "y"
    lowercase = input("Use lowercase letters? (y/n): ").lower() == "y"
    digits = input("Use digits? (y/n): ").lower() == "y"
    punctuation = input("Use punctuation? (y/n): ").lower() == "y"

    if not any((uppercase, lowercase, digits, punctuation)):
        print("You must choose at least one specification.")
        continue

    password = generate_password(length=password_length, uppercase=uppercase, lowercase=lowercase, digits=digits, punctuation=punctuation)
    print("Your password is:", password)

    play_again = input("Generate another password? (y/n): ")
    if play_again.lower() != "y":
        break

password = generate_password(length=password_length, uppercase=uppercase, lowercase=lowercase, digits=digits, punctuation=punctuation)
print("Your password is:", password)
