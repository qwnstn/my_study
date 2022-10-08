from collections import deque

n, k = map(int, input().split())

visited = [0 for _ in range(100001)]
que = deque()
que.append([n, 1])  # 위치,시간(초기에 1로 시작)
escape = 1
result = 0          # 없이 하면 백준에서 NameError
while que and escape:
    q = que.popleft()
    visited[q[0]] = q[1]
    for i in [q[0], 1, -1]:
        if 0 <= q[0] + i <= 100000:
            if not visited[q[0] + i]:
                if q[0] + i == k:
                    escape = 0
                    result = q[1]
                    break
                else:
                    que.append([q[0] + i, q[1]+1])

print(result)