"""
Reverse an Array in groups of given size

Given an array arr[] and an integer k, find the array after reversing every subarray of consecutive k elements in place. If the last subarray has fewer than k elements, reverse it as it is. Modify the array in place, do not return anything.

Examples: 

Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], k = 3
Output: [3, 2, 1, 6, 5, 4, 8, 7]
Explanation: Elements is reversed: [1, 2, 3] → [3, 2, 1], [4, 5, 6] → [6, 5, 4], and the last group [7, 8](size < 3) is reversed as [8, 7]. 

Input: arr[] = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4, 5.

Input: arr[] = [5, 6, 8, 9], k = 5
Output: [9, 8, 6, 5]
Explanation: Since k is greater than array size, the entire array is reversed.
"""

class Array:
    
    def __init__(self,arr,k):
        self.arr = arr
        self.k = k
        
    def reverseAnArrayWithSize(self):
        n = len(self.arr)
        
        i = 0
        while i < n:
            l = i # 0 
            r = min(i+self.k-1,n-1)
            # r = 3 
            
            while l < r: # 0 < 3
                self.arr[l],self.arr[r] = self.arr[r],self.arr[l]
                l += 1
                r -= 1
                
            i += self.k # 5 loop breaks since i > n
        return self.arr
        
""" Test Cases """

# test case 1

# k = 3 size
arr1 = Array([1, 2, 3, 4, 5, 6, 7, 8],3)
output = arr1.reverseAnArrayWithSize()
print(output)
"""
output :

[3, 2, 1, 6, 5, 4, 8, 7]
"""

# test case 2

# k = 3 size
arr2 = Array([1, 2, 3, 4, 5],3)
output = arr2.reverseAnArrayWithSize()
print(output)
"""
output :

[3, 2, 1, 5, 4]
"""

# test case 3

# k = 5 size
arr3 = Array([5, 6, 8, 9],5)
output = arr3.reverseAnArrayWithSize()
print(output)
"""
output :

[9, 8, 6, 5]
"""
