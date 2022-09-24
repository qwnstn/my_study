import sys
sys.stdin = open("swea_5178_노드의합.txt", "r")

test = int(input())

for t in range(1, test + 1):
    n, m, l = map(int, input().split())

    tree = [0 for i in range(n + 2)]

    for i in range(m):
        a, b = map(int, input().split())
        tree[a] = b

    for i in range(n - m, 0, -1):
        if tree[i] == 0:
            tree[i] = tree[i * 2] + tree[i * 2 + 1]

    print(f'#{t} {tree[l]}')