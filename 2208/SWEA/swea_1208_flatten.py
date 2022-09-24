'''
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때,
제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open("flatten.txt", "r")


t = 10

for test_case in range(1, t + 1):
    dump = int(input())
    a = [int(i) for i in input().split()]

    a_count = [0] * 100                     # a_count[i-1] = i개의 박스를 가진 줄의 개수
    for i in a:
        a_count[i-1] = a_count[i-1] + 1

    for i in range(dump):                   # dump 1회 시행 시 최대값 -1, 다음최대값 +1, 최솟값 -1, 다음최솟값 +1
        # 정리하고 시작

        if a_count[-1] == 0:
            while a_count[-1] == 0:
                a_count = a_count[:-1]
        if a_count[0] == 0:
            while a_count[0] == 0:
                a_count = a_count[1:]

        # 길이가 1이되면 강제종료

        if len(a_count) == 1:
            break

        # 최대값 줄이기
        if a_count[-1] > 0:
            a_count[-1] = a_count[-1] - 1
            a_count[-2] = a_count[-2] + 1
        else:
            while a_count[-1] == 0:
                a_count = a_count[:-1]                   # a_count[i-1] = i개의 박스를 가진 줄의 개수
            a_count[-1] = a_count[-1] - 1
            a_count[-2] = a_count[-2] + 1

        # 최솟값 늘리기
        if a_count[0] > 0:
            a_count[0] = a_count[0] - 1
            a_count[1] = a_count[1] + 1
        else:
            while a_count[0] == 0:
                a_count = a_count[1:]
            a_count[0] = a_count[0] - 1
            a_count[1] = a_count[1] + 1
    # 끝나고 정리
    if len(a_count) == 1:
        pass
    else:
        if a_count[-1] == 0:
            while a_count[-1] == 0:
                a_count = a_count[:-1]
        if a_count[0] == 0:
            while a_count[0] == 0:
                a_count = a_count[1:]

    print(f'#{test_case} {len(a_count)-1}')