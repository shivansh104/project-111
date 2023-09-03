import os
import shutil

from_dir="C:/Users/Barbie & Sibbu/Downloads"
to_dir="C:/Users/Barbie & Sibbu/Desktop/document_files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for x in  list_of_files:
    n,e=os.path.splitext(x)
    print(n)
    print(e)

    if e in ['.txt','.pdf','.doc','.docx']:
        p1=from_dir+"/"+x
        p2=to_dir+"/"+"docs"
        p3=to_dir+"/"+"docs"+x
        if os.path.exists(p2):
            shutil.move(p1,p3)
        else:
            os.makedirs(p2)
            shutil.move(p1,p3)
            

     
    