def isPrime(n):
    count=0
    if n<=1:
        print(f"{n} is not prime number")
    elif n==2:
        print(f"{n} is a prime number")
    else:
        for i in range (2,n):
             if n%i==0:
                 count+=1
        if count >=1:
            print(f"{n} is not prime number")   
        else:
            print(f"{n} is a prime number")
            
isPrime(29)
isPrime(27)
isPrime(20)