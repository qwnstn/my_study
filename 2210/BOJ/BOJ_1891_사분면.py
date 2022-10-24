'''
오른쪽으로 이동한 경우 x가 양수, 왼쪽으로 이동한 경우 음수이며, 그 절댓값은 오른쪽 왼쪽 방향 이동 횟수를 나타낸다.
위쪽으로 이동한 경우 y가 양수, 아래쪽으로 이동한 경우 음수
'''
# 숫자를 좌표로 나타내기
def ntodot(ck, s1,e1,s2,e2): # n의 자릿수, 행(시작,끝), 열(시작,끝)
    global r, c
    if ck:
        if n[d-ck] == '2':
            ntodot(ck -1, s1, (s1+e1)//2, s2, (s2+e2)//2)
        elif n[d-ck] == '1':
            ntodot(ck - 1, s1, (s1+e1) // 2, (s2+e2)//2, e2)
        elif n[d-ck] == '3':
            ntodot(ck - 1, (s1+e1)//2, e1, s2, (s2+e2)//2)
        elif n[d-ck] == '4':
            ntodot(ck - 1, (s1+e1) // 2, e1, (s2+e2) // 2, e2)

    else:
        r = s1
        c = s2

# 좌표를 숫자로 나타내기
def dotton(f, r, c, s1, e1, s2, e2): # 필드 크기, 행, 열, 행(시작, 끝), 열(시작, 끝)
    global result
    if f >= 2:
        if s1 <= r < (s1 + e1)//2:
            if s2 <= c < (s2 + e2)//2:
                result += '2'
                dotton(f//2, r, c, s1, (s1+e1)//2, s2, (s2+e2)//2)
            elif (s2 + e2)//2 <= c < e2:
                result += '1'
                dotton(f // 2, r, c, s1, (s1+e1) // 2, (s2+e2) // 2, e2)
        elif (s1 + e1)//2 <= e1:
            if s2 <= c < (s2 + e2)//2:
                result += '3'
                dotton(f // 2, r, c, (s1+e1) // 2, e1, s2, (s2+e2)//2)
            elif (s2 + e2)//2 <= c < e2:
                result += '4'
                dotton(f // 2, r, c, (s1+e1) // 2, e1, (s2+e2) // 2, e2)


d, n = map(str, input().split())
d = int(d)
x, y = map(int, input().split())

r = c = 0
# r = 행(상하이동)
# c = 열(좌우이동)

maximum = 2**d
ntodot(d, 0, maximum, 0, maximum)
# print(r, c)
# print(r - y, c + x)

if 0 <= r - y < maximum and 0 <= c + x < maximum:
    result = ''
    dotton(maximum, r - y, c + x, 0, maximum, 0, maximum)
    print(result)
else:
    print(-1)