class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
    def __str__(self):
        return str(self.data)

class LinkList:
    def __init__(self):
        self.head=self.rear=Node()
    def add(self,num):
        node=Node(num)
        self.rear.next=node
        self.rear=node
    def show(self):
        current=self.head.next
        while(current):
            print(current)
            current=current.next            
                    
    def searchI(self,i):
        j=0
        current=self.head.next
        while(current):
            j+=1
            if j==i:
                return current
            else:
                current=current.next
        return False
    
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
    
def test():
    a=list(i for i in range(1,11))
    h=LinkList()
    for n in a:
        h.add(n)
    h.show()
    print(h.searchE(10))
    print(h.insertI(1,11))
    h.show()
    
test()
            
        