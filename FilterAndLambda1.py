"""
understanding filter and lamba

filter the std with id between 5 to 7
"""

stds = [
    (5,"dj",90),
    (3,"vk",95),
    (7,"vj",99),
    (6,"sp",100)
    ]
    
fun = lambda std : std[0] >= 5 and std[0] <= 7
filteredIds = list(filter(fun,stds))

print(filteredIds)
