import sys
sys.setrecursionlimit(1001)

def angry(N):
    if N < 3:
        return memo[N]
    if memo[N] == -1:
        memo[N] = angry(N - 1) + angry(N - 2) * 2
    return memo[N]



N = int(input())
memo = [-1] * (N + 1)          # [-1, -1, -1, ..., -1]
memo[0] = 0                    # [ 0, -1, -1, ..., -1]
memo[1] = 1                    # [ 0,  1, -1, ..., -1]
if N >= 2:
    memo[2] = 3                    # [ 0,  1,  3, ..., -1]
print(angry(N) % 10007)