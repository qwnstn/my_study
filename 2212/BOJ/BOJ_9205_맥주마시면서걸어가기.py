from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    now = tuple(map(int, input().split()))
    stations = [tuple(map(int, input().split())) for _ in range(n)]
    goal = tuple(map(int, input().split()))
    stations += [goal]
    visited = [0 for _ in range(n+1)]
    # print(station)

    # bfs
    que = deque([now])
    # print(que)
    while que:
        q = que.popleft()
        # print(q)
        for idx, station in enumerate(stations):
            if not visited[idx]:
                if abs(station[0] - q[0]) + abs(station[1] - q[1]) <= 1000:
                    que.append(station)
                    visited[idx] = 1

        if visited[-1]:
            break

    print('happy') if visited[-1] else print('sad')