while True:
    input_sentence = input()
    if input_sentence == '#':
        break
    spell = input_sentence[0]
    sentence = input_sentence.split(spell)
    SENTENCE = input_sentence.split(spell.upper())
    print(spell, len(sentence) - 2 + len(SENTENCE) - 1)