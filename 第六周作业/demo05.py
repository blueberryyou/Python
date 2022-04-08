import random
x=0
y=0
sum1=0
sum2=0
list=[]
list_pick=[]
#选双色球
print("1.机选")
print("2.自定义输入")
choice=int(input("请输入您的选择："))
#机选
if int(choice)==1:
    for i in range(0, 6):
        y = random.randint(1, 33)
        if y<10:
            y='0'+str(y)
        list_pick.append(str(y))
    list_pick.sort()
    y=random.randint(1, 16)
    if int(y) < 10:
        y = '0' + str(y)
    list_pick.append(str(y))
    print("机选双色球为{}".format(list_pick))
#自定义选择
elif int(choice)==2:
    for i in range(0,6):
        y=eval(input("请输入红色球的号码，范围在1-33："))
        if y<10:
            y='0'+str(y)
        list_pick.append(str(y))
    list_pick.sort()
    y = eval(input("请输入蓝色球号码，范围在1-16："))
    if y < 10:
        y = '0' + str(y)
    list_pick.append(str(y))
    print("自选双色球为{}".format(list_pick))

#开奖
for i in range(0,6):
    x=random.randint(1,33)
    if x < 10:
        x = '0' + str(x)
    list.append(str(x))
list.sort()
x=random.randint(1,16)
if x < 10:
    x = '0' + str(x)
list.append(str(x))
print("中奖双色球为{}".format(list))
#统计中奖个数
for i in range(0,6):
    if str(list[i])==str(list_pick[i]):
        sum1=sum1+1
if str(list[6])==str(list_pick[6]):
    sum2=1
#判断奖金
if sum1<=2 and sum2==1:
    print("奖金5元！")
elif sum1+sum2==4:
    print("奖金10元！")
elif sum1+sum2==5:
    print("奖金200元！")
elif sum1==5 and sum2==1:
    print("奖金3000元！")
elif sum1==6:
    print("奖金10万元！")
elif sum1==6 and sum2==1:
    print("奖金500万元！")
else:
    print("很遗憾您未中奖！")