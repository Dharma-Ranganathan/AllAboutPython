
"""
number pattern - 8

11011
11011
00000
11011
11011

"""

# here are codes to achieve this using for loops

for i in range(1,6):
    for j in range(1,6):
        if i == 3 or j == 3:
            print(0,end='')
            continue
        print(1,end='')
    print()
