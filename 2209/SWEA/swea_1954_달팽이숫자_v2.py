'''


'''

import sys;sys.stdin=open('swea_1954_달팽이숫자.txt', 'r')


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

test = int(input())

for t in range(1, test + 1):
    n = int(input())

    snail = [[0 for _ in range(n)] for _ in range(n)]

    d = 0
    x = 0
    y = -1
    for i in range(1, n**2 + 1):
        x += dx[d]
        y += dy[d]
        try:   
            if not snail[x][y]: # 값이 0이면
                snail[x][y] = i
            else:               # 값이 존재하면
                x -= dx[d]
                y -= dy[d]
                d += 1
                d %= 4
                x += dx[d]
                y += dy[d]
                snail[x][y] = i
        except: # 에러 방지용
            x -= dx[d]
            y -= dy[d]
            d += 1
            d %= 4
            x += dx[d]
            y += dy[d]
            snail[x][y] = i

    print(f'#{t}')
    for i in snail:
        print(*i)