
import sys
sys.stdin = open('swea_5102_노드의거리.txt', 'r')

def bfs(s, g):
    visited[s] = 0
    q = [s]
    while q:
        v = q.pop(0)
        if v == g:
            return visited[v]
        for w in arr[v]:
            if visited[w] == -1:
                visited[w] = visited[v] + 1
                q.append(w)
    return 0

test = int(input())

for t in range(1, test + 1):
    v, e = map(int, input().split())

    arr = [[] for i in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)                                # [[], [2,3], [1,4], [1,4,5,6], [2,3]]

    s, g = map(int, input().split())

    visited = [-1 for i in range(v+1)]                   # [0, 0, 0, 0]

    print(f'#{t} {bfs(s, g)}')