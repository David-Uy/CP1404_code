"""
Word Occurrences
Estimate: 10 minutes
Actual:   19 minutes
"""

user_input = input("Enter a string: ")
words = user_input.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_length_word = max(len(word) for word in word_count.keys())

for word, count in sorted(word_count.items()):
    print(f"{word:{max_length_word}} : {count}")

