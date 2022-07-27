word = input()

word = word.upper() # 대문자 변환
set_word = set(word) # 중복 제거용 set, 순서가 뒤죽박죽으로 바뀜

ck = {}
for i in set_word:
    ck[i] = word.count(i)     # ex) ck = {'B':5, 'A':4...}

maximum = []
max_word = []                  # 두 리스트의 순서쌍은 유지된다
for k, v in ck.items():
    maximum.append(v)
    max_word.append(k)

new_maximum = sorted(maximum)   # maximum 정렬, maximum 유지

if len(new_maximum) == 1:       # 단어가 하나로만 되어 있을 때,
    print(max_word[0])
elif new_maximum[-1] == new_maximum[-2]: # 단어에 많이 쓰인 글자가 중복일 때,
    print('?')
else:
    print(max_word[maximum.index(new_maximum[-1])]) # 이외