import sys
sys.stdin = open("swea_1231_중위순회.txt", "r")

# 중위순회 - 완전 이진 트리
def inorder(k = 1):
    if k <= n:
        inorder(2 * k)
        print(tree[k], end='')
        inorder(2 * k + 1)

test = 10
for t in range(1, test + 1):
    n = int(input())
    tree = [0 for i in range(n + 1)]

    for i in range(n):
        a, spell, *b = map(str, input().split())
        a = int(a)
        tree[a] = spell

    print(f'#{t} ', end='')
    inorder()
    print()