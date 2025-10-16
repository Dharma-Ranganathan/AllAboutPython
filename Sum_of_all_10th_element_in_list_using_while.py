# code to select 10th element of list and sum all

# numpy
import numpy as np 

list_ = np.arange(1,101,1)

# all
print('before :')
print(list_)
print()

# while loop 
summate = 0
i = 1
while i <= 10 :
    summate += list_[i*10-1]
    i += 1

# after
print('sum of all 10th element :')
print(summate)
    
    
