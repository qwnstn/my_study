import sys
# sys.stdin = open("BOJ_1781_컵라면.txt", "r")
input = sys.stdin.readline

n = int(input())

problem = []
# (데드라인, 컵라면 수)
for _ in range(n):
    problem.append(tuple(map(int, input().split())))

problem.sort(key=lambda x: (-x[1], x[0]))
# 컵라면 많은 순으로 정렬, 데드라인 적은 순으로 정렬
# print(problem)

ck = dict()
result = 0
for d, c in problem:
    tmp = ck.get(d)
    if tmp == 0:
        continue

    if not tmp:
        ck[d] = d - 1
        result += c

    else:
        while ck.get(tmp):
            ck[d] = ck.get(tmp)
            tmp = ck.get(tmp)
        if ck.get(tmp) == None:
            result += c
        ck[tmp] = tmp - 1

    # print(ck)
    # print(result)
print(result)
'''
6
3 54
2 15
2 10
10 6
10 5
3 3
'''