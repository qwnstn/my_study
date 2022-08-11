import sys

n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
mlist = list(map(int, sys.stdin.readline().split()))

nlist.sort()
result = []

for i in mlist:
    turn = 0
    ck = 0
    if i == nlist[-1]:
        result.append(1)
        continue

    while n//(2**turn) > 0:
        turn = turn + 1
        turnlen = 0

        if nlist[n//(2**turn) + turnlen] > i:
            pass
        elif nlist[n//(2**turn) + turnlen] < i:
            turnlen = turnlen + n//(2**turn)
        else:
            ck = ck + 1
            break

    result.append(ck)
print(' '.join(map(str,result)))