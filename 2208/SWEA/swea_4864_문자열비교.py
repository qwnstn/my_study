'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.


ABC

ZZZZZABCZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.


ABC

ZZZZAZBCZZZZZ

문자열이 일치하지 않으므로 0을 출력.
'''

import sys

sys.stdin = open("swea_4864_문자열비교.txt", "r")

test = int(input())

for t in range(1, test+1):
    n = input()
    m = input()

    if m.count(n) > 0:          # 카운트가 되면  '1'
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')