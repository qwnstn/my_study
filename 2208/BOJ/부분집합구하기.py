import sys

a = list(map(str, sys.stdin.readline().strip()))

result = set()
for i in range(1, 1<<len(a)):
    sum = ''
    for j in range(len(a)):
        if i & (1 << j):
            sum = sum + a[j]
            result.add(sum)
print(result, len(result))