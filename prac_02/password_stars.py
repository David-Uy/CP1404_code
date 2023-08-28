MINIMUM_LENGTH = 8  # A constant for minimum password length


def main():
    """Entry point of the program."""
    password = get_valid_password()
    print_password_asterisk(password)


def get_valid_password():
    """Get a valid password from the user.

    Asks the user to input a password and ensures it meets the minimum length requirement.

    Returns:
        str: The valid password.
    """
    password = input("Enter Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid Password. Too short")
        password = input("Enter Password: ")
    return password


def print_password_asterisk(password):
    """Print the password as asterisks.

    Args:
        password (str): The password to be printed as asterisks.
    """
    print("*" * len(password))


main()
