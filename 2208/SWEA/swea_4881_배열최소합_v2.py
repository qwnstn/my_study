def dfs(n):
    global total_max
    global ck
    global temp

    if len(stack) == n:
        if temp < total_max:
            total_max = temp
        return

    for i in range(n):
        if i not in stack:
            ck = ck + 1
            stack.append(i)
            temp = temp + arr[ck][stack[ck]]
            if temp > total_max:
                temp = temp - arr[ck][stack[ck]]
                ck = ck - 1
                stack.pop()
                return
            dfs(n)
            temp = temp - arr[ck][stack[ck]]
            ck = ck - 1
            stack.pop()

import sys
sys.stdin = open('swea_4881_배열최소합.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    stack = []
    total_max = 10 * N
    ck = -1
    temp = 0
    dfs(N)

    print(f'#{t} {total_max}')