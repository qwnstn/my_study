import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = list(map(int, input().split()))

score_list = [0 for i in range(10001)]

for i in score:
    score_list[i] += 1

ck = -1
student = 0
while student < k:
    ck += 1
    student += score_list[10000 - ck]


print(10000 - ck)