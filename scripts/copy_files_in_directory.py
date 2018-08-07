import shutil,os,re

def copy_files_in_dir(_dir):
    [shutil.copyfile(_dir+each, _dir+re.sub('.ext', '.bak.ext', each))
     for each in os.listdir('data') if (each.endswith('.ext') and not each.endswith('.bak.ext'))]
