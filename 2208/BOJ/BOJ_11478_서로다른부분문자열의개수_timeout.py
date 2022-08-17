'''
시간 초과
'''
import sys

a = list(map(str, sys.stdin.readline().strip()))
find = (1<<(len(a))) - 1   # 이진법 1111...(n개)

result = set()
for i in range(len(a)):     # 처음은 1111..., 다음은 01111..., 그 다음은 001111..., 마지막 ..001까지
    ck = find >> i
    for k in range(i+1):      # 붙어있는 문자열 부분집합 ex) 0011, 0110, 1100 묶음
        ck = ck << k
        sum = ''
        for j in range(len(a)):
            if ck & (1 << j):
                sum = sum + a[j]
                result.add(sum)
        ck = ck >> k          # ck를 다시 원상복구해서 다음 ck에 영향이 없도록
print(len(result))

# ababc

# for i in range(1, 1<<len(a)):
#     sum = ''
#     for j in range(len(a)):
#         if i & (1 << j):
#             sum = sum + a[j]
#             result.add(sum)
# print(result, len(result))