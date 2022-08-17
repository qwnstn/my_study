'''
615612kb 2612ms
'''
a = input()
find = set()
maximum = (1 << len(a)) - 1     # 이진법 1111...(1이 n개)
for i in range(len(a)):         # 처음은 1111..., 다음은 01111..., 그 다음은 001111..., 마지막 ..001까지
    ck = maximum >> i
    for k in range(i+1):        # 붙어있는 문자열 부분집합 ex) 0011, 0110, 1100 묶음
        ck = ck << k
        find.add(str(bin(ck)[2:])[::-1])  # 이진법을 문자로 받되 뒤집어서 받음
        ck = ck >> k            # ck를 다시 원상복구해서 다음 ck에 영향이 없도록


result = set()
for i in find:
    result.add(a[i.index('1'):len(i)])
print(len(result))

# ababc

# for i in range(1, 1<<len(a)):
#     sum = ''
#     for j in range(len(a)):
#         if i & (1 << j):
#             sum = sum + a[j]
#             result.add(sum)
# print(result, len(result))