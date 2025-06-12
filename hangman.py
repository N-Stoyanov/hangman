import random

words = ["hashmap", "spotify", "steam", "switch", "witcher", "doctor", "gs"
"guitar"]

chosen_word = random.choice(words)
guessed_word = ["_"] * len(chosen_word)
guessed_letters = []
lives = 6

print("Welcome to Hangman!")

while lives > 0 and "_" in guessed_word:
    print("\nWord: " + " ".join(guessed_word))
    print("\nGuessed Letters: " + " ".join(guessed_letters))
    print("\nLives: " + " ".join(str(lives)))

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single digit letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Adds to the list of guessed letters
    guessed_letters.append(guess)

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        lives -= 1
        print("Incorrect.")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word " + chosen_word + "!")
else:
    print("\nGame Over! The correct word was " + chosen_word + ".")
