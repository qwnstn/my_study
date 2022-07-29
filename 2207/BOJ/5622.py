word = input()

word_list = []
word_list.extend(word)                              # 문자 하나하나 리스트로 받음
result = 0

for i in word_list:
    if ord(i) <= 82:
        result = result + (ord(i) + 1)//3 - 19
    elif ord(i) == 83:
        result = result + 8
    elif ord(i) <= 89:
        result = result + ord(i)//3 - 19
    else:
        result = result + 10                        # 아스키코드로 분류

print(result)