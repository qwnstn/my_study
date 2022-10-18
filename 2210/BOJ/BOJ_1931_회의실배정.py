import sys
input = sys.stdin.readline

n = int(input())
study = [list(map(int, input().split())) for _ in range(n)]
study.sort(key=lambda x: (x[1], x[0]))

result = 0
start = 0
for s, e in study:
    if s >= start:
        start = e
        result += 1

print(result)