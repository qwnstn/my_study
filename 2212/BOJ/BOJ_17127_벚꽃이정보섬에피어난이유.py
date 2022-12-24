from itertools import combinations
n = int(input())
flower = list(map(int, input().split()))
result = 0
for com in combinations(range(1, n), 3):
    a1, tmp1 = flower[:com[0]], 1
    a2, tmp2 = flower[com[0]:com[1]], 1
    a3, tmp3 = flower[com[1]:com[2]], 1
    a4, tmp4 = flower[com[2]:], 1

    for i in a1:
       tmp1 *= i
    for i in a2:
       tmp2 *= i
    for i in a3:
       tmp3 *= i
    for i in a4:
       tmp4 *= i

    tmp = tmp1 + tmp2 + tmp3 + tmp4
    if result < tmp:
        result = tmp

print(result)