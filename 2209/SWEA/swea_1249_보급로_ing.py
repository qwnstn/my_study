'''
새 값이 기존값보다 작으면 갱신
                같으면? 갱신X
                크면 ? 갱신x
'''

import sys;sys.stdin=open('swea_1249_보급로.txt', 'r')

from collections import deque


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] > visited[x][y] + arr[nx][ny]:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    q.append((nx, ny))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[float('inf')] * N for _ in range(N)]

    bfs()
    print(f'#{tc} {visited[N-1][N-1]}')