# behind the scenes of enumerate function 

# numpy
import numpy as np 

# data
data = np.random.randint(1,10,5)
print(data)

# function creating 
def enumerate_(list_):
    i = 0
    while i < len(list_):
        yield i,list_[i]
        i += 1
        
# function call
for i , v in enumerate_(data):
    print(f'index : {i} • value : {v}')
    
"""
output came :

[8 8 8 4 2]
index : 0 • value : 8
index : 1 • value : 8
index : 2 • value : 8
index : 3 • value : 4
index : 4 • value : 2
"""



