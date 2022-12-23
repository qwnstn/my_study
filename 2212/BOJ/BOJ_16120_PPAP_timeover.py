word = input()

if word == 'P':
    print('PPAP')
elif word[-2] != 'A':
    print('NP')
else:
    A = word.count('A')
    for _ in range(A):
        word = word.replace('PPAP', 'P')
    print('PPAP') if word == 'P' else print('NP')