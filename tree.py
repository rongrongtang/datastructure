class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)
    
class Tree:
    def __init__(self,head=None):
        self.head=head
    def root(self):
        return self.head
    def add(self,num):
        node=Node(num)
        if not self.head:
            self.head=node
            return self.head
        elif num<self.head.data:
            if not self.head.left:
                self.head.left=node
            else:
                left=Tree(self.head.left)
                left.add(num)
        else:
            if not self.head.right:
                self.head.right=node
            else:
                right=Tree(self.head.right)
                right.add(num)
    
    def midPro(self):
        if self.head:
            left=Tree(self.head.left)
            left.midPro()
            print(self.head)
            right=Tree(self.head.right)
            right.midPro()
            
def BFS(root):
    seq=[]
    if root:
        seq.append(root)
    while(seq):
        cur=seq.pop(0)
        print(cur)
        if cur.left:
            seq.append(cur.left)
        if cur.right:
            seq.append(cur.right)
            
def DFS(root):
    stack=[]
    if root:
        stack.append(root)
    while(stack):
        cur=stack.pop(-1)
        print(cur)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
            

def test():
    t=Tree()
    t.add(2)
    t.add(1)
    t.add(3)
    t.add(4)
    t.midPro()
    BFS(t.root())
    DFS(t.root())
    
test()
            