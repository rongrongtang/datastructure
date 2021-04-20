class Node:
    def __init__(self,data=None):
        self.data=data
        
    def __str__(self):
        return str(self.data)
    
class LinkList:
    def __init__(self):
        self.head=self.rear=None
        
    def add(self,num):
        node=Node(num)
        if not self.head:
            self.head=self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        self.rear.next=self.head
        
    def show(self):
        if not self.head:
            print(None)
        elif self.head==self.rear:
            print(self.head)
        else:
            current=self.head
            while(current!=self.rear):
                print(current)
                current=current.next
            print(self.rear)
    
  
            
def delI(current,i):
    """delete the ith node after current node,i>=1,reutrn the prior of delNode"""
    j=1
    while(current.next):
        if j<i:
            j+=1
            current=current.next
        elif j==i:
            delNode=current.next
            nextNode=delNode.next
            current.next=nextNode
            print('del num is ',delNode)
            return nextNode
    return False

def kingMonkey(n,m):
    l=LinkList()
    for i in range(1,n+1):
        l.add(i)    
    j=0
    current=l.head
    while(j<n-1):
        newHead=delI(current,m-1)
        current=newHead
        j+=1
    return newHead.next

def test():
    n=2
    m=3
    print(kingMonkey(n,m))

test()
