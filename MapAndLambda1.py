"""
understanding map and lamba 

making a new list contains only name and marks
"""

stds = [(123,"dj",35),(124,"sp",49),(125,"vk",50)]

name_marks = list(map(lambda std:(std[1],std[2]),stds))
print(name_marks)
