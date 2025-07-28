
"""
number pattern - 9

10001
01010
00100
01010
10001

"""

# here are codes to achieve this using for loops

for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5:
            if j==1 or j==5:
                print(1,end='')
                continue
            print(0,end='')
            continue
        if i%2 == 0:
            if j%2==0:
                print(1,end='')
                continue
            print(0,end='')
            continue
        if i==3:
            if j==3:
                print(1,end='')
                continue
            print(0,end='')
            continue
    print()
