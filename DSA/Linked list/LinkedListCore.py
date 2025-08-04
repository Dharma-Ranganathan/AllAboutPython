"""
understanding linked list data structure
"""

""" creating Node class """

class Node :
    def __init__(self,data):
        self.data = data
        self.pointer = None

""" creating Linked List class """

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    """ appending a data """
    
    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.length += 1
        
        else:
            current = self.head
            while current.pointer != None:
                current = current.pointer
            
            current.pointer = node
            
            self.length += 1
    
    """ prepending a data """
    
    def prepend(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.length += 1
        else:
            current = self.head
            node.pointer = current
            self.head = node
            self.length += 1
    
    """ search a given data """
    
    def search(self,data):
        if self.head != None:
            current = self.head
            index = 0
            while current != None and current.data != data:
                index += 1
                current = current.pointer
            
            if current == None:
                print("searched : No such data found")
                return
            
            if current.data == data:
                print(f"searched : {data} found at {index} index")
                return
        else:
            print("cannot search in linked list as it is empty")
    
    """ insert a data at given index """
    
    def insert(self,pos,data):
        if pos > self.length - 1:
            print("index out of range",pos)
            return
        node = Node(data)
        if self.head == None:
            self.head = node
            self.length += 1
        else:
            index = 0
            current = self.head
            
            if pos == 0:
                node.pointer = self.head
                self.head = node
                self.length += 1
                return
            
            while index != pos-1: 
                index += 1
                current = current.pointer
            node.pointer = current.pointer
            current.pointer = node
            self.length += 1
            
    """ remove a data """
    
    def remove(self,data):
        if self.head == None:
            print("list is empty, nothing to remove")
        else:
            if self.head.data == data:
                self.head = self.head.pointer
                self.length -= 1
                return
            current = self.head
            while current != None and current.pointer.data != data:
                current = current.pointer
            if current == None:
                print("No such data to remove")
                return
            current.pointer = current.pointer.pointer
            self.length -= 1
            
            
    """ printing a linked list """
    
    def print(self):
        if self.head != None:
            print("list len : ",self.length)
            current = self.head
            while current != None:
                print(current.data,end=" => ")
                current = current.pointer
            
        else :
            print("Linked List is empty")
            
            
            
ll1 = LinkedList()
ll1.append(4)
ll1.insert(0,5)
ll1.prepend(7)
ll1.insert(2,6)
ll1.insert(3,True)
ll1.remove(7)
ll1.remove(6)
ll1.remove(True)
ll1.insert(1,333)
ll1.append(456)
ll1.search(5)
ll1.search(True)
ll1.print()


"""
outcome :-

searched : 5 found at 0 index
searched : No such data found
list len :  4
5 => 333 => 4 => 456 => 
"""
