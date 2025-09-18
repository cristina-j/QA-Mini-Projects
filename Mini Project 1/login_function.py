# I have written a Python script for login_validation, but now that I have learned about functions, I want to create this into a function so that it can be reusable.

def validate_login (username, password):
    valid_username = "validusername1"
    valid_password = "validpassword1"

    if username == valid_username and password == valid_password:
        return True 
    return False

# testing the function
print(validate_login("validusername1", "validpassword1")) #True
print(validate_login("wrongusername", "wrongpassword")) #False
