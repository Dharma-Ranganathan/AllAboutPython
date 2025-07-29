"""
generating prime numbers
"""

num = input("enter range : ")
if num.isalpha():
    print("letters and characters not be allowed")
if num.isnumeric():
    num = int(num)
    prime = (num*num) + num + 1
    print(prime)
