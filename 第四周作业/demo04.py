#2.0版
import random
num = random.randint(20, 40)
i = 0
while (i < 5):
    a = input("请输入一个数字：")
    a1 = int(a)
    i += 1
    if (a1 < num):
        print("猜小了")
        continue
    elif (a1 > num):
        print("猜大了")
        continue
    else:
        print("恭喜你猜对了！数字是%s" % (num))
        break
if (i == 5):
    print("失败！！！")
#1.0版
# x=eval(input("玩家A请输入目标数字："))
# y=eval(input("玩家B请输入猜测数字："))
# n=5
# while y!=x and n!=0:
#     n=n-1
#     if y>x:
#         print("猜大了，请重新猜测，您还有{}次机会".format(n))
#         y = eval(input("玩家B请输入猜测数字："))
#     elif y<x:
#         print("猜小了，请重新猜测，您还有{}次机会".format(n))
#         y = eval(input("玩家B请输入猜测数字："))
#     elif y==x:
#         print("恭喜您，猜对了！")
#         break
# print("您的机会已用完!本次猜测不计入成绩！")
#

