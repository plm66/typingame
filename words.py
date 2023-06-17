with open('words_1000.txt', 'r') as file:
    words = file.read().split()[:100]

for word in words:
    print(word)