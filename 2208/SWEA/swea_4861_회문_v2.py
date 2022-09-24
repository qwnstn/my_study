'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다.
NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
'''
import time
start = time.time()

import sys

sys.stdin = open("swea_4861_회문.txt", "r")

test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())

    bingo = []
    for i in range(n):
        bingo.append(list(map(str, input().strip())))               # .strip()을 하면 문자 하나씩 받아짐
    # print(bingo)

    for i in range(n):                                              # 행 번호
        for j in range(n-m+1):                                      # 행마다 찾을 개수
            ck1 = 0
            ck2 = 0
            for k in range(m // 2):                                 # 회문 확인
                if bingo[i][j + k] == bingo[i][j + (m - 1) - k]:
                    ck1 = ck1 + 1
                    if k == range(m // 2)[-1] and ck1 == m // 2:
                        print(f'#{t}', end=' ')
                        print(''.join(bingo[i][j:j+m]))
                if bingo[j + k][i] == bingo[j + (m - 1) - k][i]:
                    ck2 = ck2 + 1
                    if k == range(m // 2)[-1] and ck2 == m // 2:
                        print(f'#{t}', end=' ')
                        for x in range(m):
                            print(bingo[j+x][i], end='')
                        print()
                if k == range(m // 2)[-1] and (ck1 != m//2 or ck2 != m//2):
                    break

print("time :", time.time() - start)