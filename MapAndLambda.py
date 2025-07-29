"""
understanding of map and lambda

converting fahrenheit list to celcius list
"""

fahren = [100,101,102,103,104,105]

celcius = list(map(lambda f : float("{:.2f}".format((f-32)*(5/9))),fahren))
print(celcius)
