def fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo(n-1) + fibo(n-2))  
terms = int(input("How many terms? "))
if ((terms>=1) and (terms<=1000000)):
    if terms <= 0:  
        print("Plese enter a positive integer")  
    else:  
        print("Fibonacci sequence:")  
        for i in range(terms):  
            print(fibo(i))  
else:
    print("out of bounds")
