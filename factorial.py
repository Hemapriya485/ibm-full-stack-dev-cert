def factorial_of_n(n):
    fact=1
    for x in range(1,n+1):
        fact=fact*x
    return fact
print("Enter a number:")
n=int(input())
print(n)
factorial=factorial_of_n(n)
print("Factorial of "+str(n)+" is "+str(factorial))