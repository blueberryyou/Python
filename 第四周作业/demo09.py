list = []
for i in range(0,5):
    score=input("请输入学生{}的成绩：".format(i+1))
    list.append(score)
print("这5位学生成绩：")
for i in range(0,5):
    print("学生{}的成绩是{}".format(i+1,list[i]))
