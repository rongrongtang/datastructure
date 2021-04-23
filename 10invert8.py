def convert(n,base):
    if n<base:
        return str(n)
    r=''
    while n>0:
        r+=str(n%base)
        n=n//base                
    return(r)    


def test():
    for i in range(16):
        r=convert(i,8)
        print(r[-1::-1])
        
test()        