import shutil
import os
import requests
r = requests.get('https://raw.githubusercontent.com/javiuribe/bloqueos/main/hosts')
f = open("hosts",'w')
f.write(r.text)
f.close()
shutil.copyfile(os.getcwd() + "\\hosts", 'C:\\Windows\\System32\\drivers\\etc\\hosts', follow_symlinks=True) #copy src to dst
os.remove("hosts")