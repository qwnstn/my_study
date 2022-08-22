from itertools import combinations, permutations

n, m = map(int, input().split())

numlist = list(range(1, n+1))

perm = list(combinations(numlist, m))

for i in perm:
    print(*i)