def backtrack(row, n, temp):
    global mini             # 전역 변수 최솟값 mini
    if len(stack) == n:     # stack의 길이가 n과 같아지면
        if temp < mini:         # 임시 합 temp가 현재 최솟값 mini보다 작을 때
            mini = temp             # mini 갱신
    elif mini < temp:       # 가지치기 Pruning: 현재 최솟값 mini보다 임시합이 커지면 길이와 상관없이 재귀 함수 중단
        return
    else:                   # stack에 중복을 허용하지 않는 순열 생성
        for i in range(n):
            if i not in stack:
                stack.append(i)
                # 다음 줄로 넘어가고, arr에서 아래 행과 열에 맞는 값을 찾아서 임시합 갱신
                # 행=(현재 backtrack에 입력된 row값), 열=(새로 추가된 순열의 숫자)
                backtrack(row + 1, n, temp + arr[row][stack[-1]])
                stack.pop()

import sys
sys.stdin = open('swea_4881_배열최소합.txt', 'r')


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    # N일 때 최댓값으로 초기값 설정
    mini = 9 * N
    backtrack(0, N, 0)

    print(f'#{t} {mini}')


# def dfs(n):
#     if len(stack) == n:
#         perms.append(stack[:])
#         return
#
#     for i in range(n):
#         if i not in stack:
#             stack.append(i)
#             dfs(n)
#             stack.pop()
#
#     for p in perms:
#         temp = 0
#         for idx in range(N):
#             temp += arr[idx][p[idx]]
#         if temp < arr_min:
#             arr_min = temp

'''
1
3
2 1 2
5 8 5
7 2 2
'''