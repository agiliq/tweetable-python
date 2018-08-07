import itertools

words = set(open('/usr/share/dict/words').read().split())

def anagrams(txt):
    return set(["".join(perm) for perm in itertools.permutations(txt.lower())
                if "".join(perm) in words])


def test_all_valid_anagrams_of_a_word():
    resp = anagrams('rat')
    assert resp == {'art', 'rat', 'tar', 'tra'}
