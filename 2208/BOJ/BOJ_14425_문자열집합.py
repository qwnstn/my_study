'''
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
'''
import sys

n, m = map(int, input().split())

S = {sys.stdin.readline().strip() for i in range(n)}
M_list = [sys.stdin.readline().strip() for i in range(m)]
M = set(M_list)

SM = (S & M)

result = 0
for i in SM:
    result = result + M_list.count(i)

print(result)