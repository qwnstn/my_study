'''
다음 100X100의 2차원 배열이 주어질 때,
각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
'''

import sys
import time
start = time.time()  # 시작 시간 저장
sys.stdin = open("swea_1209_sum.txt", "r")

for x in range(10):
    t = int(input())
    bingo = [list(map(int, input().split())) for i in range(100)]

    maximum = sum(bingo[0])                     # 초기값
    for i in range(100):
        if sum(bingo[i]) > maximum:
            maximum = sum(bingo[i])             # 행 최대값

    for j in range(100):                        # 열 최대값
        ck = 0
        for i in range(100):                    # [i,j(고정)]의 합
            ck = ck + bingo[i][j]
        if ck > maximum:
            maximum = ck

    for i in range(100):                        # 우하 대각선
        ck = 0
        ck = ck + bingo[i][i]
        if ck > maximum:
            maximum = ck
    
    for i in range(100):                        # 우상 대각선
        ck = 0
        ck = ck + bingo[i][99-i]
        if ck > maximum:
            maximum = ck

    print(f'#{t} {maximum}')
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
