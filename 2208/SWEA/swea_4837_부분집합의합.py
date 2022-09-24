'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다.
집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.


예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
'''


import sys
sys.stdin = open("swea_4837_부분집합의합.txt", "r")

#  사용할 방법은 이진수를 나타낸 다음
#  원소끼리 곱함
#  ex) 이진수 10101과 집합 {1,2,3,4,5}가 있으면
#      1*1+2*0+3*1+4*0+5*1
#  계산결과가 0인지 확인

def SUMP(a,b):#두 배열에서 대응되는 것을 곱해서 리턴
    L= len(a) if len(a)<len(b) else len(b)
    #길이가 짧은 것을 기준으로 맞춤
    s=0
    for i in range(1,L+1):
        #길이가 다른 경우를 고려하여 뒤에서부터 곱해서 더함
        s+=int(a[-i])*int(b[-i])
    return s

test = int(input())                     #테스트케이스 수

for t in range(1, test+1):
    L = []
    for i in range(1, 13):
        L.append(i)

    n, k = map(int, input().split())

    '''
    스플릿만해서 리스트로 만듦.
    정수로 바꾸는건 함수에서 해줌
    경우의 수 고려
    bin을 쓰면 숫자를 알아서 2진법으로 바꿈
    문자열로 리턴되고 앞에 2진법을 나타내는 문자 2개가나옴
    곱해서 더해진게 k이면 끝
    '''

    result = 0
    for i in range(1, 1<<len(L)):
        a = bin(i)[2:]
        list_a = []
        list_a.extend(a)
        if list_a.count('1') == n and SUMP(a, L) == k:
            result = result + 1

    print(f'#{t} {result}')