import os 
f1=open("cwd.txt",'w+')
with open("cwd.txt", "a") as myfile1:
    myfile1.write("%s"% os.getcwd())
with open("cwd.txt", "a") as myfile:
 print("PLEASE ENTER THE FOLDER NAME IN CAPITALS ONLY")
 Folder_name=input("Enter your folder name")
 myfile.write("\%s"% Folder_name)
f1.close()
f1=open("back_up.txt",'w+')
with open("back_up.txt", "a") as myfile2:
    myfile2.write("%s"% os.getcwd())
with open("back_up.txt", "a") as myfile:
 myfile.write("\BACK_UP")
f1.close()
f1=open("cwd.txt",'r')
folder_path=f1.read()
f2=open("back_up.txt",'r')
backup_path=f2.read()
os.mkdir(folder_path)
os.mkdir(backup_path)
f1.close()
f2.close()








