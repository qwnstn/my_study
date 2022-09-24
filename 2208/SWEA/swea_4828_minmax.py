# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

import sys
sys.stdin = open("minmax.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    a = list(map(int, input().split()))

    maximum = a[0]
    minimum = a[0]
    for i in range(1, n):
        if a[i] > maximum:
            maximum = a[i]
        if a[i] < minimum:
            minimum = a[i]

    print(f'#{test_case} {maximum - minimum}')