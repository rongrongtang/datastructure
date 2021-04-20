def monkeyKing(n,m):
    j=1
    nums=[x for x in range(1,n+1)]    
    i=countI=0
    while(j<n):
        #delete n-1 times
        while(countI<m-1):
            #Do not count times if nums[i]==None
            if nums[i%n]!=None:
                countI+=1
            i+=1
        #if nums[i]==None, continue to search next nums[i]
        while(nums[i%n]==None):
            i+=1
        print('delete num is ',nums[i%n])
        nums[i%n]=None       
        countI=0
        j+=1
    return nums

def search(nums):
    for i in range(len(nums)):
        if nums[i]!=None:
            print('the king is ',nums[i])
        
nums=monkeyKing(2,3)
search(nums)   
    