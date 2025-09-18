"""
Utilized 
String Methods, 
while loops, 
modules and packages 
(json,datetime,time),
error handled...
"""

# imports
import time as t
import datetime as dt
import json as js


# title
print("User Management System")
print("Implemented time module for realtime experience")
print()

# users list - global
users = []

# function for registration 
def register():
    acc = {}
    username = str(input("Username : ")).lower().strip()
    email = input("Email : ").strip()
    createdAt = dt.date.today()
    
    acc['username']=username
    acc['email']=email
    acc['createdAt']=str(createdAt)
    user = js.dumps(acc)
    users.append(user)
    t.sleep(1)
    print()
    print("✓ Registered Account Successfully...")

# function for login
def login():
    email = input("Email to login : ").strip()
    
    i = 0
    while i < len(users):
        user = js.loads(users[i])
        if user['email'] == email:
            t.sleep(1)
            print()
            print("checking database...")
            t.sleep(2)
            print("✓ Logged In successfully...")
        else:
            print()
            print("Invalid credentials...")
        i += 1
        

# function for logout
def logout():
    print("""NOTE : 
If you logout now, you account
details also be deleted...
    """)
    email = input("Email to Logout : ").strip()
    i = 0
    while i < len(users):
        user = js.loads(users[i])
        if user['email'] == email:
            users.remove(users[i])
            t.sleep(2)
            print("✓ Logged Out Successfully...")
        else:
            print("No such account in database...")
        i+=1
        
# function for getting all users
def getUsers():
    if len(users) == 0:
        t.sleep(1)
        print()
        print("No Accounts were registered yet...")
        return
    i = 0
    while i<len(users):
        print(f"{i+1} • {users[i]}")
        i += 1
    return

# while loop
while True:
    print()
    print("1. Register Account")
    print("2. Login Account")
    print("3. Logout")
    print("4. Get Users")
    print("5. Quit")
    print()
    
    # strip and lower applied
    ch = input("Enter choice :").lower().strip()
    
    # check if alphabets given
    if ch.isalpha():
        print("Cannot be characters...")
        break

    if ch == "1":
        print()
        print("Register Your Account here...")
        t.sleep(2)
        register()
        
    elif ch == "2":
        print()
        print("Login here...")
        t.sleep(2)
        login()
        
    elif ch == "3":
        print()
        print("logging out...")
        t.sleep(2)
        logout()
        
    elif ch == "4":
        print()
        print("Getting All Users from Database...")
        t.sleep(2)
        getUsers()
        
    elif ch == "5":
        print("Quitting the program...")
        t.sleep(2)
        break
    
    else:
        print()
        print("Invalid choice selection...")
        t.sleep(1)
        print("Re-run if you want to try again...")
        t.sleep(1)
        break

        
        
        

        
        
