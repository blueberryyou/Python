n = eval(input("请输入n:"))
sum=0
pro=1
for i in range(1,n+1):
    pro=pro*i
    sum=sum+pro
print("阶乘之和为{}".format(sum))