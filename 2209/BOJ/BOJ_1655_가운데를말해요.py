'''
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

'''

import sys
import heapq
input = sys.stdin.readline

n = int(input())

h1 = [int(input())]     # 기준값보다 큰 값만 받고, 작은 수 정렬(h1[0] = 작은 수)
h2 = []                 # 기준값보다 작은 값만 받고, 큰 수 정렬(h2[0] = 큰 수)
heapq.heapify(h1)
heapq.heapify(h2)
print(h1[0])

for i in range(n-1):
    a = int(input())
    if a >= h1[0]:       # 기준 값보다 큰 값만 받는다.
        heapq.heappush(h1, a)
    else:               # 기준 값보다 작은 값만 역으로 받는다.
        heapq.heappush(h2, (-a, a))
        
    if len(h2) - len(h1) == 2:
        heapq.heappush(h1, heapq.heappop(h2)[1])
        result = h2[0][1]
    elif len(h2) - len(h1) in [0, 1]:
        result = h2[0][1]
    elif len(h2) - len(h1) == -1:
        result = h1[0]
    elif len(h2) - len(h1) == -2:
        result = heapq.heappop(h1)
        heapq.heappush(h2, (-result, result))

    print(result)