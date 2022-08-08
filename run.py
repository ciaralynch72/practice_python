import gspread
from google.oauth2.service_account import Credentials
import datetime
import json

# Every Google account has as an IAM (Identity and Access Management)
# configuration which specifies what the user has access to.
# The SCOPE lists the APIs that the program should access in order to run.

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('cred.json'))
CREDS = Credentials.from_service_account_info(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("python-cows")

calves = SHEET.worksheet("calves")
print(calves)

def welcome():
    print("╔═╗┌─┐┬  ┬  ┬┌─┐┌─┐")
    print("║  ├─┤│  └┐┌┘├┤ └─┐")
    print("╚═╝┴ ┴┴─┘ └┘ └─┘└─┘")
    new_birth()


def new_birth():
    """
    Function to welcome to ask the user is a new birth needs to be recorded
    """
    print("\nI hope calving season is going well!")
    print("\nWould you like to record a new birth?")
    question1 = input("\nPlease enter yes or no \n")
    if question1.lower() == ("yes"):
        print("Congratulations")
        date_of_birth()
    elif question1.lower() == ("no"):
        print("Come back after the cow has calved.")
        welcome()
    else:
        print("Sorry invalid entry.")
        print("Plese enter yes or no.")
     

def date_of_birth():
    """
    Find out the date of birth of the animal
    """
    birthday = input('Enter date the calf was born dd/mm/yyyy \n')
    day, month, year = list(map(int, birthday.split("/")))
    birthdate = datetime.date(year, month, day)
    
    print(f"Calf was born on {birthdate.strftime('%d/%m/%Y')}")

    question2 = input("\nConfirm the date is correct yes or no\n")
    if question2.lower() == ("yes"):
        
  
        print("Lovely")
        # update_calves_worksheet()
        animal_sex()
        
    elif question2.lower() == ("no"):
        print("Please re enter the date.")
        date_of_birth()
    else:
        print("Sorry invalid entry.")
        print("Plese enter yes or no.")
        date_of_birth()
     
def animal_sex():
    question3 = input("\n Is the calf a bull of heifer?\n")
    if question3.lower() == ("bull"):
        print("It's a boy")
        # update_calves_worksheet()
    elif question3.lower() == ("heifer"):
        print("it's a girl")
        # update_calves_worksheet()
    else:
        print("Sorry invalid entry.")
        print("Plese enter bull or heifer")
        animal_sex()

# def update_calves_worksheet():
#     """
#     This will update the calves worksheet
#     in the google spreadsheet, and add a new row
#     to the list
#     """
#     print("Updating calves list...\n")
#     calves_worksheet = SHEET.worksheet("calves")
#     calves_worksheet.append_row(calves)
#     print("Spreadsheet updated")



 # Call functions  

welcome()
new_birth()
date_of_birth()
animal_sex()
# update_calves_worksheet()


