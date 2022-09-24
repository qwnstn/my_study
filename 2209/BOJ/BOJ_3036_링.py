import sys

input = sys.stdin.readline

n = int(input())
ring = list(map(int, input().split()))

for i in range(1, n):
    a = ring[0]
    b = ring[i]

    while a * b != 0:
        if a >= b:
            a = a % b
        else:
            a, b = b, a

    if a:
        print(f'{ring[0] // b}/{ring[i] // b}')
    else:
        print(f'{ring[0] // b}/{ring[i] // b}')