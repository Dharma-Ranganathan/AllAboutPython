
"""
number pattern - 5

11111
10001
10001
10001
11111

"""
# here are codes to achieve this using for loops

for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 5:
            print(1,end='')
            continue
        if j == 1 or j == 5:
            print(1,end='')
            continue
        print(0,end='')
    print()
