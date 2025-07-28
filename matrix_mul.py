first = [[1,2,3],[4,5,6],[7,8,9]]
second = [[1,2,3],[4,5,6],[7,8,9]]

# matrix multiplication...

for i in range(len(first)):
    for j in range(len(second)):
        second[i][j] = second[i][j] * first[i][j]

for arr in second:
    print(arr)