def fibonacci(x):
    if x == 0:
        result = 0
        return result
    elif x == 1:
        result = 1
        return result
    else:
        result = fibonacci(x-1) + fibonacci(x-2)
    return result

n = int(input())
print(fibonacci(n))