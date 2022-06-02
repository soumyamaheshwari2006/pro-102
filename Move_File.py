from distutils import extension
import imp
from importlib.resources import path


import os
import shutil

from_dir= "C:/users/Amul Maheshwari/Downloads/Hw"
to_dir= "C:/users/Amul Maheshwari/Documents/Document_Files"

list_of_files= os.listdir(from_dir)
#print(list_of_files)
for file_name in list_of_files:
    name,extension= os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in['.jpg', '.jpeg', '.png', '.gif', '.jfif']:
        path1= from_dir+"/"+file_name
        path2= to_dir+"/"+"Image_files"
        path3= to_dir+"/"+"Image_files"+"/"+file_name
        print("path1", path1)
        print("path3", path3)
    if extension in['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov']:
        path1= from_dir+"/"+file_name
        path2= to_dir+"/"+"Video_files"
        path3= to_dir+"/"+"Video_files"+"/"+file_name
        print("path1", path1)
        print("path3", path3)
    if extension in['.ppt', '.xls', '.csv', '.pdf', '.txt']:
        path1= from_dir+"/"+file_name
        path2= to_dir+"/"+"Document_files"
        path3= to_dir+"/"+"Document_files"+"/"+file_name
        print("path1", path1)
        print("path3", path3)
    if extension in['.exe', '.bin', '.cmd', '.msi', '.dmg']:
        path1= from_dir+"/"+file_name
        path2= to_dir+"/"+"Setup_files"
        path3= to_dir+"/"+"Setup_files"+"/"+file_name
        print("path1", path1)
        print("path3", path3)

if os.path.exists(path2):
    print("Moving"+file_name+".....")

    shutil.move(path1,path3)

else:
    os.makedirs(path2)
    print("Moving"+file_name+".....")
    shutil.move(path1,path3)