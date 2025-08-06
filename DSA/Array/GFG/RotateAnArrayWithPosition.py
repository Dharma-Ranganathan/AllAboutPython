""" 
Rotate an Array by d - Counterclockwise or Left

Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
Output: {3, 4, 5, 6, 1, 2}
Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

Input: arr[] = {1, 2, 3}, d = 4
Output: {2, 3, 1}
Explanation: The array is rotated as follows:

After first left rotation, arr[] = {2, 3, 1}
After second left rotation, arr[] = {3, 1, 2}
After third left rotation, arr[] = {1, 2, 3}
After fourth left rotation, arr[] = {2, 3, 1}
"""
class Array:
    def __init__(self,arr,d):
        self.arr = arr
        self.d = d
    
    def rotateAnArrayWithD(self):
        n = len(self.arr)
        self.d = self.d % n
        #print(self.d)
        
        # reversing first d elements
        self.reverseFrom(0,self.d-1)
        
        # reversing n-d elements
        self.reverseFrom(self.d,n-1)
        
        # reversing an entire array
        self.reverseFrom(0,n-1)
        
        return self.arr
    
    def reverseFrom(self,l,r):
        while l < r:
            self.arr[l],self.arr[r] = self.arr[r],self.arr[l]
            l += 1
            r -= 1
        
""" test cases """
            
arr1 = Array([1,2,3,4,5,6],2)
output = arr1.rotateAnArrayWithD()
print(output)

""" 
output :
[3, 4, 5, 6, 1, 2]
"""

arr2 = Array([1,2,3],4)
output = arr2.rotateAnArrayWithD()
print(output)

""" 
output :
[2, 3, 1]
"""
