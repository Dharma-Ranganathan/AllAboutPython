"""
code to select every 10th element
and append in array then sum all.
"""

# Libraries 
import numpy as np

arr = np.random.randint(1,100,100)

# before 

print(f'before : {arr}')
print()

# after - getting all 10th element

sum_arr = []

x = 1
for i in arr:
    if x == 10:
        sum_arr.append(i)
        x = 1
    else:
        x+=1
        continue

print(f'sum_arr : {sum_arr}')
print()

# after - summing all 10th element

summate = 0

for i in sum_arr:
    summate += i
    
print(f'summate : {summate}')
