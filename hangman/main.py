import random
from hangman_words import word_list
from hangman_art import logo, stages

print (logo)

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessedLetters = []

while not game_over:

    print(f"You have {lives} remaining!")
    print(f"Guessed letters: {guessedLetters}")
    guess = input("Guess a letter: ").lower()
    if guess in guessedLetters:
        print("You have already guessed that letter, try again!")
        guess = input("Guess a letter: ").lower()
    guessedLetters += guess

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"**********You lose!! The correct word was {chosen_word}**********")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
