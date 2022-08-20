# 메모이제이션
def func(k, n):
    ck = 0
    if k >= 2:
        if memo[k][n] == 0:
            for i in range(1, n + 1):
                ck = ck + func(k - 1, i)
            memo[k][n] = ck
        return memo[k][n]
    elif k == 1:
        if memo[k][n] == 0:
            memo[k][n] = n * (n + 1) // 2
        return memo[1][n]
    else:
        if memo[k][n] ==0:
            memo[0][n] = n
        return memo[0][n]


t = int(input())


for i in range(t):
    k = int(input())
    n = int(input())
    memo = [[0 for i in range(n+1)] for i in range(k+1)]

    print(func(k, n))