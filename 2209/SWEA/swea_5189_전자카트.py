'''
전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

순열문제
'''
import sys;sys.stdin=open('swea_5189_전자카트.txt', 'r')

import itertools

test = int(input())

for t in range(1, test + 1):
    n = int(input())

    ground = [[0 for _ in range(n + 1)]]          # 인덱스와 숫자 맞추는 용도
    for _ in range(n):
        a = list(map(int, input().split()))
        ground.append([0] + a)

    P = [i for i in range(2, n + 1)]               # 루트 생성
    nPr = itertools.permutations(P, n-1)

    result = 0
    for i in nPr:
        route = [1] + list(i) + [1]

        check = 0
        for k in range(len(route)-1):
            check += ground[route[k]][route[k+1]]

            if check >= result and result != 0:            # 가지치기
                break

        if result == 0:                                  # 처음 값은 무조건 받는다
            result = check
        elif check < result:                        # 다음부턴 작을때만 받는다
            result = check

    print(f'#{t} {result}')