def reverse_number(number):
    rev=""
    length=len(number)
    for i in range(length-1,-1,-1):
        rev += number[i]
    return rev
        
print(reverse_number("123456789"))