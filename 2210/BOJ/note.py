N, M, K= map(int,input().split())

DP = [[-1,1]+[-1] * (N-1) for i in range(M+1)]

#N이 자리수, M이 만들 수, K번째 찾기

#점차 증가해야함
#재귀로 넣는 수는 절대 수치가 아닌 상대수치로 넣기
#기본적으로 1은 다 넣어야하니까
#일단 시작은 M대신 M-N으로 들어가야함
#N은 자리수니까 그대로 들어감
#func(N, M-N)으로 시작
#for i in range(X):
#   func(N-1, M-N*i) 여기서 M-N*i는 0이상이어야함
#   i는 증가량을 뜻하기 때문
#   이번에 1,2,3으로 수열이 생긴 상태에서 i=1이라면
#   다음 수부터는 전부 4이상임을 뜻함
#   그럼 X는 M//i+1

#함수의 끝은?
#1.

def func(N,M,T): #N은 남은 자리 1씩 증가
                #M은 남은 숫자 T씩 감소
                #T는 마지막수, 단조증가
    if N*T>M:
        return 0

    #남은게 N자리 M칸   채우기인데 마지막 수가 T라면
    #N자리 M-NT칸
    if DP[M-N*T][N]!=-1:
        return DP[M-N*T][N]

    rst=0
    for i in range(T,M//N+1):
        rst+=func(N-1,M-i,i)
    DP[M-N*T][N]=rst
    return rst

print(func(N,M,1))
print(DP)