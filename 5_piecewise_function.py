# Piecewise Function
def f(x):
    if x < 0:
        return x ** 2
    elif x == 0:
        return 0 
    else:
        return x + 2

result = f(3)
print("Result = ", result)
