'''
Given an integer n.
n space-separated integers as input,
create a tuple t, of those n integers.
Then compute and print the result of hash(t).

Note : hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input :
The first line contains an integer,n,denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.

Output:
Print the result of hash(t).

Sample Input:
n = 2
n = 1 2

Sample Output:
3713081631934410656

'''

if __name__ == "__main__":
    n = int(input("N : "))

    integer_list = tuple(map(int, input("List : ").split()))

    print(hash(integer_list)) #output : -3550055125485641917

    # python below versions (3.x) giving the expected outputs.
    # output : 3713081631934410656
    # In below 3.x versions, I am getting expected output as given
