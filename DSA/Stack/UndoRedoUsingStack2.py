"""
main objective : 
undo / redo using stack structure
"""
class UndoRedo:
    def __init__(self,stack):
        self.stack = stack
        
        ''' push actions '''
        self.push_undo = []
        self.push_redo = []
        
        ''' pull actions '''
        self.pull_undo = []
        self.pull_redo = []
    
    def push(self,e):
        self.stack.append(e)
        self.push_undo.append(e)
        
    def redoPush(self):
        if not self.push_redo:
            print("nothing to redo..")
            return
        pop = self.push_redo.pop(-1)
        self.stack.append(pop)
        self.push_undo.append(pop)
    
    def undoPush(self):
        if not self.push_undo:
            print("nothing to undo..")
            return
        self.stack.pop(-1)
        pop = self.push_undo.pop(-1)
        self.push_redo.append(pop)
        
    
    def pull(self):
        if not self.stack:
            print("nothing to pull..")
            return
        pop = self.stack.pop(-1)
        self.pull_redo.append(pop)
        
    def redoPull(self):
        if not self.pull_redo:
            print("nothing to redo..")
            return
        pop = self.pull_redo.pop(-1)
        self.stack.append(pop)
        self.pull_undo.append(pop)
    
    def undoPull(self):
        if not self.pull_undo:
            print("nothing to undo..")
            return
        pop = self.pull_undo.pop(-1)
        self.stack.pop(-1)
        self.pull_redo.append(pop)
    
    def print(self):
        stack = ""
        if not self.stack:
            stack += 'is empty...'
        stack += " • ".join(map(str,self.stack))
        print('stack :',stack)
        

# initiating object for class
s1 = UndoRedo([])
s1.push(1)
s1.push("a")
s1.push(3)
s1.push("b")
s1.print()
s1.undoPush()
s1.print()
s1.undoPush()
s1.print()
s1.redoPush()
s1.print()
s1.redoPush()
s1.print()
s1.redoPush()
s1.pull()
s1.print()
s1.redoPull()
s1.print()
s1.undoPull()
s1.print()
s1.undoPull()
s1.print()

"""
completely analyzed the test cases...
"""
