'''
n*(n+1) < (length) <= (n+1)**2 < (length) <= (n+1)*(n+2)
            2n+1번                2n+2번
 ck(n)                                          ck(n+1)
'''
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    length = y - x

    n = 0
    ck = 0
    while True:
        n += 1
        ck = n * (n + 1)
        if length <= ck:
            break
    n -= 1

    if ck - (n + 1) < length <= ck:
        print(2 * n + 2)
    else:
        print(2 * n + 1)