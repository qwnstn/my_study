import pprint
a, b = input().split()
set_b = set(b)

for i, v in enumerate(a):
    if v in set_b:
        first_a = i
        first_b = b.index(v)
        break
# print(first_a, first_b)

n = len(a)
m = len(b)
answer = [['.' for _ in range(n)] for _ in range(m)]

for i in range(m):
    answer[i][first_a] = b[i]
answer[first_b] = list(a)

for i in range(m):
    for k in range(n):
        print(answer[i][k], end='')
    print()
# pprint.pprint(answer)
