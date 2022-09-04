import sys

input = sys.stdin.readline
test = int(input())

for t in range(test):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    result = 0

    for i in range(n):
        ck = 0
        cx, cy, r = map(int, input().split())
        if (x1-cx)**2 + (y1-cy)**2 < r**2:
            ck += 1
        if (x2-cx)**2 + (y2-cy)**2 < r**2:
            ck += 1

        if ck == 1:
            result += 1

    print(result)