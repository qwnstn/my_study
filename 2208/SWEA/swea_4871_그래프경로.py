'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.

두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
'''
def dfs(v):
    # print(v)
    visited[v] = 1              # 방문하면 1 찍기
    for w in adjlist[v]:
        if visited[w] == 0:     # 1이 없으면
            dfs(w)

import sys

sys.stdin = open("swea_4871_그래프경로.txt", "r")

test = int(input())

for t in range(1, test+1):

    v, e = map(int, input().split())        # 0부터 v까지 노드, e개의 간선
                                            # 노드가 v+1 개
    adjlist = [[] for i in range(v+1)]      # 간선연결 리스트
    for i in range(e):                      # [[1,2]    a=0
        a, b = map(int, input().split())    # [3,4]     a=1
        adjlist[a].append(b)                # [4]]      a=2

    s, g = map(int, input().split())

    visited = [0] * (v+1)                   # 방문할 구역 미리 생성
    dfs(s)

    if visited[g] ==1:
        ck = 1
    else:
        ck = 0


    print(f'#{t} {ck}')