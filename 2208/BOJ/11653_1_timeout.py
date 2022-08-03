# 시간 초과
n = int(input())

num_list = [1]              # 1 추가

for i in range(2, n//2 +1):       # 2의 배수 추가, 2 제거
    num_list.append(i*2)

for i in range(1, n//2 +1):       # 3부턴 홀수만 시행
    p= i*2 + 1                            # 있는건 시행 X
    if p in num_list:
        pass
    else:
        for j in range(2, n//p +1): 
            num_list.append(j * p)

num_list = set(num_list)                # 중복 제거(set), 소수를 제외한 숫자들

p_list = list(range(1, n + 1))
for i in num_list:
    if i in p_list:
        p_list.remove(i)                # 소수 리스트 제작


while n not in p_list:
    for i in p_list:
        if n % i == 0:
            n = n // i
            print(i)
            break
print(n)