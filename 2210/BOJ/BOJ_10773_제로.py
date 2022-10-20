import sys
input = sys.stdin.readline

n = int(input())
result = 0
stack = []
for i in range(n):
    a = int(input())
    if a:
        stack.append(a)
        result += a
    else:
        result -= stack.pop()

print(result)