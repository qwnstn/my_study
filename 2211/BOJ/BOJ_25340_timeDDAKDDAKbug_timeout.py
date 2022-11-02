import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n, T = map(int, input().split())

    # 신호등의 주기는 a초
    # 각 주기의 첫 b초동안 켜져 있다.
    # 신호등의 전원은 c초에 켜져 그때부터 작동을 시작한다.
    # 횡단보도를 건너는 데에는 d초가 걸린다.

    abcd = []   # [ [a, b, c, d] ...], n개, idx = 0 ~ n-1

    # 누적합
    D = []
    di = 0
    for i in range(n):
        a, b, c, d = map(int, input().split())
        abcd.append([a, b, c, d])
        di += d
        D.append(di)

    e = list(map(int, input().split())) # n+1개, idx = 0 ~ n

    # 누적합
    E = []
    ei = 0
    for i in e:
        ei += i
        E.append(ei)

    start_time = T - D[-1] - E[-1]  # 이 안에 출발 못하면 불가능
    if start_time < 0:
        print('NO')
        continue

    '''
    횡단보도를 건너기 시작하는 시간
    1. 횡단보도가 모두 켜져 있다는 가정 하
    sum(e[:i+1]) + sum(abcd[:i][3])
    
    2. 켜져있지 않다면?
    c 초가 될 때 까지 기다려야한다

    번외. 신호등이 켜져있어야 건널 수 있다.
    c + ax <= t <= c + ax + b - d
    
    '''

    # 신호등의 주기는 a초
    # 각 주기의 첫 b초 동안 켜져 있다.
    # 신호등의 전원은 c초에 켜져 그때부터 작동을 시작한다.
    # 횡단보도를 건너는 데에는 d초가 걸린다.

    result = 'NO'
    time = -1
    while time <= start_time:
        time += 1

        ck = time   # 집에서 출발하는 시간
        escape = 0  # for문이 잘 돌았는지 확인하는 용도
        for i in range(n):  # i = 0 ~ n-1
            # 횡단보도 도착
            ck += e[i]

            # 횡단보도 건너기
            if ck < abcd[i][2]:
                # 신호등이 작동하기 전이라면
                ck = abcd[i][2]     # 신호등이 작동할 때 까지 대기
                ck += abcd[i][3]   # 횡단보도 건너기

            else:
                # 신호등이 작동하고 있다면

                if 0 <= (ck - abcd[i][2]) % abcd[i][0] <= abcd[i][1] - abcd[i][3]:
                    # 신호등을 바로 건널 수 있다면
                    ck += abcd[i][3]    # 횡단보도 건너기

                else:
                    # 신호등을 바로 못건너면

                    ck += abcd[i][0] - (ck - abcd[i][2]) % abcd[i][0]
                    # 건널 수 있을 때 까지 대기

                    ck += abcd[i][3]  # 횡단보도 건너기

            # 남은 시간동안 못간다면 중단
            if ck + (D[-1] - D[i]) + (E[-1] - E[i]) > T:
                break

            escape += 1

        if escape == n and ck == T - e[-1]:
            result = 'YES'
            break

    print(result)