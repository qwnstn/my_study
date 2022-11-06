'''
조건
1. 연꽃엔 어울리는 개구리가 정해져있다.
2. 통나무로 만나는 개구리들은 주제의 호감도가 일치해야 한다.
'''
'''
1. 고정 개구리를 집어넣고
2. 개구리들을 순회
3. 순회 중 조건 불일치 시 전 단계로 돌아가기
4. 결과를 찾는 순간 종료 = 결과가 없으면 모든 조건을 시행
'''
'''
개선점
모든 개구리를 순차적으로 넣지 말고
연꽃의 집합을 구해서 집합마다 확인하여 실패 시 바로 종료하는 방식으로 판단하면 좋을 것 같음
'''


def frog(f=1):    # 개구리 번호
    if f == n + 1:
        print('YES')
        result[0] = 'YES'
        for i in range(1, n + 1):
            print(result[i], end=' ')
    else:
        if f in only_one_set:
          frog(f+1)

        else:
            # 고정 개구리가 아니면
            for k in frogs[f][1]:
                # 개구리의 연꽃 번호 순환
                if not result[k]:
                    # 앉아있는 개구리가 없으면
                    ck = 0
                    for j in range(1, field[k][0]+1):
                        # k연꽃 연결 순환(통나무)
                        if result[field[k][j][0]]:
                            # 이미 앉아 있는 개구리 확인
                            if frogs[result[field[k][j][0]]][0][field[k][j][1]] != frogs[f][0][field[k][j][1]]:
                                # 앉아있는 개구리와 주제 호감도 확인
                                break
                        ck += 1

                    if ck == field[k][0]:
                        result[k] = f
                        frog(f + 1)
                        if result[0] != 'YES':
                            result[k] = 0
                        else:
                            return
            return

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

only_one = [0 for _ in range(n+1)]
# 연꽃이 하나만 있는 개구리 집합
# idx = 연꽃번호, value = 개구리번호

frogs = {i:[] for i in range(1, n+1)}
# 1: [[1, 1, 1, 1], {1, 5}]
# 개구리번호: [각 주제별 호감도, 좋아하는 연꽃]

for i in range(1, n+1):
    frogs[i].append(list(map(int, input().split())))

for i in range(1, n+1):
    a, b = map(int, input().split())
    frogs[i].append({a, b})
    if a == b:
        if not only_one[a]:
            only_one[a] = i
        else:
            only_one[0] = -1

only_one_set = set(only_one)

field = {i:[0] for i in range(1, n+1)}
# 1: [(2, 1)]
# 연꽃번호: 연결 개수, (연결된 연꽃, 주제번호)...
for i in range(m):
    a, b, t = map(int, input().split())
    field[a].append((b, t-1))
    field[a][0] += 1
    field[b].append((a, t-1))
    field[b][0] += 1

# print('frogs', frogs)
# print('field', field)

'''
데이터 부분
-----------------
계산 부분
'''
if only_one[0]: # 연꽃이 하나인 개구리 중복 확인
    print('NO')
else:
    only_one = deque(only_one)
    only_one.popleft()
    only_one.appendleft('NO')
    result = list(only_one)

    frog()
    if result[0] == 'NO':
        print('NO')