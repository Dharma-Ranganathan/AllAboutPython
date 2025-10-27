# label encoding in a simple way

import numpy as np 

data = ['y','n','n','y']
data = np.asarray(data)

# label encoding 
label = np.where(data == 'y',1,0)
print(label)

# output came 
# [1,0,0,1]
