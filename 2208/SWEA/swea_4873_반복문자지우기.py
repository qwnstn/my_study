'''
문자열 s에서 반복된 문자를 지우려고 한다.
지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.


다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.


CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.

CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.

CAA 연속 문자 AA를 지운다.

C 1글자가 남았으므로 1을 리턴한다.
'''

import sys

sys.stdin = open("swea_4873_반복문자지우기.txt", "r")

test = int(input())

for t in range(1, test+1):
    word = input()
    result = [word[-1]]
    try:
        ck = 1
        while True:
            ck = ck + 1
            if result == []:                # 비어있으면 넣고 반복문 재실행
                result.append(word[-ck])
                continue

            if result[-1] == word[-ck]:     # 같으면 제거
                result.pop()
            else:
                result.append(word[-ck])    # 다르면 넣기

    except IndexError:
        print(f'#{t} {len(result)}')
