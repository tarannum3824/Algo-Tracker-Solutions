class gdcFind:
    def findGCD(self, str1:str, str2:str)->str:
        if str1+str2 != str2+str1:
            return ""
        def gdc(a:int, b:int)->int:
            while b !=0:
                a,b =b,a%b
            return a
        gdc_length=gdc(len(str1),len(str2))
        return str1[0:gdc_length]
    
obj1=gdcFind()
print(obj1.findGCD("tatatatatata","tata"))