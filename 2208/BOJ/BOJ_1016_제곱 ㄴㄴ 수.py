'''
1 10    7
1도 포함됨
소수
소수끼리의 조합
'''

min, max = map(int, input().split())

prime_com = []          # 소수의 거듭제곱으로 나눠지지 않는 수

prime = [2, 3]                      # 소수 구하기
p = 3
while p <= max:
    for i in range(1, len(prime)):
        if p % prime[i] == 0:
            break
        else:
            if prime[i] == prime[-1]:
                prime.append(p)

    if p >= min:                                            # 제곱으로 나눠지지 않는 수
        for i in range(len(prime)):                      # 소수를 포함함. 즉 결과임
            if p % (prime[i]**2) == 0:
                break
            if prime[i] > int(p**(1/2)):
                prime_com.append(p)
                break

        for i in range(len(prime)):
            if p + 1 > max:
                break
            if (p+1) % (prime[i]**2) == 0:
                break
            if prime[i] > int((p+1)**(1/2)):
                prime_com.append(p+1)
                break
    p += 2

if min == 2:
    print(len(prime_com) + 1)
elif min == 1:
    print(len(prime_com) + 2)
else:
    print(len(prime_com))