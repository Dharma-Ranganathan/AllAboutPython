# main objective : FIFO

class Queue:
    def __init__(self,queue):
        self.queue = queue
        
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) ==0
    
    def enqueue(self,e):
        self.queue.append(e)
        
    def dequeue(self):
        if self.isEmpty():
            print("cannot dequeue an element as queue is empty...")
            return
        self.queue.pop(0)
    
    def printQueue(self):
        queue = " => ".join(map(str,self.queue))
        print("Queue : ",queue)
        
# initiating object

queue1 = Queue([9,7,5,3,1])
queue1.printQueue()
size = queue1.size()
print(size)
queue1.dequeue()
queue1.dequeue()
queue1.printQueue()
size = queue1.size()
print(size)
print(queue1.isEmpty())
queue1.enqueue(8)
queue1.printQueue()
