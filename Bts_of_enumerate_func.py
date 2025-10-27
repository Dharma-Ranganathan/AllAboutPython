# import numpy
import numpy as np 

# data
data = np.random.randint(1,10,5)

# function creating 
def enumerate_(list_):
  i = 0
  while i < len(list_):
    yield i,list_[i]
    i += 1

# function call
for i,v in enumerate_(data):
  print(f'index : {i} • value : {v}') 

"""
output came :
[6,7,8,4,4]
index : 0 • value : 6
...
...
...
index : 4 • value : 4
"""
