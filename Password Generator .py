"""Creating a python program on strong password generator by user details i.e (name, birth year, 
special character, passwolrd length) and random values i.e (digits,alphabets, punctuations)"""
import random
import string
#The special characters values
SPECIAL_CHARS = "!@#$%^&*()"
def generate_password(name, birth_year, special_char="!", length=12):
    #Here the first element in uppercase, from index value 1 to 3 elements are in lowercase
    name_part = name[0].upper() + name[1:3].lower()
    #the last 2 values in the birth year  
    year_part = str(birth_year)[-2:]
    #the elements are printed in reverse order as per the length
    reversed_name = name[::-1].lower()
    #the random values are choice between digits, punctuation or uppercase alphabets
    random_char = random.choice(string.digits + string.punctuation + string.ascii_uppercase)
    """the password in the formate of name,year,special character, one random character and
    the name prints in reverse order based on given length"""
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
#the name must contain only alphabets otherwise it displays invalid message and exits 
if not name.isalpha():
    print("Invalid: Name should contain only alphabetic characters.")
    exit()

year_input = input("Birth Year: ")
#The year must contain numbers only otherwise it displays invalid messsage and exits
try:
    year = int(year_input)
except ValueError:
    print("invalid: Birth year must be a number.")
    exit()

special = input(f"Special Character (choose from {SPECIAL_CHARS}, default '!'): ") or "!"
# The special characters must be "!@#$%^&*()" these only otherwise it displays error message
if special not in SPECIAL_CHARS:
    print(f"Error: Special character must be one of: {SPECIAL_CHARS}")
    exit()
#The length must be a number only otherwise it displays invalid message
try:
    length = int(input("Enter desired password length: "))
except ValueError:
    print("invalid: Password length must be a number.")
    exit()

print("Generated Password:", generate_password(name, year, special, length))
