import sys
input = sys.stdin.readline

n = int(input())

problem = []
# (데드라인, 컵라면 수)
for _ in range(n):
    problem.append(tuple(map(int, input().split())))

# print(problem)
problem.sort(key=lambda x: (x[0], -x[1]))

result = 0
ck = 0  # 데드라인 체크
for d, c in problem:
    if d != ck:
        ck = d
        result += c

print(result)