import os,shutil, datetime as dt
result_dict={}
download_dir='~/Desktop/'
[result_dict.setdefault(
    dt.datetime.strftime(
        dt.datetime.fromtimestamp(
            os.path.getmtime(download_dir+each)), '%Y-%m'), []).append(each)
 for each in os.listdir(download_dir) if os.path.isfile(download_dir+each)]
for x in result_dict:
    new_dir = download_dir+x+'/'
    os.makedirs(new_dir, exist_ok=True)
    [shutil.move(download_dir+each, new_dir+each) for each in result_dict[x]]
