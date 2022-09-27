'''


'''
import sys;sys.stdin = open('swea_6485_삼성시의버스노선.txt', 'r')

test = int(input())

for t in range(1, test + 1):
    stop = [0 for _ in range(5001)]

    n = int(input())

    bus = []            # 버스 노선
    for _ in range(n):
        bus.append(list(map(int, input().split())))

    for b in bus:       # 정류장에 버스 개수 체크
        for ck in range(b[0], b[1]+1):
            stop[ck] += 1

    p = int(input())
    want = []           # 보고 싶은 버스 정류장 번호
    for _ in range(p):
        want.append(int(input()))

    print(f'#{t} ', end='')
    for r in want:
        print(f'{stop[r]} ', end='')
    print()