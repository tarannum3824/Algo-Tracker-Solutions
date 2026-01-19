def factorialOfNumber(number):
    if number < 0:
        return "Factorial is not for negative number"
    elif number ==0:
        return 1
    else:
        result=1
        for i in range (1, number+1):
            result *= i
        return result
     
print(factorialOfNumber(100))