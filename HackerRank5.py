"""
In python, a string can be split on a delimiter.

Example :

SPLITTING THE STRING
--------------------
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings based on "space" delimiter
# >>> print(a)
["this","is","a","string"]

JOINING THE STRING
------------------
# >>> a = "-".join(a)
# >>> print(a)

this-is-a-string

Task:
You are gicen a string. Split the string on a " " ((space)) delimiter and
join using a "-" hyphen.

Function Description:
complete the split_and_join function in the editor below.

split_and_join has the following parameters:
* string line: a string of space_separated words.

returns:
* string: the resulting string.
"""

def split_and_join(line):
    modified = line.split(" ")
    return "-".join(modified)

if __name__ == "__main__":
    line = input("line : ")
    result = split_and_join(line)
    print(result)
