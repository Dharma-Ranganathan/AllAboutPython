"""

DSA Array problem 1 :-

Third largest element in an array of distinct elements

Given an array of n integers, the task is to find the third largest element. All the elements in the array are distinct integers. 

Examples : 

Input: arr[] = {1, 14, 2, 16, 10, 20}
Output: 14
Explanation: Largest element is 20, second largest element is 16 and third largest element is 14

Input: arr[] = {19, -10, 20, 14, 2, 16, 10}
Output: 16
Explanation: Largest element is 20, second largest element is 19 and third largest element is 16 
"""

class Array:
    
    def __init__(self,array):
        self.array = array
        self.n = len(array)
    
    def getThirdLargest(self):
        self.array.sort()
        
        for i in range(self.n - 3,-1,-1):
            if self.array[i] != self.array[self.n-1]:
                return self.array[i]
        return -1
    
    def getSecondLargest(self):
        self.array.sort()
        
        for i in range(self.n - 2,-1,-1):
            if self.array[i] != self.array[self.n-1]:
                return self.array[i]
        return -1
    
    
array1 = Array([1, 14, 2, 16, 18,10, 20])
third = array1.getThirdLargest()
second = array1.getSecondLargest()
print(third,second,sep='\n')
