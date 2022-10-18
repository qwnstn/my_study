import sys;input = sys.stdin.readline

n = int(input())

result = []
stack = []
for _ in range(n):
    a, *b = map(str, input().split())

    if a[-1] == 'h':
        stack.append(*b)
    elif a[-1] == 'p':
        if stack:
            if a[0] == 'p':
                result.append(stack.pop())
            else:
                result.append(stack[-1])
        else:
            result.append(-1)
    elif a[-1] == 'e':
        result.append(len(stack))
    elif a[-1] == 'y':
        if stack:
            result.append(0)
        else:
            result.append(1)

print('\n'.join(map(str, result)))