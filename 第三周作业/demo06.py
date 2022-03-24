x = eval(input("请输入您的酒精含量（mg/100ml）："))
if x >= 80:
    print("您是醉酒驾驶！")
elif 20 <= x < 80:
    print("您是饮酒驾驶！")
elif x < 20:
    print("您是正常驾驶！")
