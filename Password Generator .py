def generate_password(name, birth_year,  special_char="!", length=12):
    base = name[0].upper() + name[1:3].lower() + birth_year[-2:] + special_char + name[::-1].lower()
    # Assemble the password
    password = base + special_char 
    return password[:length]  # Trim if over length
name = input("Enter Name: ")
year = input("Birth Year: ")
special = input("Special Character (default '!'): ") or "!"
length = int(input("Enter desired password length: "))

print("Generated Password:", generate_password(name, year, special,length))
