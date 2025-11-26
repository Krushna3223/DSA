# Program: Factorial using normal function

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of", num, "is", result)



# Program: Factorial using recursive function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of", num, "is", result)
