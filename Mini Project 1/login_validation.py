# This script will reflect a valid login using if/else statements, variables, and functions

#Scenario: You forgot your credentials to sign in to your website account. You called customer service, and they were able to provide you with your correct username and password. 

# This is the username and password that will be embedded for this script.

valid_username = "validusername1"
valid_password = "validpassword1"

# This will allow users to input their login information.

username = input("What is your username? ")
password = input("What is your password? ")

# Using an if/else statement so if the user puts in the correct or incorrect credentials something will happen either way

if username == valid_username and password == valid_password:
    print("Login is successful!")
elif username == "" and password == "":
    print("Username and password fields cannot be empty.")
elif username == valid_username and password != valid_password:
    print("The password provided is not what we have on file. Please enter your correct password.)
elif username != valid_username and password == valid_password:
    print("The username provided is not what we have on file. Please enter your correct username.")
