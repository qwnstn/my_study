import sys
input = sys.stdin.readline

player = dict()
result = []
while True:
    player.clear()
    result.clear()
    first = 0
    second = 0
    n, m = map(int, input().split())
    if not n:
        break
    for _ in range(n):
        for a in map(int, input().split()):
            if player.get(a):
                player[a] += 1
            else:
                player[a] = 1
            if first < player[a]:
                first = player[a]

    for k, v in player.items():
        if second < v:
            if v != first:
                second = v
    for k, v in player.items():
        if v == second:
            result.append(k)
    result.sort()
    print(*result)