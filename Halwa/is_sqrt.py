class checkSqrt:
    def isNumberSqrt(self, number:int)->bool:
        if number <0:
            return False
        squareRoot=number**0.5
        if squareRoot.is_integer():
            return True
        else:
            return False
        
obj1=checkSqrt()
print(obj1.isNumberSqrt(36))
print(obj1.isNumberSqrt(26))