"""
code to select every 10th element
and then sum all.
"""

# Libraries 
import numpy as np

arr = np.random.randint(1,100,100)

# before 

print(f'before : {arr}')
print()

# after - getting all 10th element

sum_arr = 0

x = 1
for i in arr:
    if x == 10:
        sum_arr += i
        x = 1
    else:
        x+=1
        continue

print(f'sum_arr : {sum_arr}')
print()



