'''
N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다.
정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다.
정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

재귀형식으로 하니 깊이 제한을 몰라서 틀림
'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs():
    global ck

    p = stack.pop()
    if not visited[p[0]]:
        ck += 1
        visited[p[0]] = ck
        if graph.get(p[0]):
            for i in graph.get(p[0]):
                stack.append([i, ck])

            while stack:
                dfs()

n, m, r = map(int, input().split())
# 정점 수, 간선 수, 시작 지점

graph = dict()
for _ in range(m):
    u, v = map(int, input().split())

    if graph.get(u):
        graph[u] += [v]
    else:
        graph[u] = [v]

    if graph.get(v):
        graph[v] += [u]
    else:
        graph[v] = [u]

for v in graph.values():
    v.sort(reverse=True)

ck = 0
stack = [[r, 1]]
visited = [0 for i in range(n+1)]
dfs()

for i in range(1, n+1):
    print(visited[i])