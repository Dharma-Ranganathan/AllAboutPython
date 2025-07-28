"""
number pattern - 7

10101
01010
10101
01010
10101

"""

# here are codes to achieve this using for loops

for i in range(1,6):
    for j in range(1,6):
        if i%2 != 0:
            if j%2 != 0:
                print(1,end='')
                continue
            print(0,end='')
            continue
        if i%2 == 0:
            if j%2 == 0:
                print(1,end='')
                continue
            print(0,end='')
            continue
    print()
