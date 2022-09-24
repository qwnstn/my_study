'''
문자열로 이루어진 계산식이 주어질 때,
이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.


중위 표기식을 후위 표기식으로 바꾸는 방법

토큰이 연산자일 때,
스택에 값이 없으면 push,
이 토큰이 스택의 top에 있는 토큰보다 우선순위가 높으면 저장,
이 토큰이 같거나 낮으면 작아질때 까지 스택에서 pop 후 토큰을 push.
'''
import sys
sys.stdin = open('swea_1224_계산기3.txt', 'r')

for T in range(10):
    N = int(input())                                        # 길이
    infix = input()                                         # 중위 표기식
    stack = []                                              # 기호 저장용
    postfix = ''                                            # 후위 표기식 제작용

    # 중위 표기식을 후위 표기식으로 변경
    for x in infix:                                         # 문자를 넣는다
        if ord('0') <= ord(x) <= ord('9'):                  # 문자가 숫자인지 확인
            postfix += x                                        # 숫자면 넣음
        else:                                               # 문자가 기호일 때
            if x == '(':                                        # '(' 는 넣는다
                stack.append(x)
            elif x == '*' or x == '/':                          # 곱셈과 나눗셈일 때
                while stack and (stack[-1] == '*' or stack[-1] == '/'): # 스택의 top이 곱셈과 나눗셈이면
                    postfix += stack.pop()                              # 스택에서 pop한 값(곱셈 혹은 나눗셈)을 post에 넣는다.
                stack.append(x)                                 # 넣는다.
            elif x == '+' or x == '-':                          # 덧셈과 뺼셈일 때
                while stack and stack[-1] != '(':                   # 스택의 top이 '('가 아니면 스택의 top이 '('가 될때까지
                    postfix += stack.pop()                          # 스택의 값을 pop해서 post에 넣는다.
                stack.append(x)                                 # 넣는다
            elif x == ')':                                      # ')' 일 때
                while stack and stack[-1] != '(':                   # 스택의 top이 '('가 아니면 스택의 top이 '('가 될때까지
                    postfix += stack.pop()                          # 스택의 값을 pop해서 post에 넣는다.
                stack.pop()                                     # stack의 top인 ')'를 뺀다.

    while stack:                                            # 나머지 스택의 모든 값을 빼서
        postfix += stack.pop()                                  # post에 넣는다.
                                                            # 후위표기법 완성

    # 후위 표기식으로 계산
    stack2 = []                                             # stack2.pop() & stack2.pop()
    for x in postfix:                                       #   우측 값    &   좌측 값
        if ord('0') <= ord(x) <= ord('9'):                      # 문자가 숫자인지 확인
            stack2.append(int(x))                                   # 숫자면 정수로 바꾼 뒤 스택2에 넣는다.
        elif x == '+':                                          # '+'는
            stack2.append(stack2.pop() + stack2.pop())              # 스택2 최상단 값 2개를 더하고 다시 넣는다
        elif x == '-':                                          # '-'는
            stack2.append(-stack2.pop() + stack2.pop())             # 스택2 최상단 값 2개를 빼고 다시 넣는다. 먼저 빠진 값이 -값이다.
        elif x == '*':                                          # '*'는
            stack2.append(stack2.pop() * stack2.pop())              # 스택2 최상단 값 2개를 곱하고 다시 넣는다.
        elif x == '/':                                          # '/'는
            stack2.append(1 / (stack2.pop() / stack2.pop()))        # 스택2 최상단 값 2개를 나누고 다시 넣는다. 먼저 빠진 값이 분모이므로 역수를 취한다.

    print(f'#{T + 1} {stack2.pop()}')                       # 완성