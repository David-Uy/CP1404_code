import random

MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    user_score = get_user_score()
    result = evaluate_score(user_score)
    print(result)

    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    result = evaluate_score(random_score)
    print(f"Random score: {random_score}, Result: {result}")


def get_user_score():
    """Get the user's score as input.

    Returns:
        float: The user's score.
    """
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))

    return score


def evaluate_score(score):
    """Evaluate the score and provide a corresponding result.

    Args:
        score (float): The score to be evaluated.

    Returns:
        str: The result based on the score.
    """
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score > PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()
