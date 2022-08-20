import sys

n, m = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))
num.sort()

maximum = 0
for i in range(n-1, 1, -1):
    for j in range(n-2, 0, -1):
        if j == i:
            continue
        for k in range(n-3, -1, -1):
            if k == i or k == j:
                continue
            sum = num[i] + num[j] + num[k]
            if sum <= m and maximum < sum:
                maximum = sum
                break

print(maximum)