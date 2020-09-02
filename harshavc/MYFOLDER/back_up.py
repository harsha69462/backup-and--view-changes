import os
import os.path
import shutil

destination = "D://harshavc//BACK_UP"

with os.scandir('D://harshavc//MYFOLDER') as x:
    for i in x:
        dest = shutil.copy2(i, destination)

print("BACKUP harsha")
print("BACK_UP FOLDER: ", os.listdir(destination))




