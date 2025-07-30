"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.

Example :
Pythonist 2 ==> pYTHONIST 2

Function Description:
Complete the swap_case function in the editor below.

swap_case has the following params.
* string s: the string to modify.

returns
* string: the modified string.

Input format : A single line containing a string s.

Sample Input : HackerRank.com presents "Pythonist 2"
Sample Output : hACKERrANK.COM PRESENTS "pYTHONIST 2"

"""

def swap_case(s):
   return s.swapcase()


if __name__ == "__main__":

    s = input("s: ")

    result = swap_case(s)

    print(result)
