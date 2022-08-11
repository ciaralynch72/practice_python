
import random
from words import country
import time
import colorama
import sys
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import pyfiglet

print(pyfiglet.figlet_format("Destination Unknown"))


def introduction_message():  
    while True:
        name = input("What is your name?\n")
        if name.isalpha():
            print(f"Good day {name}!")
            print("Try to guess the county by choosing a letter.")
            print("You have x tries.")
            print("If you try to guess same letter twice :")
            print("*if it is not in the word you will loose attempt.")
            print(f"GOOD LUCK {name}!")
        else:
            print("I do not understand, add letters only.\n")

def choose_word():
    word = random.choice(country)
    while '-' in word or ' ' in word:
        word = random.choice(country)
    return word.lower()

def word_in_progress(word, guesses):
    word_in_progress = ""
    for letter in word:
        if letter in guesses:
            word_in_progress += letter
        else:
            word_in_progress += "*"
    return word_in_progress

def goodbye_message():
    """
   Final function which ends the game if the
   player pressed N to end the game.
   It also prints Goodbye message with pyfiglet.
    """
    print(pyfiglet.figlet_format(f"Goodbye!"))
    sys.exit()

def play_again():
    play_again = input("Would you like to continue yes or no?: ")
    if play_again == ("yes"):
        choose_word()
    elif play_again == ("no"):
        print("Thank you for playing")
        goodbye_message()
    else:
        print("Sorry invalid entry.")
        print("Plese enter yes or no.")
    #main(word)

def main(word):
    lettersguessed = []
    chances = len(word)*int(1.5)
    name = input("What is your name?\n")
# Here the user is asked to enter the name first

    print(f'"Good Luck, {name}!')
    print(Fore.CYAN + "You are looking for a word that is " + str(len(word)) + " letters long.")

    while True:
        if chances != 0:
            print("\nYou have " + str(chances) + " chances left.")
            time.sleep(1)
            print("Word so far: " + word_in_progress(word, lettersguessed))
            time.sleep(1)
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



  