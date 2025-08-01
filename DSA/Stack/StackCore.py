# main objective : FILO / LIFO

class Stack:
    def __init__(self,stack):
        self.stack = stack
        
    def size(self):
        return len(self.stack)
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if self.isEmpty():
            print("cannot pop elements as stack is empty...")
            return
        self.stack.pop(self.size() - 1)
        
    def append(self,e):
        self.stack.append(e)
    
    def printStack(self):
        stack = " => ".join(map(str,self.stack))
        print("stack : ",stack)
    
# initiating with object

stack1 = Stack([1,2,3,4,5])
stack1.printStack()
stack1.pop()
stack1.printStack()
size = stack1.size()
print(size)
stack1.append(6)
stack1.printStack()
size = stack1.size()
print(size)
