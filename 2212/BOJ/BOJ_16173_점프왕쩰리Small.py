from collections import deque

n = int(input())

ground = [tuple(map(int, input().split())) for _ in range(n)]

d = ((0, 1), (1, 0))

# bfs
result = 'Hing'
que = deque([(0, 0)])
while que:
    q = que.popleft()
    x, y = q[0], q[1]
    value = ground[x][y]
    if not ground[x][y]:
        continue
    if ground[x][y] == -1:
        result = 'HaruHaru'
        break
    for dx, dy in d:
        x, y = q[0] + dx * value, q[1] + dy * value
        if 0 <= x < n and 0 <= y < n:
            que.append((x, y))

print(result)