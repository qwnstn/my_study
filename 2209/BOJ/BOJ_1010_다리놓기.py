import sys

input = sys.stdin.readline
test = int(input())

for t in range(test):
    n, m = map(int, input().split())
    # mCn

    M = 1
    N = 1

    if n <= m//2:
        for i in range(n):
            N *= (n - i)
            M *= (m - i)
    else:
        n = m - n
        for i in range(n):
            N *= (n - i)
            M *= (m - i)

    print(M // N)