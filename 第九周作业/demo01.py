import random
str1=''
for i in range(6):
    x=random.randint(1,3)
    if x==1:
        a=48+random.randint(0,9)
        str1=str1+chr(a)
    if x==2:
        a=65+random.randint(0,25)
        str1=str1+chr(a)
    if x==3:
        a=97+random.randint(0,25)
        str1=str1+chr(a)
print("验证码：{}".format(str1))




