"""
output :
 
        *
      * * *
    * * * * *
  * * * * * * * 
* * * * * * * * * 
"""
l = 4
r = 6
for i in range(0,5):
    for j in range(1,10):
        if j>l and j<r:
            print("*",end=" ")
            continue
        print(" ",end=" ")
    print()
    l -= 1
    r += 1
