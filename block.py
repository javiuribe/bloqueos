import shutil
import os
shutil.copyfile(os.getcwd() + "\\hosts", 'C:\\Windows\\System32\\drivers\\etc\\hosts', follow_symlinks=True) #copy src to dst
