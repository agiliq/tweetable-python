import shutil,os,re
[shutil.copyfile('data/'+each, 'data/'+re.sub('.ext', '.bak.ext', each))
 for each in os.listdir('data') if (each.endswith('.ext') and not each.endswith('.bak.ext'))]
