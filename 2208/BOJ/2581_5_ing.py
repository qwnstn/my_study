def ppp(n, input_list):
    if :
        return input_list                   # 내가 하고자 하는 것: 들어온 리스트가 충족이 되면 그대로 쓸 것임
                                            # x를 사용하면 될 거 같음
    
    else:
        p_list = [2, 3]                     # 소수들, 2, 3, 5,.. 
        x = 3
        while p_list[-1] < n:
            x = x + 2                       # 5부터 홀수만 시행
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
for i in ppp(n)[-1::-1]:
    if i < m:
        break
    else:
        result = result + i
        min = i
        
if result == 0:
    print(-1)
else:
    print(result)
    print(min)