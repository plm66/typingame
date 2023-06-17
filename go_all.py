import random
from playsound import playsound

common_words = []
with open('words_1000.txt', 'r') as f:
    for line in f:
        word = line.strip()
        common_words.append(word)
        if len(common_words) >= 1000:
            break
with open('incorrect_words.txt', 'r') as f:
    incorrect_words = [line.strip() for line in f]

def generate_string(words):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter = random.choice(letters)
    word = random.choice([w for w in words if letter in w])
    index = random.randint(0, len(word) - 1)
    return f"{letter} {word[:index]}{letter}{word[index+1:]}"

num_attempts = 0
while True:
    string = generate_string(common_words)
    print(f"Type the letter followed by a word containing that letter: {string}")
    user_input = input().rstrip()
    if user_input == string:
        print("Correct!")
    else:
        print("Incorrect. Try again.")
        incorrect_words.append(string.split()[1])
        with open('incorrect_words.txt', 'a') as f:
            f.write(f"{string.split()[1]}\n")
        playsound('buzz3.wav') # play sound file
    num_attempts += 1
    if len(incorrect_words) >= 10 or num_attempts >= 1000:
        print("You have made 10 errors. Practice these words:")
        print(", ".join(incorrect_words))
        incorrect_words = []
        num_attempts = 0