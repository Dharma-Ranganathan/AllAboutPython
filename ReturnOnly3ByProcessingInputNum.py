"""
input any number but return 3 anyway
by just processing the input number
itself.

EXM : 1

input = 10
processing some operations with
input...
output = 3

EXM : 2

input = 87
processing some operations with
input...
output = 3
"""

# get number from user
def getNum():
    
    num = input('enter a number : ').strip()
    
    if num.isnumeric():
        return num
    else:
        print('invalid credentials')
        
# process the input and return 3
def processNum(num):
    
    num = int(num)
    
    if num == 3:
        return num
    
    elif num > 3:
        pro = num + 3
        return pro - num
    
    elif num < 3:
        loss = num - 3
        return num - loss
    
    else:
        return None
        
    
# result 
num = getNum()
result = processNum(num)
print(f'processed the input : {num} to return {result}')
