import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n, T = map(int, input().split())

    # 신호등의 주기는 a초
    # 각 주기의 첫 b초동안 켜져 있다.
    # 신호등의 전원은 c초에 켜져 그때부터 작동을 시작한다.
    # 횡단보도를 건너는 데에는 d초가 걸린다.
    abcd = []   # [ [a, b, c, d] ...], n개
    D = 0
    for i in range(n):
        a, b, c, d = map(int, input().split())
        abcd.append([a, b, c, d])
        D += d

    e = list(map(int, input().split())) # n+1개
    E = sum(e)

    start_time = T - D - E  # 이 안에 출발 못하면 불가능
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
    0 <= t - (c+ax) <= b - d
    
    '''

    # 신호등의 주기는 a초
    # 각 주기의 첫 b초 동안 켜져 있다.
    # 신호등의 전원은 c초에 켜져 그때부터 작동을 시작한다.
    # 횡단보도를 건너는 데에는 d초가 걸린다.

    # 거꾸로 돌아가는 방식
    result = 'YES'

    time = T - e[-1]    # 총 걸린시간, 결과적으로 T가 되어야함
    for i in range(1, n+1):
        time -= abcd[-i][3]

        # 주기의 나머지에 건너는 시간을 더한 값이 건너는 신호등의 청색 신호(b)보다 길어지면
        # 건너는 시간(d)을 확보할 때 까지 시간을 줄인다. 나머지 + d = b
        # 시간을 늘일 순 없다.
        if time < abcd[-i][2] + abcd[-i][0]:
            result = 'NO'
            break

        # ck = (time - (c+a)) % (a+b)
        ck = (time - (abcd[-i][2] + abcd[-i][0])) % (abcd[-i][0] + abcd[-i][1])

        if ck + abcd[-i][3] > abcd[-i][1]:
            time += abcd[-i][1] - abcd[-i][3] - ck
            start_time += abcd[-i][1] - abcd[-i][3] - ck

        # 신호등이 켜져있지 않으면 중단
        if start_time < 0 or time < 0:
            result = 'NO'
            break

        time -= e[-i-1]

    if time < 0:
        result = 'NO'

    print(result)