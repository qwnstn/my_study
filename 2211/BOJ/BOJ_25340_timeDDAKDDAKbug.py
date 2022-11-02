import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n, T = map(int, input().split())

    abcd = [[0]]  # [[0], [a, b, c, d] ...], n+1개, 인덱스 번호용 [0]
    D = 0
    for i in range(n):
        a, b, c, d = map(int, input().split())
        abcd.append([a, b, c, d])
        D += d

    e = list(map(int, input().split()))  # n+1개

    E = sum(e)

    start_time = T - D - E  # 이 안에 출발 못하면 불가능
    if start_time < 0:
        print('NO')
        continue

    # 신호등의 주기는 a초
    # 각 주기의 첫 b초동안 켜져 있다.
    # 신호등의 전원은 c초에 켜져 그때부터 작동을 시작한다.
    # 횡단보도를 건너는 데에는 d초가 걸린다.

    start = e[0]
    end = start_time + e[0]
    mid = (start + end) // 2
    for i in range(1, n+1):
        a = abcd[i][0]
        b = abcd[i][1]
        c = abcd[i][2]
        d = abcd[i][3]

        if start < c:
            start = c + d + e[i]
        else:
            tmp = (start - c) % a
            if tmp + d <= b:
                start += d + e[i]
            else:
                start += a - tmp + d + e[i]

        tmp = (mid - c) % a
        if tmp + d <= b:
            mid += d + e[i]
        else:
            mid += a - tmp + d + e[i]

        if end < c:
            result = 'NO'
            break
        else:
            tmp = (end - c) % a
            if tmp + d <= b:
                end += d + e[i]
            else:
                end += a - tmp + d + e[i]

    ck = set(range(start, end+1))
    print(ck)
    if T in ck:
        print('YES')
    else:
        print('NO')
        
    # 필요한것 : 어떻게 구분하는가?