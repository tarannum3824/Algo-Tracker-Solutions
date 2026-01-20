class swapnumbers:
    def swapnumber1(self,a:int,b:int)->int:
        a=a+b
        b=a-b
        a=a-b
        return a,b
    
    def swapnumber2(self,a:int,b:int)->int:
        a=a*b
        b=a//b
        a=a//b
        return a,b
    
    
obj1=swapnumbers()
print(obj1.swapnumber1(2,5))
print(obj1.swapnumber2(10,5))