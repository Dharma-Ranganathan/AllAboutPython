"""
LEETCODE 

question : 

given two arrays arr1 and arr2, the arr2 are distinct and arr1 contains all elements as in arr2.

sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.

elements that don't appear in arr2 should be placed at the end of an arr1 in ascending order.

EXAMPLE 1 :

input : 
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

ouput : [2,2,2,1,4,3,3,9,6,7,19]
"""

class NumSort:
    
    def sort(self,a1,a2):
        result = []
        for i in a2:
            for j in a1:
                if i == j:
                    result.append(j)
                continue
        asc = []     
        for a in a1:
            if a not in result:
                asc.append(a)
            continue
                
        asc.sort()
        for e in asc:
            result.append(e)
            
        return result



arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

numSort = NumSort()
sortedArr = numSort.sort(arr1,arr2)
print(sortedArr)
