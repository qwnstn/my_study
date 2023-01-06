import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    maximum = n
    while n != 1:
        if n % 2:
            n = n * 3 + 1
            if maximum < n:
                maximum = n
        else:
            n //= 2
    print(maximum)