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

    ck = 0
    for i in range(len(wooord)-len(want)):
        for k in range(len(want)):
            if wooord[i+k] != want[k]:
                break
            elif wooord[i+k] == want[k]:
                if k == len(want)-1:            # k 가 마지막 번호일 때
                    ck = ck + 1

    print(f'#{t} {ck}')