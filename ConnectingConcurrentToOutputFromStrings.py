"""
connecting concurrent strings of s1 and s2 to output 
"""
# returns min length str 
def returnMin(s1,s2):
    if len(s1) < len(s2):
        return [s1,"s1"]
    return [s2,"s2"]

s1 = "dharma"
s2 = "ranganathan"
minStr = returnMin(s1,s2)
output = ""

i = 0
while i < len(minStr[0]):
    output += s1[i] + s2[i]
    i += 1

if minStr[1] == 's2':
    output += s1[i:]
else:
    output += s2[i:]
    
print(output)
