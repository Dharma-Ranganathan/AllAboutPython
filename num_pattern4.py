"""
number pattern - 4

01010
01010
01010
01010
01010

"""
# here are codes to achieve this using for loops

for i in range(1,6):
    for j in range(1,6):
        if j%2 == 0:
            print(1,end="")
            continue
        print(0,end="")
    print()
