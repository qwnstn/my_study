'''
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.


예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다.
입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.


정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.


print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.
'''

import sys

sys.stdin = open("swea_4866_괄호검사.txt", "r")

test = int(input())

for t in range(1, test+1):
    word = str(input())
    lstack = []         # (, {

    for i in word:
        if i == '(' or i == '{':
            lstack.append(i)
            continue

        try:                                    # 처음에  )나 }가 들어오면 lstack에 아무것도 없어 인덱스에러가 난다.
            if i == ')':
                if lstack[-1] == '(':
                    lstack.pop()
                else:
                    lstack.append('end')
                    break
            elif i == '}':
                if lstack[-1] == '{':
                    lstack.pop()
                else:
                    lstack.append('end')
                    break
        except IndexError:
            lstack.append('end')
            break


    if len(lstack) == 0:
        result = 1
    else:
        result = 0
    print(f'#{t} {result}')