import random
import string


def generate_password(min_len, numbers=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_character:
        characters += special

    pwd = ""
    meets_criteria = False

    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_character:
            meets_criteria = meets_criteria and has_special

    return pwd


min_len = input("Enter the min len for password")
if min_len.isdigit():
    min_len = int(min_len)
else:
    print("The min len should be a digit")
has_number = input("Do you want to have number (y/n): ").lower()
has_special = input("Do you want to have special characters (y/n): ").lower()
if has_number == 'y':
    has_number = True
else:
    has_number = False
if has_special == 'y':
    has_special = True
else:
    has_special = False
pwd = generate_password(10, has_number, has_special)
print(pwd)
