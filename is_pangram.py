alpha = 'abcdefghijklmnopqrstuvwxyz'
def is_pangram(phrase):
    p = phrase.lower()
    w = []
    for i in p:
        if i.isalpha():
            w.append(i)
    if len(set(w)) == len(alpha):
        return True
    else:
        return False
      
