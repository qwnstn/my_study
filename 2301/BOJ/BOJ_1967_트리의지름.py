import sys

input = sys.stdin.readline

n = int(input())

tree = {i:[] for i in range(1, n+1)}
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)