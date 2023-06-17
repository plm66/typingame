import random
from playsound import playsound


common_words = []
with open('words_1000.txt', 'r') as f:
    for line in f:
        word = line.strip()
        common_words.append(word)
        if len(common_words) >= 1000:
            break
def generate_string(length, words):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter = random.choice(letters)
    word = random.choice([w for w in words if letter in w])
    return f"{letter} {word}"
incorrect_words = []
while True:
    string = generate_string(5, common_words)
    print(f"letter & word : {string}")
    user_input = input().rstrip()
    if user_input == string:
        print("Correct! continue... 🤝")
    else:
        print("Incorrect. Please Pratice this word! 🤬.")
        incorrect_words.append(string.split()[1])
        with open('incorrect_words.txt', 'a') as f:
            f.write(f"{string.split()[1]}\n")
        playsound('buzz3.wav') # play sound file

    if len(incorrect_words) >= 10:
        print("You have made 10 errors. Practice these words:")
        print(", ".join(incorrect_words))
        incorrect_words = []