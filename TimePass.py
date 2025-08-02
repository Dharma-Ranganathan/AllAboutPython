"""
form filling using python loops

time passing code..
"""
import re

email= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

forms = [
    "name",
    "age",
    "email",
    "phno",
    "city"
    ]
    
datas = {}

for i in range(len(forms)):
    value = input(f"{forms[i]} : ").lower()
    datas[forms[i]] = value
    
if datas["age"].isalpha():
    print("Age cannot be letters..")
    
elif not re.fullmatch(email,datas["email"]):
    print("Invalid Email Input..")

elif len(datas["phno"]) != 10 or datas["phno"].isalpha():
    print("Phone number cannot be alphabets / less or more than ten..")
else:
    yn = input("do you want to submit application ? y/n : ").lower()
    if yn != "y" and yn != "n":
        print("Invalid selection..")
    
    if yn == "n":
        print("Form not submitted..")
    else:
        print("Form submitted..")
