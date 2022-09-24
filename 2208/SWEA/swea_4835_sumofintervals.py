'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
'''


import sys
sys.stdin = open("sumofintervals.txt", "r")


t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))


    maximum = 0
    minimum = 0
    for k in range(m):
        maximum = maximum + a[k]
        minimum = minimum + a[k]


    for k in range(1, n - m + 1):
        sum = 0
        for x in range(m):
            sum = sum + a[k+x]
        if sum > maximum:
            maximum = sum
        if sum < minimum:
            minimum = sum

    print(f'#{i} {maximum - minimum}')