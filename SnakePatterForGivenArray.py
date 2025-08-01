"""
snake patter in 2d matrix

output :
[[1,2,3],
[6,5,4],
[7,8,9]]

in 'given' array, i have added one more list to cross verify this patter.
"""
given = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
    ]
snake = []
""" actual code to achieve snake pattern """
for i in range(len(given)):
    if i%2 != 0:
        n = len(given[i]) - 1
        snake.append([given[i][x] for x in range(n,-1,-1)])
        continue
    snake.append(given[i])

""" show casing """
print("initial pattern")
for g in given:
    print(g)
print()
print("snake pattern")
for s in snake:
    print(s)
