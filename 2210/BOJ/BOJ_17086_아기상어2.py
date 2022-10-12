def length(a, b):
    ck = 0
    c0 = abs(a[0] - b[0])
    c1 = abs(a[1] - b[1])

    return max(c0, c1)


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

shark = []                          # 상어 좌표
for i, v in enumerate(ground):
    for k in range(m):
        if v[k]:
            shark.append([i, k])

for i in range(n):
    for k in range(m):
        if not ground[i][k]:
            ground[i][k] = float('inf')
            for s in shark:
                tmp = length([i, k], s)
                if tmp < ground[i][k]:
                    ground[i][k] = tmp
                if ground[i][k] == 1:
                    break
        else:
            ground[i][k] = 0

result = 0
for i in ground:
    tmp = max(i)
    if tmp > result:
        result = tmp

print(result)