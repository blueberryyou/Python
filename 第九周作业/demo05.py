import os
f=open("example.txt","r",encoding='utf-8')
f1 = open("FinalExample.txt", "a+", encoding='utf-8')
x=0
lines=f.readlines()
for line in lines:
    if line== "小结\n" or line == "习题\n":
        line = "  " + line
    for i in line:
        if i=='.':
            x=x+1
    if x==1:
        line="  "+line
    if x==2:
        line="    "+line
    f1.writelines(line)
    x=0
f.close()
f1.close()
os.remove("example.txt")
