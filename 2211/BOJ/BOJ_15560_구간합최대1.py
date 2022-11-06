'''
개선점
더 빠르게 해야 하는데..

'''
import sys
input = sys.stdin.readline

N, Q, U, V = map(int, input().split())
K = list(map(int, input().split()))

tmp = V
UK = [V] # 누적합
for i in range(N):
    tmp += U * K[i] + V
    UK.append(tmp)
# print('K', K)
# print('UK', UK)
'''
max(U*(Ki + ... + Kj) + V*(j-i))
=max(U*kj+V + ... + U*Ki+V - V)

'''

for _ in range(Q):
    C, A, B = map(int, input().split())

    if C:
        K[A-1] = B
        tmp = UK[A-1]
        for i in range(A-1, N):
            tmp += U * K[i] + V
            UK[i+1] = tmp
        # print(A)
        # print(K)
        # print(UK)

    else:
        result = float('-inf')
        for i in range(A, B+1):
            if i == A:
                tmp = K[i-1] * U
            else:
                tmp = UK[i] - min(UK[A-1:i]) - V
            if tmp > result:
                result = tmp
        print(result)