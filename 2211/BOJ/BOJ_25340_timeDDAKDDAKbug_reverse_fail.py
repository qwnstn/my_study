import sys
input = sys.stdin.readline

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
        ei += i
        E.append(ei)

    start_time = T - D[-1] - E[-1]  # 이 안에 출발 못하면 불가능
    if start_time < 0:
        print('NO')
        continue

    '''
    신호등이 켜져있어야 건널 수 있다.
    c + ax <= t <= c + ax + b - d
    
    이외엔 다 무시
    '''
    '''
    거꾸로 가기
    계산 순서
    T - 길 가는 시간 - 횡단보도 건너는 시간 - (기다리는 시간, 변동값) 
    
            (t - c1) % a1 <= b1 - d1
            -(a1 - (b1 - d1)) <= t % a1 - c % a1 <= b1 - d1 
            t = t + d1
            (t - c2) % a2 <= b2 - d2
    
    '''

    # 신호등의 주기는 a초
    # 각 주기의 첫 b초동안 켜져 있다.
    # 신호등의 전원은 c초에 켜져 그때부터 작동을 시작한다.
    # 횡단보도를 건너는 데에는 d초가 걸린다.
    start = end = T
    for i in range(1, n+1):
        a = abcd[-i][0]
        b = abcd[-i][1]
        c = abcd[-i][2]
        d = abcd[-i][3]

        end -= e[-i] + d
        if end < c:
            start = -1
            end = -2
            break
        tmp = (end - c) % a
        if tmp > b - d:
            end += -tmp + b - d

        start -= e[-i] + d
        if start < c:
            start = c
            continue
        tmp = (start - c) % a
        if c + tmp == start:
            start = c
        else:
            start += -tmp -a + b

    start = max(start, e[0])
    end = min(end, start_time + e[0])
    mid = (start + end) // 2

    result = 'NO'
    while start < end:

        for i in range(1, n+1):
            a = abcd[i][0]
            b = abcd[i][1]
            c = abcd[i][2]
            d = abcd[i][3]

            if ck < c:
                ck = c + d + e[i]
                if ck + (D[-1] - D[n]) + (E[-1] - E[n]) > T or ck > T:
                    break
                continue

            tmp = (ck - c) % a
            if 0 <= tmp <= b-d:
                ck += d + e[i]
            else:
                ck += -tmp + a + d + e[i]

            if ck + (D[-1]-D[n]) + (E[-1]-E[n]) > T or ck > T:
                break

        if ck > T:
            break
        if ck == T:
            result = 'YES'
            break

    print(result)