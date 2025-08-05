"""
Move all zeros to end of array

Given an array of integers arr[], the task is to move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

Examples: 

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: arr[] = [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: arr[] = [0, 0]
Explanation: No change in array as there are all 0s.
"""

class Array:
    
    def __init__(self,arr):
        self.arr = arr
        
    def moveAllZeroesToEnd(self):
        for i in range(len(self.arr)):
            if self.arr[i] == 0:
                popped = self.arr.pop(i)
                self.arr.append(popped)
                continue
        return self.arr

""" Test Cases """

# test case 1

arr1 = Array([1, 2, 0, 4, 3, 0, 5, 0])
output = arr1.moveAllZeroesToEnd()
print(output)

"""
output :
[1, 2, 4, 3, 5, 0, 0, 0]
"""

# test case 2

arr2 = Array([10, 20, 30])
output = arr2.moveAllZeroesToEnd()
print(output)

"""
output :
[10, 20, 30]
"""

# test case 3

arr2 = Array([0, 0])
output = arr2.moveAllZeroesToEnd()
print(output)

"""
output :
[0, 0]
"""
