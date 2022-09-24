'''
김 프로는 수영장을 이용한다.

김 프로는 지출이 너무 많아 내년 1년 동안 각 달의 이용 계획을 수립하고 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 있다.

수영장에서 판매하고 있는 이용권은 아래와 같이 4 종류이다.

   ① 1일 이용권 : 1일 이용이 가능하다.

   ② 1달 이용권 : 1달 동안 이용이 가능하다. 1달 이용권은 매달 1일부터 시작한다.

   ③ 3달 이용권 : 연속된 3달 동안 이용이 가능하다. 3달 이용권은 매달 1일부터 시작한다.
       (11월, 12월에도 3달 이용권을 사용할 수 있다 /
       다음 해의 이용권만을 구매할 수 있기 때문에
       3달 이용권은 11월, 12월, 1윌 이나 12월, 1월, 2월 동안 사용하도록 구매할 수는 없다.)

   ④ 1년 이용권 : 1년 동안 이용이 가능하다. 1년 이용권은 매년 1월 1일부터 시작한다.

   각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때,

   가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력하는 프로그램을 작성하라.
'''
'''
한 달의 횟수가 한달권 // 일일권 보다 같거나 크면 한달권이 이득

세 달의 횟수가 세달권 // 일일권 보다 같거나 크면 세달권이 이득
세달권이 한달권 * 횟수 보다 크면 세달권이 이득

1년권은 상한선 
'''

import sys
sys.stdin = open("swea_1952_수영장.txt", "r")

test = int(input())

for t in range(1, test + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    total = [0 for i in range(12)]


    # 일일권 가격
    for i in range(12):
        total[i] = price[0] * plan[i]                     #(price[0] * plan[i])


    # 한달권 가격
    for i in range(12):
        if total[i] > price[1]:
            total[i] = price[1]


    # 세달권 가격
    # 두 달 이하는 비교 x
    # 세 달 ~ 다섯 달 = 맥스값을 찾아 비교
    # 여섯 달 ~ 8달은? 상관 없음

    result = 0

    for i in range(4):
        threemonths = []
        for i in range(len(total)-2):
            threemonths.append(total[i] + total[i+1] + total[i+2])
        if max(threemonths) >= price[2]:
            result = result + price[2]
            total.pop(threemonths.index(max(threemonths)))
            total.pop(threemonths.index(max(threemonths)))
            total.pop(threemonths.index(max(threemonths)))



    # 1년권보다 비싸면
    result = result + sum(total)
    if result > price[3]:
        result = price[3]

    print(f'#{t} {result}')