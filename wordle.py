
import random
from words import country
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import pyfiglet

def introduction_message():
    print(pyfiglet.figlet_format("Welcome to Destination Unknown", justify="center"))

introduction_message()


def choose_word():
    word = random.choice(country).lower()
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
    name = input("What is your name?\n")
# Here the user is asked to enter the name first
 
    print(f'"Good Luck "{name}')
    print(Fore.CYAN + "You are looking for a word that is " + str(len(word)) + " letters long.")

    while True:
        if chances != 0:
            print("\nYou have " + str(chances) + " chances left.")
            time.sleep(2)
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

