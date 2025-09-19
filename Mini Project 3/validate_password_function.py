# I have written a Python script for validate_password.py, but now that I have learned about functions, I want to create this into a function so that it can be reusable.

# The requirements of this password is to:
   #make sure there are at least 16 characters 
    #make sure there is at least one number 
    #make sure there is at least one special character

def validate_password(password): validate_password
  
    #checks the length of the password
    if len(password) < 16:
        return False
    
    #checks if there is one number in password
    has_one_number = False 
    for number in password:
        if number.isdigit():
            has_one_number = True 
            break 
    if not has_one_number:
        return False

    #checks to see if password has a special character
    special_characters = "!@#$%^&*()_-+=:;'<>,./[/]{?}"
    has_special_character = False
    for character in password:
        if character in special_characters:
            has_special_character = True
            break
    if not has_special_character:
        return False
         
    #this is if the password has all the requirements
    return True
    

# testing the function
print(validate_password("notlongenough1")) #False
print(validate_password("thereisnotnumber*")) #False
print(validate_password("hasanumber1butnospecialchar")) #False
print(validate_password("thisisavalidpassword1#")) #True
