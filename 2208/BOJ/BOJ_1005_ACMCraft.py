'''
1
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7

120
39

BFS로 하고 n번 건물에 필요한 건물 번호를 넣어서 최대값만 더해가는 식으로 만들기
'''

test = int(input())

for t in range(test):
    n, k = map(int, input().split())

    d = list(map(int, input().split()))
    dn = {}
    for i in range(1, n+1):
        dn[i] = d[i-1]

    arr = [[] for i in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[x-1].append(y)

    