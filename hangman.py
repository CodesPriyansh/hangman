import random

print("Welcome to HANGMAN!")
print("You get 6 lives to guess a word!")

simple_words = ["wizard", "archer", "summer", "guitar", "hitler", "planet", "python", "spyder"]
lives = 6

word = random.choice(simple_words)

while lives > 0:
    print(word[0])
    guess = input("guess this word:")
    if guess == word:
        print(f"congratulations! you guessed the word: {word}")
        break
        
    else:
        lives -= 1
        print(f"you {lives} lives left.")
        if lives == 0:
            print("You lose :(")
        


