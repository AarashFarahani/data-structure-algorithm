def fibbonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(fibbonacci(3))
print(fibbonacci(10))

print(factorial(3))
print(factorial(5))
print(factorial(10))