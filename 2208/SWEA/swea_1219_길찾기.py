'''
그림과 같이 도식화한 지도에서 A도시에서 출발하여 B도시로 가는 길이 존재하는지 조사하려고 한다.

길 중간 중간에는 최대 2개의 갈림길이 존재하고, 모든 길은 일방 통행으로 되돌아오는 것이 불가능하다.

다음과 같이 길이 주어질 때, A도시에서 B도시로 가는 길이 존재하는지 알아내는 프로그램을 작성하여라.

 - A와 B는 숫자 0과 99으로 고정된다.

 - 모든 길은 순서쌍으로 나타내어진다. 위 예시에서 2번에서 출발 할 수 있는 길의 표현은 (2, 5), (2, 9)로 나타낼 수 있다.

 - 가는 길의 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재하는 것이다.

 - 단 화살표 방향을 거슬러 돌아갈 수는 없다.
'''
def dfs(v):
    visited[v] = 1
    for w in adjlist[v]:
        if visited[w] == 0:
            dfs(w)


import sys
sys.stdin = open("swea_1219_길찾기.txt", "r")

try:

    while True:

        test, v = map(int, input().split())

        linelist = list(map(int, input().split()))

        adjlist = [[] for i in range(100)]
        for i in range(len(linelist)//2):
            a, b = linelist[i*2], linelist[i*2 +1]
            adjlist[a].append(b)

        visited = [0] * (100)
        dfs(0)

        if visited[99] == 1:
            ck = 1
        else:
            ck = 0

        print(f'#{test} {ck}')
except:
    pass