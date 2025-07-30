"""
understanding DSA 1 - stack

by understanding the data structure of stack, I've designed this small project.

- stack is a realtime data structure which is used in many ways.

realtime :

* google history managing (like back and forth history shifting)

* undo/redo like etc...

"""

from collections import deque

print("available images...")
images = "img1 • img • img3 • img4 • img5"
print(images)
print()

stackLeft = deque(["img1","img2","img3","img4"])

stackRight = deque(["img5"])


def showImg(img):
    print("displaying :",img)

showImg(stackRight[-1])

def msg(msg):
    print("alert message :",msg)

# scrollLeft

def scroll_left():
    if stackLeft[-1] == "img1":
        currImg = stackLeft[-1]
        showImg(currImg)
        msg("no more images on left")
        return
    
    popped = stackLeft.pop()
    stackRight.append(popped)
    showImg(popped)

# scrollRight

def scroll_right():
    if stackRight[-1] == "img5":
        currImg = stackRight[-1]
        showImg(currImg)
        msg("no more images on right")
        return
    
    popped = stackRight.pop()
    stackLeft.append(popped)
    showImg(popped)

    

while True:
    print(
"""
"<" to scroll left
">" to scroll right
"x" to exit
"""
)

    choice = input("enter choice : ").lower()
    if choice.isnumeric():
        print("numbers not applicable...")
        continue
    if choice == "<":
        scroll_left()
    elif choice == ">":
        scroll_right()
    elif choice == "x":
        print("come back again...")
        break
    else:
        print("invalid choice selection")
        continue
