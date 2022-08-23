import sys

input = sys.stdin.readline

n = int(input())

a = [0] * 10001
for i in range(n):
    num = int(input())
    a[num] = a[num] + 1

for k, v in enumerate(a):
    if v != 0:
        for i in range(v):
            print(k)