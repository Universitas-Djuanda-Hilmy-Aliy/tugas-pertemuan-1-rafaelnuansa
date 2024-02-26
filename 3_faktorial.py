# Faktorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    for i in range(2, n + 1):
        n *= i
    return n

print(factorial(10))
