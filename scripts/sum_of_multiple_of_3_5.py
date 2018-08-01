import math
print(sum(set([x*3 for x in range(math.ceil(1000/3)) if x<1000]+[x*5 for x in range(math.ceil(1000/5)) if x*5<1000]+[x*15 for x in range(math.ceil(1000/15)) if x*15<1000])))
