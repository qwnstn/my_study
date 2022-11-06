import sys
input = sys.stdin.readline

n, k = map(int, input().split())    # n = 전체, k = 1의 최소 개수
num_list = list(map(int, input().split()))

idx = []
ck = 0
for i in range(n):
    if num_list[i] == 1:
        idx.append(i)
        ck += 1

if ck < k:
    result = -1
else:
    result = n
    for i in range(ck - k + 1):
        tmp = idx[i + k - 1] - idx[i] + 1
        if tmp < result:
            result = tmp

print(result)

