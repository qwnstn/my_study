import sys
input = sys.stdin.readline

n = int(input())

tree = {i:[] for i in range(1, n+1)}
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[v].append(u)
    tree[u].append(v)

# 리프 노드를 구분할 방법?
# dfs
stack = [(1, 0)]
ck = 0
while stack:
    idx, lv = stack.pop()
    if ck <
    for i in tree[idx]:
        stack.append((i, lv+1))
    ck = lv + 1
