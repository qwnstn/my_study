'''
n-4개를 1에서 1번으로
n-3개를 1에서 2번으로
n-2개를 1에서 1번으로
n-1개를 1에서 2번으로
출력
n-1개를 2에서 3번으로
n-2개를 1에서 3번으로
n-3개를 2에서 3번으로
n-4개를 1에서 3번으로
...
'''
def tower(n, s=1, e=3):    # 횟수, 시작점, 끝점
    if n == 1:
        print(s, e)

    else:
        tower(n - 1, s, 6-s-e)
        print(s, e)
        tower(n - 1, 6-s-e, e)

n = int(input())
print(2**n-1)
tower(n)