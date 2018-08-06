from string import ascii_uppercase as upr, ascii_lowercase as lwr

def rot13(txt):
    map = dict(list(zip(upr, upr[13:] + upr[:13])) + list((zip(lwr, lwr[13:] + lwr[:13]))))
    return "".join([map[el] for el in txt])
