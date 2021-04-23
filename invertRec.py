def invert(n,base):    
    if n<base:
        return str(n)
    if n>0:
        return invert(n//base,base)+str(n%base)

def test():
    
    for i in range(16):        
        print(invert(i,8))
        
test()
