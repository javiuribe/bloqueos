#Crear ejecutable--> pyinstaller --onefile dns_block.py

import shutil
import os
import requests
ruta_windows = "C:\\Windows\\System32\\drivers\\etc\\hosts"
ruta_ubuntu = "/etc/hosts"
r = requests.get('https://raw.githubusercontent.com/javiuribe/bloqueos/main/hosts') #descargar fichero host
f = open("hosts",'w')
f.write(r.text)
f.close()
shutil.copyfile(
    os.getcwd() + "\\hosts", ruta_windows, follow_symlinks=True) #sobreescribir fichero host
os.remove("hosts")