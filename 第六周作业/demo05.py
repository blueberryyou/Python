import random
x=0
y=0
sum1=0
sum2=0
list=[]
list_pick=[]
for i in range(0,6):
    x=random.randint(1,33)
    for j in range(0,i):
        while x<=list[j]:
            x=random.randint(1, 33)
    list.append(x)
list.append((random.randint(1,16)))
print("1.机选")
print("2.自定义输入")
choice=input("请输入您的选择：")
if int(choice)==1:
    for i in range(0, 6):
        y = random.randint(1, 33)
        for j in range(0, i):
            while y <= list_pick[j]:
                y=random.randint(1, 33)
        list_pick.append(y)
    list_pick.append((random.randint(1, 16)))
    print("机选双色球为{}".format(list_pick))
elif int(choice)==2:
    for i in range(0,7):
        list_pick.append(input())
print("中奖双色球为{}".format(list))
for i in range(0,6):
    if int(list[i])==(list_pick[i]):
        sum1=sum1+1
if int(list[6])==int(list_pick[6]):
    sum2=1
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







