"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
->A ValueError will occur if the user enters a non-integer value (e.g., a string or a float)
for either the numerator or the denominator.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters 0 as the denominator, resulting in an attempt
to divide by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
We can change the code to avoid the possibility of a ZeroDivisionError by checking if the denominator is zero
before performing the division. We can include a conditional statement to handle this case separately.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")