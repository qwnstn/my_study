n = int(input())
if n == 1:
    print(0)
elif not n % 2:
    print(n - n//2)
else:
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            result = n - n // i
            break
    try:
        print(result)
    except:
        print(n - 1)
