'''
0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.

N = 0.625
0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625

N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고,
13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.
'''

import sys; sys.stdin = open('swea_5186_이진수2.txt', 'r')

test = int(input())

for t in range(1, test + 1):
    n = float(input())

    result = ''
    ck = 0
    while ck != 13:
        ck += 1
        if n - 2**-ck > 0:
            n -= 2**-ck
            result += '1'
        elif n - 2**-ck < 0:
            result += '0'
        elif n - 2**-ck == 0:
            result += '1'
            break

    if ck == 13:
        print(f'#{t} overflow')
    else:
        print(f'#{t} {result}')