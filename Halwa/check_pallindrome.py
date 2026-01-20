class palindrome:
    def checkPalindrom(self, string:str)->bool:
        cleanString=[]
        for character in string:
            if character.isalnum():
                lowercharacter=character.lower()
                cleanString.append(lowercharacter)
        return cleanString==cleanString[::-1]
           
obj1=palindrome()
check=obj1.checkPalindrom("My name is Sanu!")
print(check)

obj2=palindrome()
check=obj2.checkPalindrom("A man, a plan, a canal: Panama")
print(check)