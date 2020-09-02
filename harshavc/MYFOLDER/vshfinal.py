import os
import os.path, time
import difflib

with os.scandir('C:/Users/hp/Desktop/harshavc//MYFOLDER') as x:
    with os.scandir('C:/Users/hp/Desktop/harshavc//BACK_UP') as y:
        for i in x:
            for j in y:
                if (str(j) == str(i)):
                    f1 = open(j, 'r')
                    f1_text = f1.read()
                    f2 = open(i, 'r')
                    f2_text = f2.read()
                    print("FILE CREATE TIME : %s" % time.ctime(os.path.getctime(i)))
                    print("FILE LAST MODIFIED TIME : %s" % time.ctime(os.path.getmtime(i)))
                    print(" ")
                    print("MODIFICATIONS IN THE FILE ARE: ")
                    # for line in difflib.context_diff(f1_text, f2_text, fromfile=str(j), tofile=str(i), lineterm=''):
                    #     print(line[:], end="")
                    diff = difflib.ndiff(f1_text.splitlines(keepends=True), f2_text.splitlines(keepends=True))

                    print(''.join(diff), end="")
