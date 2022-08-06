def factorial(x):
    if x == 0 or x == 1:
        result = 1
        return result
    result = x * factorial(x-1)
    return result

n = int(input())
print(factorial(n))