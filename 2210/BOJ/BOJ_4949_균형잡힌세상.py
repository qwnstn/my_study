while True:
    word = input()
    if word == '.':
        break

    left = []
    result = 'yes'
    for i in word:
        if i == '(' or i == '[':
            left.append(i)
        elif i == ')':
            try:
                if left.pop() == '(':
                    pass
                else:
                    result = 'no'
                    break
            except:
                result = 'no'
                break
        elif i == ']':
            try:
                if left.pop() == '[':
                    pass
                else:
                    result = 'no'
                    break
            except:
                result = 'no'
                break
    if left:
        result = 'no'
    print(result)
