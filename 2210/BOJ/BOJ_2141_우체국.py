'''
N(1 ≤ N ≤ 100,000)          10만
|X[i]| ≤ 1,000,000,000      20억 
0 ≤ A[i] ≤ 1,000,000,000    10억
'''

import sys
input = sys.stdin.readline

n = int(input())

total = float('inf')
city = []
for i in range(n):
    x, a = map(int, input().split())
    city.append([x, a])

city.sort()
# print(city)

# 누적 인구 오름차순, 좌측 누적 인구
aup = [0]
atmp = 0
for idx in range(len(city)):
    atmp += city[idx][1]
    aup.append(atmp)

# 누적 인구 내림차순, 우측 누적 인구
adown = []
atmp = aup.pop()
for idx in range(len(city)):
    atmp -= city[idx][1]
    adown.append(atmp)

# print('좌측 aup',aup)
# print('우측 adown',adown)


result = [0]
# 변화량 = 상대 거리 * (좌측 인구수 - (우측 인구수 + 해당 마을 인구수))
tmp = 0

# 상대 거리 * 인구수
for idx in range(1, len(city)):   # 최대 10만
    tmp += (city[idx][0] - city[idx-1][0]) * ((aup[idx]) - (adown[idx-1]))
    result.append(tmp)

# print(result)
print(city[result.index(min(result))][0])