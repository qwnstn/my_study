'''
0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.

신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고, 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.

당일 시작, 다음날 끝나는 것은?

* 반례 : 짧은 것이 긴 것 두개에 걸친다면? - 해결 못함
'''
import sys;sys.stdin = open('swea_5202_화물도크.txt', 'r')


test = int(input())

for t in range(1, test + 1):
    n = int(input())

    total = []
    for i in range(n):
        s, e = map(int, input().split())

        if e > s:                   # l은 걸린 시간
            l = e - s
        else:
            l = e - s + 24

        total.append([l, s, e])

    total.sort(key=lambda x:x[0])   # 작업 시간 순 정렬

    ck = set()                      # 작업 시간 저장용
    result = 0
    for i in total:
        escape = 0
        for k in range(i[1], i[1] + i[0]):  # 작업 시간이 걸리면 해당 작업 패스
            if k in ck:
                escape = 1
                break

        if escape:
            continue

        for k in range(i[1], i[1] + i[0]):  # 작업 시간 추가
            ck.add(k)

        result += 1                         # 작업량 추가

    print(f'#{t} {result}')