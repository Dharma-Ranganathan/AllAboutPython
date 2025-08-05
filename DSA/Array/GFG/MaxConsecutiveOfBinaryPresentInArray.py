"""
Maximum consecutive one’s (or zeros) in a binary array

Given a binary array arr[] consisting of only 0s and 1s, find the length of the longest contiguous sequence of either 1s or 0s in the array.

Examples : 

Input: arr[] = [0, 1, 0, 1, 1, 1, 1]
Output: 4
Explanation: The maximum number of consecutive 1’s in the array is 4 from index 3-6.

Input: arr[] = [0, 0, 1, 0, 1, 0]
Output: 2
Explanation: The maximum number of consecutive 0’s in the array is 2 from index 0-1.

Input: arr[] = [0, 0, 0, 0]
Output: 4
Explanation: The maximum number of consecutive 0’s in the array is 4.
"""

class Array:
    
    def __init__(self,arr):
        self.arr = arr
    
    def max_cons01(self):
        prev = None
        cons = 1
        index = ""
        for i in range(len(self.arr)):
            if prev == None:
                prev = self.arr[i]
                continue
            if self.arr[i] != prev:
                prev = self.arr[i]
                continue
            index += str(i-1)
            if self.arr[i] == prev:
                cons += 1
                index += str(i)
        return f"{prev} consecutively present from {index[0]} to {index[-1]} for {cons} times"

""" Test cases """

# test case 1

arr1 = Array([0, 1, 0, 1, 1, 1, 1])
output = arr1.max_cons01()
print(output)

""" 
output came :

1 consecutively present from 3 to 6 for 4 times
"""

# test case 2

arr2 = Array([0, 0, 1, 0, 1, 0])
output = arr2.max_cons01()
print(output)

"""
output came :

0 consecutively present from 0 to 1 for 2 times
"""

# test case 3

arr3 = Array([0, 0, 0, 0])
output = arr3.max_cons01()
print(output)

"""
output came :

0 consecutively present from 0 to 3 for 4 times
"""
