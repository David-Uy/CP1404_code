MINIMUM_LENGTH = 8
password = input("Enter a password: ")

while len(password) < MINIMUM_LENGTH:
    print("Invalid Password. Too short")
    print("*" * len(password))
    password = input("Enter Password: ")

print("*" * len(password))
print("Created")