
"""
number pattern - 6

11111
11111
11011
11111
11111

"""

# here are codes to achieve this using for loops

for i in range(1,6):
    for j in range(1,6):
        if i == 3 and j == 3:
            print(0,end='')
            continue
        print(1,end='')
    print()
