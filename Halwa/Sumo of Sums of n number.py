def sumofsumsofnumber(n):
    sumofSums=0
    for i in range(1,n+1):
        total=0
        for j in range(1,i+1):
            total+=j
        sumofSums+=total    
    return sumofSums
print(sumofsumsofnumber(5))
        
    
    
    
