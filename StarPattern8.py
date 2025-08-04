"""
output :

* 
* * 
* * * 
* * * *
* * * * * 
* * * * 
* * * 
* * 
*

"""
rows = 5
for i in range(1,10):
    if i < rows:
        for j in range(1,i+1):
            print("*",end=" ")
            continue
        print()
    if i >= rows:
        for j in range(0,rows):
            print("*",end=" ")
            continue
        print()
        rows-=1
