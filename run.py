import gspread
from google.oauth2.service_account import Credentials
import json

# Every Google account has as an IAM (Identity and Access Management)
# configuration which specifies what the user has access to.
# The SCOPE lists the APIs that the program should access in order to run.

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_info(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("python-cows")

def new_birth():
    print("I hope calving season is going well!")
        while True:
            a = input(("Do you wish to record the birth of a new animal? Y or N:"))
            if a=="Y":
                print(input(("Was the animal still born? Y or N?:/n")))
            elif a=="N":
                print("Please come back when you have data to record")
             else:
        print("Enter either Y/N")

new_birth()



