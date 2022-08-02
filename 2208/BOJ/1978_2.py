num_list = [1]              # 1 추가

for i in range(2, 501):       # 2의 배수 추가, 2 제거
    num_list.append(i*2)


for i in range(1, 500):        # 3부턴 홀수만 시행
    p= i*2 + 1                 # 있는건 시행 X
    if p in num_list:
        continue
    else:
        for j in range(2, 1000 // p + 1):
            num_list.append(j * p)


num_list = set(num_list)    # 중복 제거(set)

p_list = list(range(1001))
for i in num_list:
    p_list.remove(i)    # 소수 리스트 제작

n = int(input())
num = list(map(int, input().split()))

ck = 0
for i in num:
    if i in p_list:         # 숫자가 소수 리스트 안에 있는지 확인
        ck = ck + 1

print(ck)