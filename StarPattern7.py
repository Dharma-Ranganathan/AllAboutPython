"""
output :

*
* * 
* * * 
* * * * 
* * * * *

* * * * * 
* * * * 
* * *
* * 
*

"""
row = 5
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
print()
for i in range(0,5):
    for j in range(0,5):
        if j <row:
            print("*",end=" ")
            continue
        print(" ",end=" ")
    print()
    row -= 1
