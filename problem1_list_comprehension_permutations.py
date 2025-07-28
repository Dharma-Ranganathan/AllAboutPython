"""
You are given three integers x,y,and z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
Here, Please use list comprehensions rather than multiple loops, as a learning exercise.

Example :

x=1
y=1
z=2
n=3

All Permutations of [i,j,k] are,
[[0,0,0],[0,0,1],[0,0,2],....] if any nested lists that sum to n=3 given,remove an array.

print the list in lexicographic increasing order.

sample input:
x=1
y=1
z=1
n=2

sample output:
[[0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,1,1]]

none of the nested lists have sum to n=2 given. if its,error.

"""

if __name__ == "__main__":

    x = int(input("x : "))
    y = int(input("y : "))
    z = int(input("z : "))
    n = int(input("n : "))
    permutations = []

    def construct_nest(arr):
        value = 0
        for val in arr:
            value += val
        if value == n:
            return
        else:
            permutations.append(arr)


    list1 = [z for z in range(z+1)]
    list2 = [x for x in range(x+1)]
    list3 = [y for y in range(y+1)]

    # print(list1, list2, list3)

    for i in range(len(list1)):
        for j in range(len(list2)):
            for k in range(len(list3)):
                construct_nest([i, j, k])

    print(permutations)