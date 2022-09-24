'''
스파이의 암호 코드에 다음과 같은 규칙이 있음을 발견했다.


1. 암호코드는 8개의 숫자로 이루어져 있다.

2. 올바른 암호코드는 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수가 되어야 한다.

    ex) 암호코드가 88012346일 경우,
    ( ( 8 + 0 + 2 + 4 ) x 3 ) + ( 8 + 1 + 3 + 6) = 60은 10의 배수이므로 올바른 암호코드다.

    ex) 암호코드가 19960409일 경우,
    ( ( 1 + 9 + 0 + 0 ) x 3 ) + ( 9 + 6 + 4 + 9) = 58은 10의 배수가 아니므로 잘못된 암호코드다.

'''

import sys
sys.stdin = open('swea_1240_단순2진암호코드.txt', 'r')

key = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
       '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

test = int(input())

for t in range(1, test + 1):
    n, m = map(int, input().split())

    for i in range(n):
        x = list(map(int, input().split()))
        if x != [0]:
            while x[0] % 10 == 0:
                x[0] //= 10
            code = '000000' + str(x[0]) + '0'

    result = 0
    ckcode = 0
    for i in range(8):
        a = code[-8-(7*i):-1-(7*i)]
        result += key[a]
        if i % 2 == 0:
            ckcode += key[a]
        else:
            ckcode += key[a] * 3

    if ckcode % 10 == 0:
        print(f'#{t} {result}')
    else:
        print(f'#{t} 0')