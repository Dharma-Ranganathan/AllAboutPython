"""
output :

            *
         *  *
      *  *  *
   *  *  *  *
*  *  *  *  *
   *  *  *  *
      *  *  *
         *  *
            *
"""
rows = 5
lap = 5
for i in range(1,10):
    if i < lap:
        # rows = 5
        for j in range(1,lap+1):
            if j < rows:
                print(" ",end=" ")
                continue
            print("*",end=" ")
        print()
        rows -= 1
    if i >= lap:
        # rows = 1
        for j in range(1,lap+1):
            if j >= rows:
                print("*",end=" ")
                continue
            print(" ",end=" ")
        print()
        rows += 1
