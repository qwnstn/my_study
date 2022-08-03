# 30840kb, 332ms

m = int(input())
n = int(input())

num_set = {1}              # 1 추가

for i in range(m//2, n//2 + 1):       # 2의 배수 추가, 2 제거
    num_set.add(i*2)
if 2 in num_set:
    num_set.remove(2)

for i in range(1, n//2 + 1):        # 3부턴 홀수만 시행
    p= i*2 + 1                         # 있는건 시행 X
    if p in num_set:
        pass
    else:
        for j in range(2, n//p +3): 
            num_set.add(j * p)

p_list = list(range(m, n + 1))
for i in num_set:
    if i in p_list:
        p_list.remove(i)    # m과 n사이 소수 리스트 제작


ck = 0
if p_list == []:
    print(-1)
else:
    for i in p_list:
        ck = ck + i
    minimum = p_list[0]
    print(ck), print(minimum)