'''
1. 총 8개의 숫자로 이루어져 있다.

2. 앞 7자리는 상품 고유의 번호를 나타내며, 마지막 자리는 검증 코드를 나타낸다.

    - 검증코드는 아래와 같은 방법으로 계산한다.

    “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수가 되어야 한다.

    상품 고유의 번호가 8801234일 경우,

    “( ( 8 + 0 + 2 + 4 ) x 3 ) + ( 8 + 1 + 3 ) + 검증 코드”

    = “42 + 12 + 검증 코드”

    = “54 + 검증 코드” 가 10 의 배수가 되어야 하므로, 검증코드는 6이 되어야 한다.

    즉, 88012346 이 정상적인 암호코드고, 그 외의 검증코드가 포함된 경우 비정상적인 암호코드다.
'''
'''
암호 코드 리스트 제작
리스트 요소마다 확인 실행
'''
# import time
# start = time.time()  # 시작 시간 저장
# import sys; sys.stdin = open('swea_1242_암호코드스캔.txt', 'r')

def findcode(num16):
    # 받은 16진암호 이진코드로 변경 후 맨 뒤에 슬라이싱용 '0' 붙이기, x = 이진 암호코드
    if num16:
        x = ''
        for k in num16:
            x += key[k]
        x = x.strip('0') + '0'
        # x = 코드 + '0'

        # 암호의 배율 찾기, ck = 배율
        ck = 0
        while True:
            ck += 1
            y = x[-1 -7*ck : -1]
            ckword = ''
            if y[0] == '0':
                for k in range(7):
                    a = k * ck
                    ckword += y[a]
                if password.get(ckword):        # 값이 맞으면 다른 값들도 확인
                    if ck == 1:
                        break
                    else:
                        escape = 1
                        for q in range(1, ck):
                            ckwordck = ''
                            for k in range(7):
                                a = k * ck
                                ckwordck += y[a+q]
                            if ckword == ckwordck:
                                escape += 1
                            else:
                                break
                        if escape == ck:
                            break


        # 배율에 따른 이진코드 길이 확인, 모자라면 0을 채운다
        if len(x) < 56 * ck + 1:
            x = x.zfill(56 * ck + 1)
            # x = 코드 + '0'

        # 이진코드화
        secret = ''
        for k in range(8):  # 이진코드의 각 숫자, 뒤에서 시작
            y = x[-1 - 7 * ck - 7 * ck * k:-1 - 7 * ck * k]
            ckword = ''
            for l in range(7):  # 숫자 이진암호 제작, 앞에서 시작
                ckword += y[l * ck]
            secret = password[ckword] + secret

        # 암호 검사, 맞으면 패스
        result = 0
        ckpassword = 0
        for k in range(len(secret)):
            if k % 2 == 1:
                ckpassword += int(secret[k])
                result += int(secret[k])
            else:
                ckpassword += int(secret[k]) * 3
                result += int(secret[k])
        if ckpassword % 10 != 0:
            result = 0

        # 2진 암호 16진으로 복구
        a = '000' + x[-1 - ck * 56:-1] + '0'
        if num16[-1] in ['2', '6', 'A', 'E']:
            a += '0'
        elif num16[-1] in ['4', 'C']:
            a += '00'
        elif num16[-1] == '8':
            a += '000'

        # code에 추가 (16진)
        codeck = 0
        code16 = ''
        while key_rev.get(a[-5 - codeck * 4:-1 - codeck * 4]):
            code16 = key_rev[a[-5 - codeck * 4:-1 - codeck * 4]] + code16
            codeck += 1
        code.append(code16.lstrip('0'))

        return result

    return 0


key = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100',
       '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001',
       'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

key_rev = {v:k for k, v in key.items()}

password = {'0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3', '0100011':'4',
            '0110001':'5', '0101111':'6', '0111011':'7', '0110111':'8', '0001011':'9'}

test = int(input())

for t in range(1, test + 1):
    n, m = map(int, input().split())
    code = []  # 이미 찾은 16진 암호 저장용
    result = 0
    for _ in range(n):
        # 16진 암호의 좌우 '0' 제거하여 받기, 중복 제거하며 받기
        num16 = input().strip().strip('0')
        if num16:
            for i in code:
                num16 = (num16.replace(i, '0', 1)).strip('0')
            if num16:
                while True:
                    result += findcode(num16)     # 암호코드 추가 함수
                    for i in code:
                        num16 = (num16.replace(i, '0')).strip('0')
                    if num16 == '':
                        break

    print(f'#{t} {result}')