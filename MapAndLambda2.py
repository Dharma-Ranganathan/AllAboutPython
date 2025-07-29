"""
understanding map and lambda

making a new list contains even and odd relevant to given number array
"""

val = [2,6,5,8,3,1]

odd_even = list(map(lambda v : "even" if v%2 == 0 else "odd", val))

print(odd_even)
