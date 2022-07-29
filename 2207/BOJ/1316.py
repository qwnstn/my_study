N = int(input())
result = N

for i in range(N):
    word = input()
    word_list = []
    word_list_rev = []
    word_list.extend(word)                  # 리스트로 한글자씩 받기
    word_list_rev.extend(word)              # 뒤집을 리스트 하나 더 생성
    word_list_rev.reverse()                 # 리스트 뒤집기
    word_set = set(word_list)               # 중복 제거용

    for k in word_set:                      # k는 word의 중복되지 않은 원소(str)
        num = word_list.index(k)                  # 가장 왼쪽 글자 왼쪽에서 순번
        rev_num = word_list_rev.index(k)              # 가장 오른쪽 글자의 오른쪽에서 순번
        new_word_list = word_list[num : len(word_list)-rev_num] # 슬라이스 

        ck_in = 0
        ck_out = 0
        for j in new_word_list:             # j는 new_word_list의 원소
            if ord(j) != ord(k):
                result = result - 1
                ck_out = ck_out - 1
                break
        
        if ck_in != ck_out:
            break                                    # 바깥쪽 for문 탈출 필요
    

print(result)