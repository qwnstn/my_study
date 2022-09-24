'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때,
칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.
'''

'''
1. 빨강 영역, 파랑 영역 좌표들을 세트로 받기 - 중복 제거
2. 교집합의 길이
'''

import sys
sys.stdin = open("swea_4836_색칠하기.txt", "r")


test = int(input())

for t in range(1, test+1):
    n = int(input())

    red = []
    blue = []
    for i in range(n):
        a = list(map(int, input().split()))
        if a[-1] == 1:
            red.append(a)       # [[2, 2, 4, 4, 1]]
        else:
            blue.append(a)      # [[3, 3, 6, 6, 2]]

    # 빨강 영역 구하기
    red_set = set()
    for i in range(len(red)):
        x1, y1 = red[i][0], red[i][1]
        x2, y2 = red[i][2], red[i][3]
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                red_set.add((x,y))
    
    # 파랑 영역 구하기
    blue_set = set()
    for i in range(len(blue)):
        x1, y1 = blue[i][0], blue[i][1]
        x2, y2 = blue[i][2], blue[i][3]
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                blue_set.add((x,y))

    # 교집합
    result = len(red_set & blue_set)

    print(f'#{t} {result}')