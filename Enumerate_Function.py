import numpy as np 

data = np.random.randint(1,100,5)

print(data)

# i for index and x for value access
# using enumerate function, we can access both index and values at same time 
for i,x in enumerate(data):
    print(f'index : {i} • value : {x}')

"""
output came :

[89 26 55 35 13]
index : 0 • value : 89
index : 1 • value : 26
index : 2 • value : 55
index : 3 • value : 35
index : 4 • value : 13

"""
