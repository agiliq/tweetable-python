leet_dict = dict(zip("aeilot", "431|07"))

def leet(txt):
    return txt.lower().translate(str.maketrans(leet_dict))
