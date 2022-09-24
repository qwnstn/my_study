'''
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

'''

'''
0. 상하좌우로 한줄씩 추가
1. 슬라이싱으로 가로로 세고,
2. 전치 행렬 해서 다시 가로로 센다

'''

import sys
sys.stdin = open("swea_1979_어디에단어가들어갈수있을까.txt", "r")

test = int(input())

for t in range(1, test+1):
    n, k = map(int, input().split())

    bingo = [[0]*(n+2)]
    for i in range(n):
        bingo.append([0] + list(map(int, input().split())) + [0])
    bingo.append([0]*(n+2))

    result = 0
    for i in range(1, n+1):                        # 행 번호(1~, n개)
        for j in range(1, n-k+1+1):                # 열 번호(1~, n-k+1개)
            if sum(bingo[i][j:j+k]) == k and bingo[i][j-1] == 0 and bingo[i][j+k] == 0:  # 정확히 k개
                result = result + 1

    bingo = list(zip(*bingo))                           # 전치

    for i in range(1, n+1):                        # 행 번호(1~, n개)
        for j in range(1, n-k+1+1):                # 열 번호(1~, n-k+1개)
            if sum(bingo[i][j:j+k]) == k and bingo[i][j-1] == 0 and bingo[i][j+k] == 0:  # 정확히 k개
                result = result + 1

    print(f'#{t} {result}')