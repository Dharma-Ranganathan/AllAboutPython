"""
output :

* * * * *
* * * * 
* * * 
* * 
*
"""

n = 5
rows = 5
for i in range(0,n):
    for j in range(1,n+1):
        if j <= rows:
            print("*",end=" ")
            continue
        print(" ",end=" ")
    print()
    rows -= 1
