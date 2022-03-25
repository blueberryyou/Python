import random
x = ""
y = ""
for i in range(4):
    index = random.randrange(0, 3)  # 它在[0,1)范围内
    if index == 0:
        x = x + chr(random.randint(97, 122))
    elif index == 1:
        x = x + chr(random.randint(65, 90))
    else:
        x = x + str(random.randint(1, 9))
print("验证码：{}".format(x))
y = eval(input("请输入验证码:"))
while y != x:
    print("验证码错误！")
    x = ""
    y = ""
    for i in range(4):
        index = random.randrange(0, 3)  # 它在[0,1)范围内
        if index == 0:
            x = x + chr(random.randint(97, 122))
        elif index == 1:
            x = x + chr(random.randint(65, 90))
        else:
            x = x + str(random.randint(1, 9))
    print("验证码：{}".format(x))
    y = eval(input("请输入验证码:"))
print("验证码正确！")
