import random


def get_wordlist():
    with open("wordlist.txt", "r") as file:
        words = file.read().splitlines()
    return words


def random_word_generator(word_list):
    return random.choice(word_list)


def input_guess(available_letters, secret_letters, lives):
    while True:
        try:
            user_guess = input("\nGuess a letter: ")
            if not user_guess.isalpha():
                raise Exception("\nYou must guess a letter!")
            elif len(user_guess) != 1:
                raise Exception("\nYou must only guess one letter at a time!")
            elif user_guess not in available_letters:
                raise Exception("\nYou've guessed that letter already!")
            else:
                break
        except Exception as error:
            print(error)

    if user_guess not in secret_letters.values():
        lives -= 1
        if lives > 0:
            print(f"\nYour guess is incorrect! You only have {lives} lives left.\n")
    return user_guess, lives


def update_progress(user_progress, secret_letters, user_guess):
    for position, letter in secret_letters.items():
        if user_guess == letter:
            user_progress[position] = letter
            print("\nYour guess is correct!\n")
    print(" ".join(user_progress))
    return user_progress


def update_available_letters(user_guess, available_letters):
    available_letters = available_letters.replace(user_guess, "")
    return available_letters


def play_hangman():
    words = get_wordlist()
    secret_word = random_word_generator(words)
    secret_letters = {}
    for index, letter in enumerate(secret_word):
        secret_letters[index] = letter

    print(f"\nWelcome to Hangman!\n")
    print(f"\nYour word is {len(secret_letters)} letters long.")
    print(secret_word)
    print(secret_letters)
    user_progress = ["_"] * len(secret_letters)
    print(" ".join(user_progress))
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    lives = 7
    while "_" in user_progress:
        user_guess, lives = input_guess(available_letters, secret_letters, lives)
        user_progress = update_progress(user_progress, secret_letters, user_guess)
        available_letters = update_available_letters(user_guess, available_letters)
        if "".join(user_progress) == secret_word:
            print("\nCongratulations! You have guessed the word! You win!")
            break
        if lives == 0:
            print(f"\nYou are out of luck! You lose!\nThe secret word was {secret_word.capitalize()}!\n")
            break

play_hangman()