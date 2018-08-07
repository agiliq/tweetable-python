import string,collections,re

def most_common_words(_file):
    z = re.sub('[\n{}]'.format(string.punctuation), '',  open(_file,'r').read().lower())
    x = collections.Counter(z.split(' '));del x['']
    return sorted(x.items(), key=lambda kv: kv[1], reverse=True)[:15]

def test_most_common_words():
    assert most_common_words('data/100west.txt')[:3] == [('the',244),('of',122),('and',101)]
