def isPalindrome(number):
    strnum=str(number)
    reverse=""
    length=len(strnum)
    for i in range(length-1,-1,-1):
        reverse +=strnum[i]  
    if strnum==reverse:
        return True
    else:
        return False
    
print(isPalindrome(123456789)) 
print(isPalindrome(12321))