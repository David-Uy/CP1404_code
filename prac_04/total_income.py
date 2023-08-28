def main():
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(number_of_months):
        income = float(input(f"Enter income for month {month + 1}: "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    print("\nIncome Report")
    print("-" * 13)
    total = 0
    month = 0
    for income in incomes:
        month += 1
        total += income
        print(f"Month {month} - Income: ${income:.2f} Total: ${total:.2f}")


main()
