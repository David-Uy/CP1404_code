# 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)

# 3
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number
print(total)