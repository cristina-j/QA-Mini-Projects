'''This script will validate a password that a user inputs to make sure it meets all the requirments. The user will have three attempts to create a valid password.

The Requirements are:
- password must be 16 characters long 
- password must include at least 1 number 
- password must include at least 1 special character
'''

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Create a password: ")

    # This will verify if the password is a valid one 
    is_valid = True 

    # Check the length of the password
    if len(password) < 16:
        print("\nPassword must be at least 16 characters long.\n")
        is_valid = False
        

    # Check to see if it has at least one number 
    has_one_number = False
    for character in password:
        if character.isdigit():
            has_one_number = True 
            break
    if not has_one_number:
        print("\nPassword must include at least one number.\n")
        is_valid = False

    # Check to see if password has at least one special character
    special_characters = "!@#$%^&[*]()_{/}-+=:;'<>,.?'"
    has_special_characters = False
    for character in password:
        if character in special_characters:
            has_special_characters = True
            break 
    if not has_special_characters:
        print("\nPassword must include at least one special character.\n")
        is_valid = False

    # Checking to see if is_valid works 
    if is_valid:
        print("\nPassword is accepted!\n")
        break
    else:
        attempts += 1 
        print(f"Attempts left: {max_attempts - attempts}\n")


# This will lockout the user if they reach the max attempt
if attempts == max_attempts:
    print("Too many invalid attempts. Please try again later.")
