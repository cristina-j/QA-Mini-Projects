# This script will reflect a valid login using if/else statements, variables, and functions

#Scenario: You forgot your credentials to sign in to your website account. You called customer service, and they were able to provide you with your correct username and password. You only have three attempts to sign in with your correct credentials, otherwise your account will be locked. 

valid_username = "validusername1"
valid_password = "validpassword1"

# This will be a while loop for the amount of times you can enter the wrong credentials 

attempts = 0
max_attempts = 3


while attempts < max_attempts:

# First the user needs to be asked to input credentials

    username = input("What is your username? ")
    password = input("What is your password? ")

    if username == valid_username and password == valid_password:
        print("\nLogin is successful!")
        break #This breaks the loop here since credentials were accepted successfully
    elif username == "" and password == "":
        print("\nUsername and password fields cannot be empty.\n")
    elif username == valid_username and password != valid_password:
        print("\nThe password provided is not correct.\n")
    elif username != valid_username and password == valid_password:
        print("\nThe username provided is not correct.\n")
    else:
        print("\nInvalid password and username.\n")

# This will be counting how many attempts a user has left to login with correct credentials

    attempts += 1 
    print(f"Login attempts left: {max_attempts - attempts}\n")

# When the amount of attempts reaches the max, the user will be presented with a message

if attempts == max_attempts:
    print("\nThe maximum amount of attempts to login has been reached. You are now locked out.\n")
