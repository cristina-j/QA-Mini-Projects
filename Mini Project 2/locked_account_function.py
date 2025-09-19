# I have written a Python script for locked_account.py, but now that I have learned about functions, I want to create this into a function so that it can be reusable.

def locked_out (username, password, attempts, max_attempts = 3):
    valid_username = "validusername1"
    valid_password = "validpassword1"

    if attempts >= max_attempts:
        return False, "Account has been locked."

    if username == valid_username and password == valid_password:
        return True, "Login is successful."
    else:
        return False, "Invalid login information."


print(locked_out("validusername1", "validpassword1", attempts =0)) #True
print() # Adding a blank space so it is easier to read

print(locked_out("wrongusername", "wrongpassword", attempts = 1)) #False
print()

print(locked_out("", "", attempts = 2)) #False
print()

print(locked_out("validusername1", "wrongpassword", attempts = 3)) # False. "Account has been locked" should appear.
