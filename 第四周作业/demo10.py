import random
list = []
for i in range(0,10):
    list.append(random.randint(0,100))
print("这10位学生成绩：")
for i in range(0,10):
    print("学生{}的成绩是{}".format(i+1,list[i]))
max=0
for i in range(1,10):
    if list[i]>list[max]:
        max=i
print("最高分为{}，是学生{}".format(list[max],max+1))


