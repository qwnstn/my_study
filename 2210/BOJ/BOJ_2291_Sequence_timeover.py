def time(d, s, m):    # d=깊이, for문 시작, m
    global ck

    if d != 1:
        for i in range(s, (m//d)+1):
            result[-d] = i
            time(d-1, i, m-i)
            if ck == k:
                return
    else:
        result[-d] = m
        ck += 1
        return 


n, m, k = map(int, input().split())
# 길이, 합, 순번

if n == 1:
    print(m)
else:
    result = [0 for i in range(n)]
    ck = 0
    time(n, 1, m)

print(*result)