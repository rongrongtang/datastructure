class LinearList():
    def __init__(self):
        self.n=0
        self.arr=[]
    def __repr__(self):
        return self.arr.__str__()
    def add(self,num):
        self.arr.append(num)
        self.n+=1
        return self.arr
    def delete(self,i):
        if i<1 or i>self.n:
            return False
        del self.arr[i-1]
        self.n-1
        return self.arr
    def search(self,i):
        if i<1 or i>self.n:
            return False
        return self.arr[i-1]
    def searchE(self,n):
        for i in range(len(self.arr)):
            if self.arr[i]==n:
                return i+1
        return False
    def __len__(self):
        return self.n
        

def test():
    l=LinearList()
    for i in range(1,11):
        l.add(i)
    print(l)
    print(len(l))
    l.delete(3)
    print(l)
    print(l.search(2))
    print(l.searchE(10))
    
test()
    
