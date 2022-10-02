import sys
input = sys.stdin.readline

n, k = map(int, input().split())

num = list(map(int, input().split()))

new_num = [0]
total = 0
for i in range(n):
    total += num[i]
    new_num.append(total)

result = float('-inf')
for i in range(k, n+1):
    tmp = new_num[i] - new_num[i - k]
    if tmp > result:
        result = tmp

print(result)

