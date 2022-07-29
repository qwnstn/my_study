word = input()

word_list = []

word_list.extend(word)      # 문자 하나씩 추가

result = len(word_list)     # 전체 길이

for num, i in enumerate(word_list):
    if ord(i) == 45:                        # '-' 제거
        result = result - 1

    if num > 1:
        if ord(i) == 61:                    # '=' 제거
            if word_list[num-1] == 'z' and word_list[num-2] == 'd':
                result = result - 2
            else:
                result = result - 1
    elif num == 1:                          # '=' 제거_2
        if ord(i) == 61:                    
            result = result - 1
    
    if num >= 1:                            # 'nj', 'lj' 제거
        if ord(i) == 106 and word_list[num-1] == 'l' or word_list[num-1] == 'n':
            result = result - 1
            

print(result)