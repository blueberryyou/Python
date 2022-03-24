password=eval(input("请输入六位数数字密码(字符串)："))
x=0
pw=0
s1=0
s2=''
for i in range(0,6):
    x=ord(password[i])-48
    s1=s1+x
    s2=str(ord(password[i]))+s2
    pw=s1+int(s2)
print("加密后的密码为{}".format(pw))
