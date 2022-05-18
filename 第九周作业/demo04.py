import random
i=1
n=0
f1=open("math1.txt","w",encoding='utf-8')
f2=open("math2.txt","w",encoding='utf-8')
while i<=20:
    x=random.randint(1, 11)
    y=random.randint(1,11)
    z=random.choice('+-*/')     #从序列中随机选取一个元素
    if(i%2==0):
        f1.write(str(x) + str(z) + str(y) + "="+"\n")
    else:
        f1.write(str(x) + str(z) + str(y) + "="+"\t\t\t")
    if z=='+':
        n=x+y
        if (i % 2 == 0):
            f2.write(str(x) + str(z) + str(y) + "=" + str(n) + "\n")
        else:
            f2.write(str(x) + str(z) + str(y) + "=" + str(n) + "\t\t\t")
    elif z=='-':
        n = x - y
        if (i % 2 == 0):
            f2.write(str(x) + str(z) + str(y) + "=" + str(n) + "\n")
        else:
            f2.write(str(x) + str(z) + str(y) + "=" + str(n) + "\t\t\t")
    elif z=='*':
        n=x*y
        if (i % 2 == 0):
            f2.write(str(x) + str(z) + str(y) + "=" + str(n) + "\n")
        else:
            f2.write(str(x) + str(z) + str(y) + "=" + str(n) + "\t\t\t")
    elif z=='/':
        n=x/y
        n = round(n, 2)  # 将a通过round函数处理后赋值给n，传入的n代表保留两位小数
        if (i % 2 == 0):
            f2.write(str(x) + str(z) + str(y) + "=" + str(n) + "\n")
        else:
            f2.write(str(x) + str(z) + str(y) + "=" + str(n) + "\t\t\t")
    i = i + 1

