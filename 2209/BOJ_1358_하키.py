import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
result = 0
for i in range(p):
    x1, y1 = map(int, input().split())

    if x <= x1 <= x + w and y <= y1 <= y + h:
        result += 1
        continue

    if x1 < x:
        if (x - x1)**2 + (y + h/2 - y1)**2 <= (h/2)**2:
            result += 1
            continue

    elif x1 > x + w:
        if (x1 - x - w)**2 + (y + h/2 - y1)**2 <= (h/2)**2:
            result += 1
            continue

print(result)