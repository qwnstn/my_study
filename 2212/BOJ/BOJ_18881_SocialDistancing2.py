n = int(input())

cows = []
for _ in range(n):
    x, s = map(int, input().split())
    cows.append((x, s))
cows.sort()

d = float('inf')
sick_idx = []
sick = 0
for i in range(n-1):
    x, s = cows[i][0], cows[i][1]
    if s != cows[i+1][1]:
        if d > cows[i+1][0] - x:
            d = cows[i+1][0] - x
    if s:
        sick_idx.append(i)
if cows[n-1][1]:
    sick_idx.append(n-1)

if d == float('inf'):
    if s:
        print(1)
    else:
        print(0)
else:
    result = 1
    for i in range(1, len(sick_idx)):
        if cows[sick_idx[i]][0] - cows[sick_idx[i-1]][0] < d:
            pass
        else:
            result += 1
        start = cows[sick_idx[i]][0]
    print(result)