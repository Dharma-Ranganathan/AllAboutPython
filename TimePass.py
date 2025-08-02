"""
form filling using python loops

time passing code..
"""

forms = [
    "name : ",
    "age : ",
    "email : ",
    "phno : ",
    "city : ",
    ]

datas = {}
for i in range(len(forms)):
    value = input(forms[i])
    datas[forms[i]] = value
    
print(datas)
