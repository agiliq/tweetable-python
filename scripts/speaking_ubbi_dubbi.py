vowels = "aeiou"
vowels_dict = {i: f"ub{i}" for i in "aeiou"}

def ubbi_dubbi(txt):
    return txt.lower().translate(str.maketrans(vowels_dict))
