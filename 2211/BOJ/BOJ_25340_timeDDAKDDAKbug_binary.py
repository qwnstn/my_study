import sys
input = sys.stdin.readline

def check(z):   # z가 T를 넘는지 확인
    for k in range(1, n + 1):
        a = abcd[k][0]
        b = abcd[k][1]
        c = abcd[k][2]
        d = abcd[k][3]

        if z < c:
            z = c
        elif (z - c) % a > b - d:
            z += a - ((z - c) % a)

        z += d + e[k]

        if z + (D[-1] - D[k]) + (E[-1] - E[k]) > T or z > T:
            return 'high'

    if z > T:
        return 'high'
    elif z < T:
        return 'low'
    else:
        return 'YES'


tc = int(input())

for _ in range(tc):
    n, T = map(int, input().split())

    # 신호등의 주기는 a초
    # 각 주기의 첫 b초동안 켜져 있다.
    # 신호등의 전원은 c초에 켜져 그때부터 작동을 시작한다.
    # 횡단보도를 건너는 데에는 d초가 걸린다.
    abcd = [[0]]  # [[0], [a, b, c, d] ...], n+1개, 인덱스 번호용 [0]
    D = [0]
    di = 0
    for i in range(n):
        a, b, c, d = map(int, input().split())
        abcd.append([a, b, c, d])
        di += d
        D.append(di)

    e = list(map(int, input().split()))  # n+1개

    E = []
    ei = 0
    for i in range(n+1):
        ei += e[i]
        E.append(ei)

    start_time = T - D[-1] - E[-1]  # 이 안에 출발 못하면 불가능

    if start_time < 0:
        print('NO')
        continue

    s = e[0]
    end = start_time + e[0]
    m = (s + end) // 2

    if check(s) == 'high':
        print('NO')
        continue
    elif check(s) == 'YES':
        print('YES')
        continue
    elif check(end) == 'low':
        print('NO')
        continue
    elif check(end) == 'YES':
        print('YES')
        continue
    elif check(m) == 'YES':
        print('YES')
        continue

    result = 'NO'
    while s != end - 1:
        if check(m) == 'high':
            end = m
            m = (s + end) // 2
        elif check(m) == 'low':
            s = m
            m = (s + end) // 2
        elif check(m) == 'YES':
            result = 'YES'
            break

    print(result)
