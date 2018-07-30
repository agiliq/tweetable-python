import os, re
[os.rename('data/'+each, 'data/'+re.sub('.txt', '.rst', each)) for each in os.listdir('data')]
