'''

16진수 1자리는 2진수 4자리로 표시된다.

N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.

단, 2진수의 앞자리 0도 반드시 출력한다.

예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

0100011111111110
'''

import sys; sys.stdin = open('swea_5185_이진수.txt', 'r')

key = {'0':0, '1':1, '2':2, '3':3, '4':4,
       '5':5, '6':6, '7':7, '8':8, '9':9,
       'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

test = int(input())

for t in range(1, test + 1):
    n, num = map(str, input().split())

    result = ''
    for i in num:
        x = bin(key[i])[2:]
        while len(x) != 4:
            x = '0' + x
        result += x

    print(f'#{t} {result}')