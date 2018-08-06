import itertools

words = set(open('/usr/share/dict/words').read().split());

def anagrams(txt):
    return set(["".join(perm) for perm in itertools.permutations(txt.lower())
                if "".join(perm) in words])
