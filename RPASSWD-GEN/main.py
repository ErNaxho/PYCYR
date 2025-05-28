import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    all_chars = letters + digits + special_chars
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    password += random.choices(all_chars, k=length - 3)

    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    print("Generated password:", generate_password(length))