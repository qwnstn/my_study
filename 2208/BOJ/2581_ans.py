def prime_list(N):
    a = [False,False] + [True]*(N-1)
    primes=[]

    for i in range(2,N+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False
    return primes

M = int(input())
N = int(input())

if list(filter(lambda n : n >= M, prime_list(N))):
    result = list(filter(lambda n : n >= M, prime_list(N)))
    print(sum(result))
    print(min(result))
else :
    print(-1)