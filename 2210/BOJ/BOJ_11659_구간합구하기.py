import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

new_num = [0]
total = 0
for i in range(n):
    total += num[i]
    new_num.append(total)

for _ in range(m):
    s, e = map(int, input().split())

    result = new_num[e] - new_num[s-1]

    print(result)
