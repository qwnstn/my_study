'''
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨)
이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.

'''

'''
좌우로 한 줄 씩 늘리고 윗줄에 한 줄 추가후 시작
'''

import sys
sys.stdin = open("swea_1210_ladder1.txt", "r")

for t in range(1, 11):
    n = int(input())

    lad = [[0]*102]
    for i in range(100):
        a = [0] + list(map(int, input().split())) + [0]
        lad.append(a)

    position = (100, lad[-1].index(2))                      # 초기값 (행 번호, 열 번호)

    # 올라가고 탐색하는 순서
    # 올라간다 = (x유지, y감소)
    # 위에 도착하면 종료
    while lad[position[0]][position[1]] != 0:
        position = (position[0] -1, position[1])                        # 위로 한 칸
        
        if lad[position[0]][position[1] -1] == 1:                       # 좌측이 1
            while lad[position[0]][position[1] -1] != 0:
                position = (position[0], position[1] -1)
        elif lad[position[0]][position[1] +1] == 1:                     # 우측이 1
            while lad[position[0]][position[1] +1] != 0:
                    position = (position[0], position[1] + 1)

    print(f'#{t} {position[1]-1}')                                      # 좌측에 1열 추가로 밀렸으니 마지막에 빼주기