class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
    def __str__(self):
        return str(self.data)

class LinkList:
    def __init__(self):
        self.head=self.rear=Node()
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.head.next:
            raise StopIteration
        self.head=self.head.next
        return self.head.data
    
    def add(self,num):
        node=Node(num)
        self.rear.next=node
        self.rear=node
        
    def searchE(self,e):
        current=self.head.next
        while(current):
            if current.data==e:
                return current
            current=current.next
        return False
    
    def insertI(self,i,data):
        s=Node(data)        
        if i==1:
            p=self.head
        else:
            p=self.searchI(i-1)        
        if not p:
            return False
        s.next=p.next
        p.next=s
        return True
    
    def show(self):
        current=self.head.next
        while(current):
            print(str(current.data)+'->',end=' ')
            current=current.next
        print('\n')
            
def delRepeat(linklist1):
    link=LinkList()
    for data in linklist1:
        if not link.searchE(data):
            link.add(data)
    return link
        
        
    
def test():
    nums=[1,2,2,3,1,4]
    link1=LinkList()
    for n in nums:
        link1.add(n)
    link1.show()
    link2=delRepeat(link1)
    link2.show()
    
test()
        
    