
import random
from words import country
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import pyfiglet

print(pyfiglet.figlet_format("Welcome to Destination Unknown"))


def introduction_message():  
    while True:
        name = input("What is your name?\n")
        if name.isalpha():
            print(f"Good day {name} !")
            print("Try to guess the county by choosing a letter.")
            print("You have x tries.")
            print("If you try to guess same letter twice :")
            print("*if it is not in the word you will loose attempt.")
            print(f"GOOD LUCK {name}!")
            choose_word()
        else:
            print("I do not understand, add letters only.\n")
            introduction_message()


def choose_word():
    word = random.choice(country)
    while '-' in word or ' ' in word:
        word = random.choice(country)
    return word


def word_in_progress(word, guesses):
    word_in_progress = ""
    for letter in word:
        if letter in guesses:
            word_in_progress += letter
        else:
            word_in_progress += "*"
    return word_in_progress

def play_again():
    play_again = input("Would you like to continue yes or no?: ")
    if play_again == ("yes"):
        choose_word()
    elif play_again == ("no"):
        print("Thank you for playing")
    else:
        print("Sorry invalid entry.")
        print("Plese enter yes or no.")
        play_again()

def main(word):
    lettersguessed = []
    chances = len(word)*int(1.5)
    name = input("What is your name?\n")
# Here the user is asked to enter the name first

    print(f'"Good Luck "{name}')
    print(Fore.CYAN + "You are looking for a word that is " + str(len(word)) + " letters long.")

    while True:
        if chances != 0:
            print("\nYou have " + str(chances) + " chances left.")
            time.sleep(2)
            print("Word so far: " + word_in_progress(word, lettersguessed))
            time.sleep(2)
            print(Fore.LIGHTGREEN_EX + "Letters guessed: " + str(lettersguessed))
            guess = input("Guess: ").lower()[0]

            if guess not in lettersguessed:
                lettersguessed.append(guess)

            if word_in_progress(word, lettersguessed) == word:
                print("\nCongratulations! You got the right word: " + word)
                break

            else:
                if guess in word:
                    print("Correct letter!")
                else:
                    print(guess + " is not in the word.")
                    chances -= 1
        else:
            print("\nOops you ran out of guesses. The correct word was " + word)
            break


while True:
    word = choose_word()
    main(word)
    play_again()


  
# def validate_data(values):
#     """
#     Inside the try, converts all string values into integers.
#     Raises ValueError if strings cannot be converted into int,
#     or if there aren't exactly 6 values.
#     """

#     try:
#         [int(value) for value in values]
#         if len(values) != 6:
#             raise ValueError(
#                 f"Exactly 6 values are required, you provided {len(values)}")

#     except ValueError as e:
#         print(f"Invalid data: {e}, please try again\n")
#         return False

#     return True