# 시간 초과
n = int(input())

if n == 1:
    print(None)                 # 아무것도 출력하지 않음 != None출력
else:
    num_set = {1}              # 1 추가

    for i in range(2, int(n**0.5) +1):       # 2의 배수 추가, 2 제거
        num_set.add(i*2)

    for i in range(1, int(n**0.5) +1):       # 3부턴 홀수만 시행
        p= i*2 + 1                           # 있는건 시행 X
        if p in num_set:
            pass
        else:
            for j in range(2, n//p +1):      # 이 부분 range설정 잘못 >> int(n**0.5) // p +1로 변경
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