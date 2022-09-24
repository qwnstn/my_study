'''
양의 정수 N에 대해 N = X**3가 되는 양의 정수X 를 구하여라.

3.0                 # 27
19.81241271808882   # 7777
3.9999999999999996  # 64

부동소수점에 의해 실제 값보다 모자랄 수 있음
'''

import sys

sys.stdin = open("swea_5688_세제곱근을찾아라.txt", "r")

test = int(input())

for t in range(1, test + 1):
    n = int(input())

    x1 = int(n**(1/3))               
    x2 = int(n**(1/3)) + 1          # 값을 두 개를 받는다
    
    if n == x1**3:
        result = x1
    elif n == x2**3:
        result = x2
    else:
        result = -1

    print(f'#{t} {result}')