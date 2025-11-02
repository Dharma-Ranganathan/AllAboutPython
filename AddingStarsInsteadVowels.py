"""

let us consider a string 'tomorrow'

vowel letters in tomorrow string
should be printed as stars with
respect to no of occurence

input = 'TOMORROW'
vowels in input -> three O's

appending star in output could be
the count of each time each vowel
occurence 

output = T*M**RR***W

"""

string = 'TOMORROW'

vowels = ['a','e','i','o','u']

occur = 0

result = ''

for i in string:
    if i.lower() in vowels:
        occur += 1
        for j in range(occur):
            result += "*"
    else:
        result += i


print(result)
