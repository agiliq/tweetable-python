c=open('data/alternate.txt','w');c.write('\n'.join([x for x in open('data/100west.txt', 'r').read().split('\n')[::2]]))
c.close()
