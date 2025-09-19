# Account Lockout Scripts  

This folder contains two versions of my **Account Lockout** project in Python.  

---

## What’s in here  
- **`locked_account.py`**: my first version, a step-by-step script that uses `input()` and a while loop to limit login attempts to 3. After 3 failures, the account is locked.  
- **`locked_account_function.py`**: a refactored version where the login check and lockout logic are written as a **function**. The function returns both a `True/False` value *and* a message to explain the result.  

---

## Why I created these  
I wanted to build on my login validation project by simulating a real-world rule: **lock an account after too many failed login attempts**.  

This project helped me practice:  
- Tracking attempts with a counter  
- Using `if` conditions to block further logins after the limit  
- Refactoring into a function that can handle different test cases (valid login, invalid login, account locked)  

---

## What I learned about functions and return values  
At first, I thought of only returning `True` or `False` from my function.  
But I realized that:  
- `False` could mean either "wrong username/password" OR "account locked"  
- I need more information than just `True/False` to show that the script is working correctly
