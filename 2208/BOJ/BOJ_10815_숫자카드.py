import sys

n = int(sys.stdin.readline().rstrip())
nset = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
mlist = list(map(int, sys.stdin.readline().split()))
mset = set(mlist)


nmset = set(nset & mset)
result = []

for i in mlist:
    if i in nmset:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))