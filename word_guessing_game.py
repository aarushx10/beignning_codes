import random

def random_words(lang):
    if lang == "y":
        words=["garmi","thandi","sundar","kambal"]
    else:
        words=["beautiful","blossom","handsome","weather","watch"] 
    word = random.choice(words)
    for i in range(len(word)):
        print("_")
    return word

def guessing_character(word,guesses):
    display = ""
    for char in word:
        if char in guesses:
            display += char + " "
        elif char not in guess:
            display += "_ "
    print(display.strip())
    return display
        
         

# Game start Logic

name = input("What's your name: ")
print(f"Hello, {name} Let's play")
lang = input("want to guess hindi words? if yes, press 'y' else 'n' and for exit press 3: ").lower()

if lang== "3":
    print("Thank you 😊")
    exit()

elif lang not in ["y","n"]:
    raise Exception("Please type 'y', 'n', or '3' to exit")

word = random_words(lang)
guesses = ""
attempts = 12
while attempts > 0:
    guess = input("guess a character: ").lower()
    if guess == "3":
        print("Thank you 😊")
        break
    elif len(guess) != 1:
        print("Please enter a single character")
        continue
    if guess in guesses:
        print("You already guessed that letter.")
        continue
    guesses += guess

    if guess not in word:
        print("Wrong guess.")
        attempts -=1
        print(f"Attempts left: {attempts}")
        
    display = guessing_character(word,guesses)

    if "_" not in display:
        print("You Win")
        break
        

else:
    print("You have run out of attempts.")
print(f"The correct word was: {word}")
