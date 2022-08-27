'''
1 10    7
1도 포함됨
소수
소수끼리의 조합
'''

min, max = map(int, input().split())

result = 0          # 소수의 거듭제곱으로 나눠지지 않는 수

prime = [2, 3]                      # 소수 구하기
p = 3
while p <= max:
    for i in range(1, len(prime)):
        if p % prime[i] == 0:
            break
        if prime[i] > int(p **(1/2)):
            prime.append(p)
            break

    if p >= min:                                         # 제곱으로 나눠지지 않는 수
        for i in range(len(prime)):                      # 소수를 포함함. 즉 결과임
            if p % (prime[i]**2) == 0:
                break
            if prime[i] > int(p**(1/2)):
                result += 1
                break

        if (p + 1) % 4 != 0 and p + 1 <= max:
            for i in range(len(prime)):
                if (p+1) % (prime[i]**2) == 0:
                    break
                if prime[i] > int((p+1)**(1/2)):
                    result += 1
                    break
    p += 2

if min == 2:
    print(result + 1)
elif min == 1:
    print(result + 2)
else:
    print(result)