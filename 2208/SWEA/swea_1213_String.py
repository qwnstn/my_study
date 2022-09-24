'''
주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.

Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.

위 문장에서 ti 를 검색하면, 답은 4이다.
'''

import sys
sys.stdin = open("swea_1213_String.txt", "rt", encoding='UTF8')

for t in range(1, 11):
    want = input()                 # 쓸모 없는 값
    want = input()
    wooord = input()
    result = wooord.count(want)

    print(f'#{t} {result}')