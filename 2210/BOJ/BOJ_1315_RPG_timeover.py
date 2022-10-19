import sys
input = sys.stdin.readline

def RPG(str=1, total=2): # 힘, 토탈
    global result
    for s in range(str, total):
        ck = 0
        tmp = 0
        for q in quest:
            if q[0] <= s or q[1] <= total - s:
                ck += 1
                tmp += q[2]
        if result < ck:
            result = ck
        if total != tmp + 2:
            RPG(s, tmp+2)

    return

n = int(input())

quest = []
for _ in range(n):
    s, i, pnt = map(int, input().split())
    quest.append([s, i, pnt])

# quest.sort()

result = 0
RPG()

print(result)