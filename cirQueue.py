class cirQue:
    def __init__(self,n=4):
        self.maxsize=n
        self.queue=[None]*self.maxsize
        self.front=0
        self.rear=0
        
        
    def enQueue(self,x):
        if not self.full():
            self.queue[self.rear]=x
            self.rear=(self.rear+1)%self.maxsize
        else:
            print( 'full')
            return False
            
    def full(self):
        return self.front==(self.rear+1)%self.maxsize
    
    def empty(self):
        return self.front==self.rear
    
    def delQueue(self):
        if self.empty():
            return False
        data=self.queue[self.front]
        self.queue[self.front]=None
        self.front=(self.front+1)%self.maxsize
        return data
    
    def getQueue(self):
        return self.queue[self.front]
    
    def showQueue(self):
        return self.queue
    
def test():
    q=cirQue(5)
    arr='abcd'
    for i in arr:
        q.enQueue(i)
    print(q.showQueue())
    for i in range(4):
        q.delQueue()
    print(q.front,q.rear)
    print(q.showQueue())
    q.enQueue('e')
    q.enQueue('f')
    q.enQueue('g')
    print(q.showQueue())
        
test()
        
        
    
    
            