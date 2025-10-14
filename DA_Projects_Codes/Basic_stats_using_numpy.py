print("simple statistics calculation...")
"""
utilised numpy
string methods
functions
loops
libraries - numpy

used time module for real time 
experience...
"""

# imported numpy
import numpy as np
import time as t

def findStats():
    arr = np.array([])
    print()
    # getting inputs from user for 10 times using for loop
    for i in range(1,6):
        num = int(input(f"{i} num to add in array : "))
        arr = np.append(arr,num)
    mean = np.mean(arr)
    median = np.median(arr)
    var = np.var(arr)
    stdDev = np.std(arr)
    
    return mean,median,var,stdDev
        
    

while True:
    print()
    print("1.mean,median,var,std dev for an array")
    print("2.quit")
    print()
    ch = str(input("enter choice : ")).strip()
    
    if ch.isalpha():
        print("choice cann't be characters...")
        break
    if ch == "1":
        # destructured variables
        mean,median,var,stdDev=findStats()
        
        # delay time 
        print()
        print("please wait...")
        print("calculating your inputs...")
        t.sleep(3)
        
        print()
        print(f"Mean of given array : {mean:.2f}")
        print(f"Median of given array : {median:.2f}")
        print(f"Variance of given array : {var:.2f}")
        print(f"Standard Deviation of given array : {stdDev:.2f}")
    elif ch == "2":
        print("quitting the program....")
        break
