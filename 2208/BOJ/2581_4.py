# 30840kb , 160ms
def ppp(n):
    p_list = [2]                     # 소수들, 2, 3, 5,.. 
    x = 1
    while x + 2 <= n:
        x = x + 2                       # 3부터 홀수만 시행
        for i in p_list:
            if x % i != 0:
                if i == p_list[-1]:
                    p_list.append(x)    # 마지막까지 나눠지지 않으면 넘어가기
                    break
            else:
                break                   # 나눠지면 바로 넘어가기
    return p_list

m = int(input())
n = int(input())

result = 0
for i in ppp(n)[-1::-1]:                # 뒤에서부터 추출
    if i < m:
        break
    else:
        result = result + i
        min = i
        
if result == 0 or (n == m == 1):
    print(-1)
else:
    print(result)
    print(min)