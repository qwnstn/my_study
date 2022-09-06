import sys

input = sys.stdin.readline

n = int(input())
result = [0 for i in range(4)]

number_p = [0 for i in range(4001)]     # 카운팅 정렬
maximum_p = [0, 0, 0, 0]                # [개수, 숫자1, 숫자2, 숫자3]
ck_p = 0                                # 개수 세기

number_m = [0 for i in range(4001)]
maximum_m = [0, 0, 0, 0]
ck_m = 0
'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''
for t in range(n):
    a = int(input())
    result[0] += a
    if a >= 0:
        number_p[a] += 1
        ck_p += 1
        if number_p[a] > maximum_p[0]:
            maximum_p[0] = number_p[a]
            maximum_p[1] = -4001
            maximum_p[2] = a
            maximum_p[3] = 4001
        elif number_p[a] == maximum_p[0]:
            if a < maximum_p[1]:
                maximum_p[3] = maximum_p[2]
                maximum_p[2] = maximum_p[1]
                maximum_p[1] = a
            elif maximum_p[1] < a < maximum_p[2]:
                maximum_p[3] = maximum_p[2]
                maximum_p[2] = a
            elif maximum_p[2] < a < maximum_p[3]:
                maximum_p[3] = a

    else:
        number_m[-a] += 1
        ck_m += 1
        if number_m[-a] > maximum_m[0]:
            maximum_m[0] = number_m[-a]
            maximum_m[1] = -4001
            maximum_m[2] = a
            maximum_m[3] = 4001
        elif number_m[-a] == maximum_m[0]:
            if a < maximum_m[1]:
                maximum_m[3] = maximum_m[2]
                maximum_m[2] = maximum_m[1]
                maximum_m[1] = a
            elif maximum_m[1] < a < maximum_m[2]:
                maximum_m[3] = maximum_m[2]
                maximum_m[2] = a
            elif maximum_m[2] < a < maximum_m[3]:
                maximum_m[3] = a

# 산술 평균
result[0] = int(round(result[0] / n, 0))

# 중앙값
if ck_m >= n//2 + 1:
    index = 0
    while ck_m >= n//2 + 1:
        index += 1
        ck_m -= number_m[index]
    result[1] = number_m[index]
else:
    index = 0
    while ck_m < n // 2 + 1:
        index += 1
        ck_m += number_p[index]
    result[1] = number_p[index]

# 최빈값
if maximum_p[0] > maximum_m[0]:
    if maximum_p[1] != -4001:
        result[2] = maximum_p[2]
    elif maximum_p[1] == -4001:
        if maximum_p[3] != 4001:
            result[2] = maximum_p[3]
        elif maximum_p[3] == 4001:
            result[2] = maximum_p[2]

elif maximum_p[0] < maximum_m[0]:
    if maximum_m[1] != -4001:
        result[2] = maximum_m[2]
    elif maximum_m[1] == -4001:
        if maximum_m[3] != 4001:
            result[2] = maximum_m[3]
        elif maximum_m[3] == 4001:
            result[2] = maximum_m[2]

elif maximum_p[0] == maximum_m[0]:
    if maximum_m[1] != -4001:
        result[2] = maximum_m[2]
    elif maximum_m[1] == -4001:
        if maximum_m[3] != 4001:
            result[2] = maximum_m[3]
        elif maximum_m[3] == 4001:
            if maximum_p[1] != -4001:
                result[2] = maximum_p[1]
            elif maximum_p[1] == -4001:
                result[2] = maximum_p[2]

# 범위
if ck_p == 0:
    while
result[3] =

for i in result:
    print(i)