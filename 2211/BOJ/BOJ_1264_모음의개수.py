'''
.split('e').split('i').split('o').split('u').split('A').split('E').split('I').split('O').split('U')
'''
import re
while True:
    word = re.split(r'a|e|i|o|u|A|E|I|O|U', input())
    if word == ['#']:
        break
    print(len(word) - 1)