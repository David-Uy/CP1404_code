BONUS_THRESHOLD = 1000
MINIMUM_BONUS = 0.1
MAXIMUM_BONUS = 0.15

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < BONUS_THRESHOLD:
        bonus = sales * MINIMUM_BONUS
    elif sales >= BONUS_THRESHOLD:
        bonus = sales * MAXIMUM_BONUS
    print(f"Bonus: ${bonus}")
    sales = float(input("Enter sales: $"))
