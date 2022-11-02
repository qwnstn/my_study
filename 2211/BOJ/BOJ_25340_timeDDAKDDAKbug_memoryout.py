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

    '''
    신호등이 켜져있어야 건널 수 있다.
    c + ax <= t <= c + ax + b - d

    이외엔 다 무시
    '''
    '''
    거꾸로 가기
    계산 순서
    T - 길 가는 시간 - 횡단보도 건너는 시간 - (기다리는 시간, 변동값) 
    '''

    time = list(range(e[0], start_time + e[0] + 1))  # 가능한 시간 목록
    time_tmp = set()  # 저장할 임시 시간 목록
    for i in range(1, n + 1):
        if not time:
            print('NO')
            break
        else:
            for t in time:
                if t < abcd[i][2]:
                    continue

                tmp = (t - abcd[i][2]) % abcd[i][0]
                b_c = abcd[i][1] - abcd[i][3]
                if 0 <= tmp <= b_c:
                    time_tmp.add(t + abcd[i][3] + e[i])
                else:
                    time_tmp.add(t + abcd[i][3] + e[i] + abcd[i][0] - tmp)

            time = list(time_tmp)
            time_tmp.clear()

    if T in set(time):
        print('YES')
    else:
        print('NO')