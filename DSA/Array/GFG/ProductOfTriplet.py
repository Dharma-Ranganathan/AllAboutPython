"""
Maximum product of a triplet (subsequence of size 3) in array

Given an integer array, find a maximum product of a triplet in the array.

Examples: 

Input:  arr[ ] = [10, 3, 5, 6, 20]
Output: 1200
Explanation: Multiplication of 10, 6 and 20

Input:  arr[ ] =  [-10, -3, -5, -6, -20]
Output: -90

Input: arr[ ] =  [1, -4, 3, -6, 7, 0]
Output: 21
"""

class Array:
    
    def __init__(self,array):
        self.array = array
    
    def product_of_triplet(self):
        self.array.sort()
        output = 1
        for i in range(-1,-4,-1):
            output *= self.array[i]
        return output
            
""" Test Cases """

arr1 = Array([1, -4, 3, -6, 7, 0])
output = arr1.product_of_triplet()
print(output)

arr2 = Array([-10, -3, -5, -6, -20])
output = arr2.product_of_triplet()
print(output)

arr3 = Array([10, 3, 5, 6, 20])
output = arr3.product_of_triplet()
print(output)
