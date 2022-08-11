
import random
from words import country
import time
import colorama
import sys
import os
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import pyfiglet


print(pyfiglet.figlet_format("Destination Unknown"))


def introduction_message():
    while True:
        name = input(f"{Fore.GREEN+Style.BRIGHT}What is your name?\n")

        if not name.isalpha():
            print(f"{Fore.RED+Style.BRIGHT}Your name must be alphabetic only")
            continue
        else:
            print(f'Good luck, {name}!')
            break
   
   
        

def choose_word():
    word = random.choice(country)
    while '-' in word or ' ' in word:
        word = random.choice(country)
    return word.lower()

def word_in_progress(word, guesses): #changed to current_country
    word_in_progress = ""
    for letter in word:
        if letter in guesses:
            word_in_progress += letter
        else:
            word_in_progress += "*"
    return word_in_progress




FIREWORKS = """
                                 .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def main(word): #change main to start game
    lettersguessed = [] #change to player_guesses
    chances = len(word)*int(1.5)
  
# Here the user is asked to enter the name first

    
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
                print(FIREWORKS)
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
    if play_again == ("yes" or "YES"):
        choose_word()
    elif play_again == ("no" or "NO"):
        print("Thank you for playing")
        goodbye_message()
    else:
        print("Sorry invalid entry.")
        print("Plese enter yes or no.") 
# def play_again():
#     while True:
#         play_again = input(f"{Fore.GREEN+Style.BRIGHT}Would you like to play again?\n")

#         if play_again == ("yes" or "YES"):
#             main(word)
#         continue
#         else :
#         print("Thank you for playing")
#         goodbye_message()
#         print("Pleae enter yes or no")
#         break


def clear_screen():
    """
    Used to clear Terminal screen
    Credit: https://www.101computing.net/python-typing-text-effect/
    """
    os.system("clear")

while True:
    word = choose_word()
    introduction_message()
    main(word)
    play_again()



  