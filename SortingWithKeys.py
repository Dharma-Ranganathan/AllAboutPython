"""
understanding sorting with keys in list of tuples.
"""
students = [
    ("maths","anitha",80),
    ("biology","anand",82),
    ("biology","balaji",70),
    ("maths","chandru",90)
    ]

# sorting students by subjects
students.sort(key=lambda student:student[0])
print(students)

# sorting students by name
students.sort(key=lambda student:student[1])
print(students)

# sorting students by marks
students.sort(key=lambda student:student[2])
print(students)

# sorting students with mark but desc to asec
students.sort(key=lambda student:student[2],reverse=True)
print(students)
