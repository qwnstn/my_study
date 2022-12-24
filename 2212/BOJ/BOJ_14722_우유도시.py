import pprint
import sys
input = sys.stdin.readline

n = int(input())
ground = [list(map(int, input().split())) for _ in range(n)]

visited = [[[float('-inf'), float('-inf'), float('-inf')] for _ in range(n)] for _ in range(n)]
# 0, 1, 2

for i in range(n):
    for k in range(n):
        a1, b1, c1 = visited[i-1][k][0], visited[i-1][k][1], visited[i-1][k][2]
        a2, b2, c2 = visited[i][k-1][0], visited[i][k-1][1], visited[i][k-1][2]

        if ground[i][k] == 0:
            visited[i][k] = [max(c1+1, c2+1, a1, a2), max(b1, b2), float('-inf')]
            if max(visited[i][k]) < 0:
                visited[i][k] = [1, float('-inf'), float('-inf')]
        elif ground[i][k] == 1:
            visited[i][k] = [float('-inf'), max(a1+1, a2+1, b1, b2), max(c1, c2)]
        elif ground[i][k] == 2:
            visited[i][k] = [max(a1, a2), float('-inf'), max(b1+1, b2+1, c1, c2)]

pprint.pprint(visited)
print(max(visited[n-1][n-1])) if max(visited[n-1][n-1]) != float('-inf') else print(0)