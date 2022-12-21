import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
s, X, Y = map(int, input().split())
d = ((1, 0), (-1, 0), (0, 1), (0, -1))

result = []
tmp_que = []
que = deque([[(X-1, Y-1)]])
while que and s:
    tmp_que.clear()
    s -= 1
    qu = que.popleft()
    # print(qu)
    for q in qu:
        for dx, dy in d:
            x, y = q[0] + dx, q[1] + dy
            if 0 <= x < n and 0 <= y < n:
                if ground[x][y]:
                    result.append(ground[x][y])
                else:
                    tmp_que.append((x, y))
    if result:
        break
    else:
        que.append(tmp_que.copy())

print(min(result)) if result else print(0)