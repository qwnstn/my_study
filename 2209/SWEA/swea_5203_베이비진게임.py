'''
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.

'''

import sys;sys.stdin=open('swea_5203_베이비진게임.txt', 'r')

test = int(input())

for t in range(1, test + 1):
    card = list(map(int, input().split()))

    p1 = {i:0 for i in range(10)}
    p2 = {i:0 for i in range(10)}

    p1ck = [[], []]
    p2ck = [[], []]     # 연속 숫자, 같은 값이 2개

    result = 0                              # 무승부면 0
    for i in range(len(card)):
        if i % 2 == 0:
            if card[i] in p1ck[1]:          # 같은 값이 2개인 숫자를 뽑으면 결과확인
                result = 1
                break

            if card[i] not in p1ck[0]:      # 새로운 수를 뽑으면
                p1ck[0].append(card[i])
                p1ck[0].sort()              # 연속 숫자에 넣고 정렬
                if len(p1ck[0]) >= 3:
                    escape = 0
                    for k in range(len(p1ck[0])-2): # 연속되는 숫자인지 확인
                        if p1ck[0][k] + 2 == p1ck[0][k+1] + 1 and p1ck[0][k+1] + 1 == p1ck[0][k+2]:
                            result = 1
                            escape = 1
                            break
                    if escape == 1:
                        break

            p1[card[i]] += 1
            if p1[card[i]] == 2:
                p1ck[1].append(card[i])


        else:
            if card[i] in p2ck[1]:
                result = 2
                break

            if card[i] not in p2ck[0]:
                p2ck[0].append(card[i])
                p2ck[0].sort()
                if len(p2ck[0]) >= 3:
                    escape = 0
                    for k in range(len(p2ck[0]) - 2):
                        if p2ck[0][k] + 2 == p2ck[0][k+1] + 1 and p2ck[0][k+1] + 1 == p2ck[0][k+2]:
                            result = 2
                            escape = 1
                            break
                    if escape == 1:
                        break

            p2[card[i]] += 1
            if p2[card[i]] == 2:
                p2ck[1].append(card[i])



    print(f'#{t} {result}')