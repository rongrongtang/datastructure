class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
    def __str__(self):
        return str(self.data)
    
class QueueLink:
    def __init__(self):
        self.head=self.rear=Node()
        
    def enQueue(self,x):
        node=Node(x)
        if self.empty():
            self.head.next=node
        self.rear.next=node
        self.rear=node               
            
    def delQueue(self):
        if self.empty():
            return None
        p=self.head.next
        if not p.next:
            self.rear=self.head
        self.head.next=p.next
        return p
    
    def getHead(self):
        if self.empty():
            return None
        return self.head.next
    
    def empty(self):
        return self.head==self.rear
    
def test():
    s=QueueLink()
    for i in range(1,6):
        s.enQueue(i)
    
  
    while(not s.empty()):
        #print(s.getHead())
        print(s.delQueue())
#         
test()    