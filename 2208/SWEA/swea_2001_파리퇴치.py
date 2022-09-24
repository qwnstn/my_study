'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

죽은 파리의 개수를 구하라!

예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.

1. N 은 5 이상 15 이하이다.

2. M은 2 이상 N 이하이다.

3. 각 영역의 파리 갯수는 30 이하 이다.
'''

import sys
sys.stdin = open("swea_2001_파리퇴치.txt", "r")

test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())

    fly = []
    for i in range(n):
        fly.append(list(map(int, input().split())))

    maximum = 0
    for i in range(n -m +1):
        for j in range(n -m +1):                            # 좌표 설정
            sum = 0
            for k in range(m):
                for l in range(m):                          # 좌표에 따른 범위 설정
                    sum = sum + fly[i+k][j+l]
                    if sum > maximum:
                        maximum = sum
    print(f'#{t} {maximum}')