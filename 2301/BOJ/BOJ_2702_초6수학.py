def U(a, b):    # 최소공배수, 최대공약수
    if not a%b:
        return a, b
    elif not b%a:
        return b, a
    else:
        tmp = a*b
        if b > a:
            a, b = b, a
        while b:
            a, b = b, a % b
        return tmp // a, a

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(*U(a, b))