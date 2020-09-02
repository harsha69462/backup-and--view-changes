import os
import os.path, time
import difflib
count=0
with os.scandir('C:/Users/hp/Desktop/harshavc/MYFOLDER') as x:
    with os.scandir('C:/Users/hp/Desktop/harshavc/BACK_UP') as y:
        for z in x:
            f=open("timestamp.txt", "r")
            time_stamp=f.read()
            if(time.ctime(os.path.getmtime(z)) > time_stamp):
                count=1

if (count == 1):
    with os.scandir('C:/Users/hp/Desktop/harshavc/MYFOLDER') as x:
        with os.scandir('C:/Users/hp/Desktop/harshavc/BACK_UP') as y:
            for i in x:
                for j in y:
                    if(str(j) == str(i)):
                        f1=open(j,'r')
                        f1_text=f1.read()
                        f2=open(i,'r')
                        f2_text=f2.read()
                        print("FILE CREATE TIME : %s" % time.ctime(os.path.getctime(i)))
                        print("FILE LAST MODIFIED TIME : %s" % time.ctime(os.path.getmtime(i)))
                        print(" ")
                        print("MODIFICATIONS IN THE FILE ARE: ", j)
                        print("PREVIOUSLY: " ,f1_text)
                        print("UPDATED: ", f2_text)
                        for line in difflib.unified_diff(f1_text, f2_text, fromfile=str(j),tofile=str(i),lineterm=''):
                            print(line)
                            break
print(os.getcwd())
                

