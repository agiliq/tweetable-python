c=open('reverse.txt','w')
c.write('\n'.join([x for x in open(sys.argv[1], 'r').read().split('\n')[::-1]]));c.close()
