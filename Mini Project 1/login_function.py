# I have written a Python script for login_validation, but now that I have learned about functions, I want to create this into a function so that it can be reusable.

def validate_login (username, password):
    valid_username = "validusername1"
    valid_password = "validpassword1"

    if username == valid_username and password == valid_password:
        return True 
    return False

# testing the function
print(validate_login("validusername1", "validpassword1")) #True
print()
print(validate_login("wrongusername", "wrongpassword")) #False
print()
print(validate_login("", "")) #False since fields are empty
print()
print(validate_login("validusername1", "wrongpassword")) #False
print()
print(validate_login("wrongusername", "validpassword1")) #False
print()

