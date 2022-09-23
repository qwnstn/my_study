import sys

def euc(a, b):              # 최대공약수 - 유클리드 호제법
    while a * b != 0:
        if a >= b:
            a = a % b
        else:
            a, b = b, a

    if a:
        return a
    else:
        return b

input = sys.stdin.readline

n = int(input())

total = []
for _ in range(n):
    total.append(int(input()))
total.sort()

ck = set()

semi_total = total[:]
for i in range(1, len(total)):      # [1]부터 [0]을 빼줌
    total[i] -= semi_total[i-1]

big = total[1]
for i in range(2, len(total)):
    big = euc(total[i], big)       # [1]과 [2]의 최대공약수

for i in range(1, int(big**0.5)+1):   # big의 약수들 구하기
    if big % i == 0:
        ck.add(i)
        ck.add(big // i)

ck = list(ck)

ck.sort()
ck.pop(0)
print(*ck)