'''
정확히 5개만 되는 줄 알고 코드 제작
6개 이상이어도 상관이 없음

만약 정확히 5개만 된다면 주석 안의 내용으로 교환
'''

import sys;sys.stdin=open('swea_11315_오목판정.txt', 'r')

test = int(input())

for t in range(1, test + 1):
    n = int(input())

    ground = [['.' for _ in range(n+2)]]
    for _ in range(n):
        ground.append(['.'] + list(input()) + ['.'])
    ground.append(['.' for _ in range(n+2)])

    ground_a = [[] for _ in range(n + 2)]
    for i in range(n + 2):
        x = ''
        for j in range(n+2):
            x += ground[i][j]
        ground_a[i].append(x)

    result = 0                              # 결과, 탈출용 변수
    for i in ground_a:          
        result = i[0].count('ooooo')        # 가로로 찾기, 5개 라면 '.ooooo.'
        if result:
            break
    if result:
        print(f'#{t} YES')
        continue

    ground_mirror = list(zip(*ground))
    ground_r = [[] for _ in range(n + 2)]
    for i in range(n + 2):
        x = ''
        for j in range(n + 2):
            x += ground_mirror[i][j]
        ground_r[i].append(x)

    for i in ground_r:
        result = i[0].count('ooooo')        # 세로로 찾기, 5개 라면 '.ooooo.'
        if result:
            break
    if result:
        print(f'#{t} YES')
        continue


    dx = [1,-1,-1,1]
    dy = [1,-1,1,-1]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if ground[i][j] == 'o':
                ck = 1
                for d in range(2):
                    tmp = 1
                    while True:
                        if ground[i+dx[d]*tmp][j+dy[d]*tmp] == 'o': # 우상대각선 찾기
                            ck += 1
                            tmp += 1
                            if ck >= 6:
                                break
                        else:
                            break
                    if ck == 5:
                        result = 1

                ck = 1
                for d in range(2, 4):
                    tmp = 1
                    while True:
                        if ground[i + dx[d]*tmp][j + dy[d]*tmp] == 'o': # 우하대각선 찾기
                            ck += 1
                            tmp += 1
                            if ck >= 6:
                                break
                        else:
                            break
                    if ck == 5:
                        result = 1
                        break
            if result:
                break
        if result:
            break

    if result:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')