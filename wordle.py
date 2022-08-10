
import random
from words import words
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)



def choose_word():
    word = random.choice(words).lower()
    return word


def word_in_progress(word, guesses):
    word_in_progress = ""
    for letter in word:
        if letter in guesses:
            word_in_progress += letter
        else:
            word_in_progress += "*"
    return word_in_progress


def main(word):
    lettersguessed = []
    chances = 6
    print(Fore.CYAN + "You are looking for a word that is " + str(len(word)) + " letters long.")

    while True:
        if chances != 0:
            print("\nYou have " + str(chances) + " chances left.")
            print("Word so far: " + word_in_progress(word, lettersguessed))
            print(Fore.LIGHTGREEN_EX + "Letters guessed: " + str(lettersguessed))
            guess = input("Guess: ").lower()[0]

            if guess not in lettersguessed:
                lettersguessed.append(guess)

            if word_in_progress(word, lettersguessed) == word:
                print("\nCongratulations! You got the right word: " + word)
                break

            else:
                chances -= 1
                if guess in word:
                    print("Correct letter!")
                else:
                    print(guess + " is not in the word.")
        else:
            print("\nOops you ran out of guesses. The correct word was " + word)
            break


while True:
    word = choose_word()
    main(word)
    if input("Would you like to continue: ").lower().startswith("n"):
        break

