# QA-Mini-Projects


This repo is where I’m sharing the small Python scripts I’ve been creating as I learn and move from **manual QA into QA engineering**.  

Right now I’m keeping it super simple — just using **variables, input, if/else, while loops, and for loops** — but even with the basics, I’m already building scripts that feel like real QA test cases. 

Yes, these are beginner projects, but they show how even the basics of Python connect to real QA work:  
- Checking rules  
- Handling good vs. bad inputs
- Thinking about what happens after repeated failures

### 1. Mini Project 1: Login Validation  
- File: `login_validation.py`  
- A little script that simulates a login system.  
- It checks username + password and handles different scenarios: correct login, wrong username, wrong password, or empty fields.

### 2. Mini Project 2: Locked Account
-  File: `locked_account.py`  
- This one adds a lockout feature to the login script.  
- If the user logs in and fails 3 times, the account gets locked.

### 3. Mini Project 3: Validate Password
- File: `validate_password.py`  
- A script that checks if a password meets some common rules:  
  - at least 16 characters  
  - at least 1 number  
  - at least 1 special character  
- Just like the lockout script, users only get 3 tries. 

## What I Practiced Here  
- Writing Python with:  
  - variables  
  - input()  
  - if/else statements  
  - while loops  
  - for loops  
- Thinking like a QA tester with:  
  - positive test cases (valid input)  
  - negative test cases (wrong/missing input)  
  - edge cases (lockouts after too many attempts, enforcing password rules)
 
