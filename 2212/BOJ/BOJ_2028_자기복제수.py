t = int(input())

for _ in range(t):
    n = input()
    ck = 10 ** len(n)

    num = int(n)
    if (num**2 - num) % ck:
        print('NO')
    else:
        print('YES')