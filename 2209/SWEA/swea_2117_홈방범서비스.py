'''
1. 전체 집의 개수 구하기

2-1. n이 홀수 일 때 같은 값의 k로 모두 덮을 수 있음
2-2. n이 짝수 일 때 k+1값으로 모두 덮을 수 있음,
        같은 값으로는 모서리 하나는 못채움 - 모서리 3개 까지는 카바 가능

3. 운영비용 구하기 - 미리 구해두기

4. 집이 가능한 최대 가격을 제한으로 운영비용의 최대값이 정해짐

5. 확인하면서 줄이기
    5-1. 범위 탐색을 어떻게 하지? 그냥 상하좌우로 가자 bfs

'''

import sys;sys.stdin=open('swea_2117_홈방범서비스.txt', 'r')

def find():     # bfs
    global ck

    while que:
        x, y, c = que.pop(0)
        if n-1 >= x >= 0 and n-1 >= y >= 0: # 유효 확인
            if visited[x][y] == 0:          # 방문 확인
                visited[x][y] = 1
                if ground[x][y] == 1:       # 집이 있으면 센다.
                    ck += 1
                if c > 1:                   # 깊이가 남아있으면
                    for z in range(4):          # que에 상하좌우 넣기
                        que.append([x+dx[z], y+dy[z], c-1])




test = int(input())

cost = [0, 1]
a = 1
for i in range(2, 22):
    a += (i-1)*4
    cost.append(a)
    # [0, 1, 5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265, 313, 365, 421, 481, 545, 613, 685, 761, 841]
    # 운영 비용, 인덱스 번호 = K

for t in range(1, test+1):
    n, m = map(int, input().split())
    ground = []
    for i in range(n):      # 2차원 땅 제작
        ground.append(list(map(int, input().split())))

    home = 0
    for i in range(n):      # 집의 개수 = home
        home += ground[i].count(1)

    if home == 0:           # 집이 없다면 종료
        print(f'#{t} 0')
        continue

    total_home = home * m     # 가능한 최대 요금 = total_home

    max_field = 0             # 가능한 최대 운영 크기 = max_field
    for i in range(1, 22):
        if total_home < cost[i]:
            max_field = i - 1
            break
        elif total_home == cost[i]:
            max_field = i
            break
        if total_home >= cost[-1]:
            max_field = 21

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for d in range(max_field, 0, -1):       # 운영범위를 줄여나갈 것
        max_home = 0            # 범위 내 최대 집의 개수, 세 범위마다 리셋
        for i in range(n):      # 좌표 한번 다 돌기
            for k in range(n):
                ck = 0          # 집의 개수, 매번 리셋 = ck
                que = [[i, k, d]]   # 좌표, 가능한 깊이 d
                visited = [[0 for _ in range(n)] for _ in range(n)] # 방문 체크용, 매번 리셋
                find()

                if ck > max_home:   # 각 좌표별 최대 집의 개수 구하기
                    max_home = ck

        if max_home * m >= cost[d]:
            break

    print(f'#{t} {max_home}')