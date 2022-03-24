num = eval(input("请输入地区编号（1、2、3）: "))
weight = float(input("请输入快递重量（kg）: "))
if num == 1:
    if weight <= 2:
        print("本次快递13元")
    else:
        print("本次快递{}元".format(13 + 3 * (weight - 2)))
if num == 2:
    if weight <= 2:
        print("本次快递12元")
    else:
        print("本次快递{}元".format(12 + 2 * (weight - 2)))
if num == 3:
    if weight <= 2:
        print("本次快递14元")
    else:
        print("本次快递{}元".format(14 + 4 * (weight - 2)))
