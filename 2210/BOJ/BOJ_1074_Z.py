def Zzz(n, r, c, s1, e1, s2, e2):  # n, r, c, 행(시작점, 끝나는점), 열(시작점, 끝나는점)
    global four
    if n:
        if s1 <= r < (s1 + e1) // 2:
            if s2 <= c < (s2 + e2) // 2:
                four += '0'
                Zzz(n-1, r, c, s1, (s1 + e1)//2, s2, (s2 + e2)//2)
            else:
                four += '1'
                Zzz(n-1, r, c, s1, (s1 + e1)//2, (s2 + e2)//2, e2)
        else:
            if s2 <= c < (s2 + e2) // 2:
                four += '2'
                Zzz(n-1, r, c, (s1 + e1) // 2, e1, s2, (s2 + e2)//2)
            else:
                four += '3'
                Zzz(n-1, r, c, (s1 + e1) // 2, e1, (s2 + e2)//2, e2)

n, r, c= map(int, input().split())

four = ''
Zzz(n, r, c, 0, 2**n, 0, 2**n)

result = 0
for i in range(1, len(four)+1):
    result += int(four[-i]) * 4 ** (i-1)

print(result)