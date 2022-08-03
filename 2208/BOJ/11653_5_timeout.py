# 99% 시간 초과
n = int(input())

if n == 1:                     # 1일땐 미출력
    print()                
else:
    num_set = {1}              # 1 추가

    for i in range(2, int(n**0.5)//2 +1):       # 2의 배수 추가, 2 제거
        num_set.add(i*2)

    for i in range(1, int(n**0.5)//2 +1):       
        p= i*2 + 1                              # 3부터 루트n까지의 홀수들만 시행
        if p not in num_set:                    # 있는건 시행 X
            for j in range(2, int(n**0.5)//p +1):   
                num_set.add(j * p)            


    p_list = list(range(1, int(n**0.5) + 1))
    for i in num_set:
        if i in p_list:
            p_list.remove(i)                # 소수 리스트 제작


    while n not in p_list:
        for i in p_list:
            if n % i == 0:
                n = n // i
                print(i)
                break
            else:
                if i == p_list[-1]:
                    p_list.append(n)        # while 탈출용 리스트추가
                    break                   
    print(n)