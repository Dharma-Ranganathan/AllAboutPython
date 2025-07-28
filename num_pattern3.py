"""
number pattern - 3

11111
00000
11111
00000
11111

"""
# here are code to achieve this using for loops

for i in range(1,6):
    for j in range(1,6):
        if i%2 == 0:
            print(0,end='')
            continue
        print(1,end='')
    print()
