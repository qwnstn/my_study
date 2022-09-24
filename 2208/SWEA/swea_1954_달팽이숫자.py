'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
'''

'''
1. 맨 윗줄은 순서 대로 넣는다.
2. 행동을 두 세트로 나눠 한 세트는 (우측, 하단) 이동, 다른 세트는 (좌측, 상단)이동을 한다.
'''
import sys

sys.stdin = open("swea_1954_달팽이숫자.txt", "r")

t = int(input())

for x in range(1, t +1):
    n = int(input())

    snail = []
    for i in range(n):
        snail = snail + [[0] * n]                    # [[0, 0..], [0, 0..]... [0, 0..]]

    num = 0
    for i in range(n):
        num = num + 1
        snail[0][i] = num                            # [[1,2,3..], [0, 0..]... [0, 0..]], num = n


    for c, i in enumerate(range(n-1, 0, -1)):
        if c % 2 == 0:                                          # 홀수번째, c//2 = 0,1,2...
            for k in range(i):                                  # k = 0 ~ i-1
                num = num + 1
                snail[(c//2 +1) +k][(n-1)-c//2] = num              # (x(증가), y(고정))

            for k in range(i):
                num = num + 1
                snail[(n-1)-c//2][(n-1)-(c//2 +1) -k] = num        # (x(고정), y(감소))

        else:                                                   # 짝수번째, c//2 = 0,1,2...
            for k in range(i):
                num = num + 1
                snail[(n-1)-(c//2 +1) -k][c//2] = num              # (x(감소), y(고정))

            for k in range(i):
                num = num + 1
                snail[c//2 +1][(c//2 +1) +k] = num                 # (x(고정), y(증가))

    print(f'#{x}')
    for i in range(len(snail)):
        print(*snail[i])