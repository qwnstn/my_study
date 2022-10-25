import sys
input = sys.stdin.readline

n = int(input())
files = [input().strip() for _ in range(n)]
result = list(files[0])

for i in files:
    for k in range(len(result)):
        if result[k] != i[k]:
            result[k] = '?'

for i in result:
    print(i, end='')