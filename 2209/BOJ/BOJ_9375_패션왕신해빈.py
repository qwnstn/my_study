import sys
input = sys.stdin.readline

test = int(input())

for t in range(test):
    n = int(input())

    clo = dict()
    for i in range(n):
        a, b = map(str, input().split())

        if clo.get(b):
            clo[b].append(a)
        else:
            clo[b] = [a]

    result = 1
    for k in clo.keys():
        result *= len(clo[k])+1
    result -= 1
    print(result)