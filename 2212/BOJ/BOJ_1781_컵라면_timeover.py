import sys
input = sys.stdin.readline

n = int(input())

problem = []
# (데드라인, 컵라면 수)
for _ in range(n):
    problem.append(tuple(map(int, input().split())))

problem.sort(key=lambda x: (-x[1], x[0]))
# 컵라면 많은 순으로 정렬, 데드라인 적은 순으로 정렬
# print(problem)

result = [0 for _ in range(n+1)]
for d, c in problem:
    if not result[d]:
        result[d] = c
    else:
        while d != 1:
            d -= 1
            if not result[d]:
                result[d] = c
                break

print(sum(result))
