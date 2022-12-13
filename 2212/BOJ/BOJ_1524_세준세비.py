import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    input()
    n, m = map(int, input().split())

    세준 = max(map(int, input().split()))
    세비 = max(map(int, input().split()))

    if 세준 >= 세비:
        print('S')
    else:
        print('B')