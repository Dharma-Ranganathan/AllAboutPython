"""
understanding zip functions

using zip function,we can zip a 2 or more grouped datas in single one.

any datatypes can be merged into single

- list
- dict
- tuple
- set

"""

# here the code to understand zip using list

names = ('dj','sp','vk')
ages = (22,22,23)
marks = (35,90,95)

zipped = zip(names,ages,marks)

print('zipped using list..')
print(list(zipped))
print()


names = ('dj','sp','vk')
ages = (22,22,23)
marks = (35,90,95)

zipped = zip(names,ages,marks)

print('zipped using tuple..')
print(tuple(zipped))
print()


names = ('dj','sp','vk')
marks = (35,90,95)

zipped = zip(names,marks)

print('zipped using dict..')
print(dict(zipped))
print()

names = ('dj','sp','vk')
ages = (22,22,23)
marks = (35,90,95)

zipped = zip(names,ages,marks)

print('zipped using set..')
print(set(zipped))
print()
