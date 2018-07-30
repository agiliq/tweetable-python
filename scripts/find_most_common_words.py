import string,collections,re
z=re.sub('[\n{}]'.format(string.punctuation), '',  open('100west.txt','r').read().lower())
x=collections.Counter(z.split(' '));del x['']
print(sorted(x.items(), key=lambda kv: kv[1], reverse=True)[:15])
