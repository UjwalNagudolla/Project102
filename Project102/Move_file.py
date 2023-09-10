import os
import shutil
from_dir="/Users/ujwal/Pictures/Screenshots"
to_dir="/Users/ujwal/Documents/Whitehat Class Scrn"

list_of_file=os.listdir(from_dir)
print(list_of_file)
for file_name in list_of_file:
    name,ext=os.path.splitext(file_name)
    print(name)
    print(ext)
    if ext=='':
        continue
    if ext in ['.png']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+"Image_File"
        path3=to_dir+'/'+"Image_File"+file_name
        print(path1)
        print(path3)
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)
