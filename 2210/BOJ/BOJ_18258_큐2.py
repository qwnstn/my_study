from collections import deque
import sys
input = sys.stdin.readline

result = []
z = deque()
n = int(input())
for _ in range(n):
    a, *b = map(str, input().split())

    if a == 'push':
        z.append(b[0])
    elif a == 'pop':
        try:
            result.append(z.popleft())
        except:
            result.append(-1)
    elif a == 'size':
        result.append(len(z))
    elif a == 'empty':
        if len(z):
            result.append(0)
        else:
            result.append(1)
    elif a == 'front':
        try:
            result.append(z[0])
        except:
            result.append(-1)
    elif a == 'back':
        try:
            result.append(z[-1])
        except:
            result.append(-1)

print('\n'.join(map(str, result)))