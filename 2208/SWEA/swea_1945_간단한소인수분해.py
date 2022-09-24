'''
숫자 N은 아래와 같다.

N=2^a x 3^b x 5^c x 7^d x 11^e

N이 주어질 때 a, b, c, d, e 를 출력하라.
'''

t = int(input())
p_num = [2, 3, 5, 7, 11]

for i in range(1, t+1):
    num = int(input())
    ex = [0] * 5
    for k, v in enumerate(p_num):
        while num % v == 0:
            ex[k] = ex[k] + 1
            num = num // v

    print(f'#{i}', end=' ')
    print(*ex)