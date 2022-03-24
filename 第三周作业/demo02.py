distance = eval(input("请输入房子距离市中心的距离（公里）："))
area = eval(input("请输入房子的面积（平方米）："))
price = 0
if distance < 10:
    price = 3*area
else:
    price = 1.5*area
print("房子的总房价为：{}万元".format(price))

