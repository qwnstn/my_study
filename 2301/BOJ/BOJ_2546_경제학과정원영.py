import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    input()
    N, M = map(int, input().split())

    C = list(map(int, input().split()))
    C.sort()
    E = list(map(int, input().split()))

    C_avr = sum(C) / N
    E_avr = sum(E) / M

    result = 0
    for i in C:
        if i < C_avr and i > E_avr:
            result += 1

    print(result)