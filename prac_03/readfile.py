# 1. read line
FILENAME = "testfile.txt"
in_file = open(FILENAME)
text = in_file.read()
in_file.close()
print(text)

# 2. Read line in loop
# in_file = open("testfile.txt")
# for line in in_file:
#     print(line)
#     # print(line.strip())  # remove 1 \n
# in_file.close()

