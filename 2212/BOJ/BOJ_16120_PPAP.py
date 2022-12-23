word = input()

stack = []
ck = 0
for w in word:
    if w == 'A':
        if ck:
            stack.append(w)
            break
        else:
            ck += 1
    else:
        if ck:
            try:
                if stack[1]:
                    stack.pop()
                    ck -= 1
                else:
                    break
            except:
                break
        else:
            stack.append(w)

print('PPAP') if len(stack) == 1 and stack[0] == 'P' and not ck else print('NP')