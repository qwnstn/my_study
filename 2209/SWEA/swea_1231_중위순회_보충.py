def inorder(k = 1):
    if k <= n:
        inorder(k * 2)
        print(tree[str(k)][0], end='')
        inorder(k * 2 + 1)

test = 10

for t in range(1, test + 1):
    n = int(input())

    tree = dict()
    for i in range(n):
        a, b, *c = map(str, input().split())
        tree[a] = [b, *c]

    print(f'#{t} ', end='')
    inorder()
    print()