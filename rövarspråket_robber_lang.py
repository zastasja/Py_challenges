vowels = ['a','e', 'i', 'o', 'u', 'y']
symbols = [',', '.', '!', '?', ';', ':', ' ']
def translate_to_robber_lang(phrase):
    n: str = ""
    for i in phrase:
        if i.lower() not in vowels and i not in symbols:
            new_letter = f'{i}o{i}'
            n += new_letter
        else:
            n += i

    return n
