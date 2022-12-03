import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    input()
    n, m = map(int, input().split())

    세준 = list(map(int, input().split()))
    세비 = list(map(int, input().split()))

    S = 0
    for i in 세준:
        if i > S:
            S = i

    B = 0
    for i in 세비:
        if i > B:
            B = i

    if S >= B:
        print('S')
    else:
        print('B')