'''
터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수를 계산하여야 한다.

탈주범은 시간당 1의 거리를 움직일 수 있다.

---------------------------------------------------------------------------------------

간선을 보냈을 때 받을 수 있어야 한다
dfs 모두 탐색
'''

import sys
sys.stdin = open("swea_1953_탈주범검거.txt", "r")

def dfs(r, c):
    global l
    if visited[r][c] != 0:
        if visited[r][c] >= l:
            return

    visited[r][c] = l  # 방문 체크
    if l == 1:
        return
    l -= 1             # 시간 체크

    # 순서는 상하좌우
    if hole[r][c] == 1:         # 십자 연결
        if hole[r-1][c] in [1, 2, 5, 6]:      # 상
            dfs(r - 1, c)
        if hole[r+1][c] in [1, 2, 4, 7]:      # 하
            dfs(r + 1, c)
        if hole[r][c-1] in [1, 3, 4, 5]:      # 좌
            dfs(r, c - 1)
        if hole[r][c+1] in [1, 3, 6, 7]:      # 우
            dfs(r, c + 1)
    elif hole[r][c] == 2:       # 상하 연결
        if hole[r-1][c] in [1, 2, 5, 6]:      # 상
            dfs(r - 1, c)
        if hole[r+1][c] in [1, 2, 4, 7]:      # 하
            dfs(r + 1, c)
    elif hole[r][c] == 3:       # 좌우 연결
        if hole[r][c-1] in [1, 3, 4, 5]:      # 좌
            dfs(r, c - 1)
        if hole[r][c+1] in [1, 3, 6, 7]:      # 우
            dfs(r, c + 1)
    elif hole[r][c] == 4:       # 상우 연결
        if hole[r-1][c] in [1, 2, 5, 6]:      # 상
            dfs(r - 1, c)
        if hole[r][c + 1] in [1, 3, 6, 7]:    # 우
            dfs(r, c + 1)
    elif hole[r][c] == 5:       # 하우 연결
        if hole[r+1][c] in [1, 2, 4, 7]:      # 하
            dfs(r + 1, c)
        if hole[r][c+1] in [1, 3, 6, 7]:      # 우
            dfs(r, c + 1)
    elif hole[r][c] == 6:       # 하좌 연결
        if hole[r+1][c] in [1, 2, 4, 7]:      # 하
            dfs(r + 1, c)
        if hole[r][c-1] in [1, 3, 4, 5]:      # 좌
            dfs(r, c - 1)
    elif hole[r][c] == 7:       # 상좌 연결
        if hole[r-1][c] in [1, 2, 5, 6]:      # 상
            dfs(r - 1, c)
        if hole[r][c-1] in [1, 3, 4, 5]:      # 좌
            dfs(r, c - 1)

    l += 1                      # 함수 탈출 시 시간 복구
    return


test = int(input())

for t in range(1, test + 1):
    n, m, r, c, l = map(int, input().split())
    r += 1
    c += 1

    hole = [[0 for i in range(m + 2)]]
    for i in range(n):
        a = [0] + list(map(int, input().split())) + [0]
        hole.append(a)
    hole.append([0 for i in range(m + 2)])

    visited = [[0 for i in range(m+ 2)] for i in range(n + 2)]

    dfs(r, c)

    result = 0
    for i in visited:
        result += i.count(0)
    result = (n+2) * (m+2) - result

    print(f'#{t} {result}')