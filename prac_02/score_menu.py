MENU = "Menu:\n (G)et Valid Score \n (P)rint Result\n (S)how stars\n (Q)uit"
MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    print(MENU)
    choice = input("Select an option: ").upper()
    score = -1
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(MENU)
            choice = input("Select an option: ").upper()
        elif choice == "P":
            if score == -1:
                print("Invalid. Enter the score first")
                print(MENU)
                choice = input("Select an option: ").upper()

            else:
                result = evaluate_score(score)
                print("Result: ", result)
                print(MENU)
                choice = input("Select an option: ").upper()

        elif choice == "S":
            if score == -1:
                print("Invalid. Enter the score first")
                print(MENU)
                choice = input("Select an option: ").upper()
            else:
                show_stars(score)
                print(MENU)
                choice = input("Select an option: ").upper()
        else:
            print("Invalid choice. Try again.")
            choice = input("Select an option: ").upper()

    print("Farewell!")


def evaluate_score(score):
    """
    Returns the evaluation of the score.
    This function will check if the score is Excellent, Passable, or Bad based on predefined thresholds.
    """
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score > PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """
    Prints stars based on the score.
    This function will print a number of stars corresponding to the score.
    """
    print("*" * int(score))


def get_valid_score():
    """
    Get a valid score from the user.
    This function will prompt the user to enter a score and validate if it is within the valid range.
    """
    score = float(input("Score:"))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))

    return score


main()
