import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
print(random.randint(1, 100))  # produce random number 1 - 100

"""
result: 18 on Line 1. smallest 5, biggest 20
result: 7 on line 2. smallest 3, largest 9. couldn't produce 4 because step is 2 and 4 is not odd number.
result: 2.54 on line 3. smallest 2.5, largest 5.5.
"""