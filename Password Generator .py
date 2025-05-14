import random
import string

SPECIAL_CHARS = "!@#$%^&*()"

def generate_password(name, birth_year, special_char="!", length=12):
    name_part = name[0].upper() + name[1:3].lower()
    year_part = str(birth_year)[-2:]
    reversed_name = name[::-1].lower()
    random_char = random.choice(string.digits + string.punctuation + string.ascii_uppercase)
    base = name_part + year_part + special_char + random_char + reversed_name
    if len(base) > length:
        password = base[:length]
    elif len(base) < length:
        padding = ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(base)))
        password = base + padding
    else:
        password = base

    return password
name = input("Enter Name: ").strip()
if not name.isalpha():
    print("Invalid: Name should contain only alphabetic characters.")
    exit()

year_input = input("Birth Year: ")
try:
    year = int(year_input)
except ValueError:
    print("Error: Birth year must be a number.")
    exit()

special = input(f"Special Character (choose from {SPECIAL_CHARS}, default '!'): ") or "!"
if special not in SPECIAL_CHARS:
    print(f"Error: Special character must be one of: {SPECIAL_CHARS}")
    exit()

try:
    length = int(input("Enter desired password length: "))
except ValueError:
    print("Error: Password length must be a number.")
    exit()

print("Generated Password:", generate_password(name, year, special, length))
