import os
from pathlib import Path
import shutil
# change the location it points
os.chdir('D:/ars/File-Manager-Using-Python/files-python')

#File handling operations are
# 1. Rename Files
# 2. Move Files 
# 3. Copy Files 
# 4. Remove Directory and File

def rename_files(nameslist=None):
    i=0
    for files in os.listdir():                  # returns list of files in the location
        i+=1
        name,ext=os.path.splitext(files)        # return list(2) 2nd element has .(dot)
        splitted=name.split("-")                # return list with no -
        names=[x.strip() for x in splitted]     # removes whitespaces
        len_old=len(os.listdir())        

        # check whether given names are enough for the items  
        if nameslist!=None and len(nameslist)>=len_old:
            new_name=f"{nameslist[i-1]}{ext}"
        else:
            new_name=f"{str(i).zfill(2)}-{names[1]}-{names[0]}{ext}"
        os.rename(files,new_name)               # rename the file
# rename_files()
# rename_files(["a","b","c","d"])
# rename_files(["a","b"])


def move_files(dest_folder="data"):
    # check whether the folder exists or not before creating and then create
    if not os.path.exists(dest_folder):  
        os.mkdir(dest_folder)
    for files in os.listdir():
        if files==dest_folder:
            continue
        shutil.move(files,dest_folder)      # move files to the folder
# move_files("newfold")

def copy_files(dest_folder):
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    for files in os.listdir():
        if files==dest_folder:
            continue
        shutil.copy(files,dest_folder)      # copy files to the folder
# copy_files("data")

def remove_directory(dir):
    # rmtree-remove the files in the directory 
    # one by one recursively and then remove the folder
    shutil.rmtree(dir)
# remove_directory("data")

