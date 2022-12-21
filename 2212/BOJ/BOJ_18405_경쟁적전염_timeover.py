import sys
input = sys.stdin.readline

n, k = map(int, input().split())

total = set()   # 전체 바이러스 좌표 집합
virus = {i: set() for i in range(1, k+1)}   # 바이러스 번호: 좌표 집합
ground = [] # 영역 표시(이미지화)
for x in range(n):  # x = x좌표
    tmp = list(map(int, input().split()))
    ground.append(tmp)
    for idx, v in enumerate(tmp):   # idx = y좌표, v = 바이러스 번호
        if v:
            virus[v].add((x, idx))
            total.add((x, idx))

s, x, y = map(int, input().split())
d = ((1, 0), (-1, 0), (0, 1), (0, -1))

tmp_position = set()    # 바이러스 위치 임시 저장소
for time in range(s):
    tmp_position.clear()
    for key, values in virus.items():    # key = 바이러스 번호, value = 바이러스 위치 집합
        for value_x, value_y in values:
            for dx, dy in d:
                new_value_x, new_value_y = value_x + dx, value_y + dy
                if (new_value_x, new_value_y) not in total:
                    if 0 <= new_value_x < n and 0 <= new_value_y < n:
                        total.add((new_value_x, new_value_y))
                        tmp_position.add((new_value_x, new_value_y))
                        ground[new_value_x][new_value_y] = key
        virus[key] = tmp_position.copy()

print(ground[x-1][y-1])