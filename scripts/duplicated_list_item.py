import collections
x=dict(collections.Counter([1,2,3,4,5,5,6,6,6,7]))
print([k for k,v in x.items() if v>1])
