import sys

n, m = map(int, input().split())

N = dict()
for i in range(n):
    N[str(i+1)] = sys.stdin.readline().rstrip()

N_reverse = dict()
for k, v in N.items():
    N_reverse[v] = k

for i in range(m):
    M = sys.stdin.readline().rstrip()
    if 48 <= ord(M[-1]) <= 57:  # 번호일 때
        print(N[M])
    else:
        print(N_reverse[M])

# M = [sys.stdin.readline().rstrip() for i in range(m)]
#
# for i in M:             # 번호일 때 단어 출력, 반대도 가능
#     if 48 <= ord(i[-1]) <= 57:          # 번호일 때
#         print(N[int(i) -1])
#     else:
#         print(N.index(i) +1)