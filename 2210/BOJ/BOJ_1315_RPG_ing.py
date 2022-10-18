import sys
input = sys.stdin.readline

def upgrade(q, ):


z = [1, 1]  # 준규 [str, int]

n = int(input())

quest = []
for _ in range(n):
    s, i, pnt = map(int, input().split())
    quest.append([s, i, pnt])

s_quest = sorted(quest, key=lambda x: (x[0], -x[2]))
i_quest = sorted(quest, key=lambda x: (x[1], -x[2]))

result = 0
rst = 0
for q in range(len(quest)):
    if z[0] >= s_quest[q][0]:
        # 힘 비교
        result += 1
        rst += s_quest[q][2]

    elif z[1] >= i_quest[q][1]:
        # 지능 비교
        result += 1
        rst += i_quest[q][2]

    else:
        # 적게 투자하고 많이 받을 수 있는 것 부터 선택
        s_tmp = s_quest[q][0] - z[0] + s_quest[q][2]
        i_tmp = i_quest[q][1] - z[1] + i_quest[q][2]

        if s_tmp > i_tmp:


