def takeSecond(elem):
    return elem[1]
def takeFirst(elem):
    return elem[0]
list = [(1,399),(2,4369),(3,539),(4,288),(5,109),(6,749),(7,235),(8,190),(9,99),(10,1000)]
max=eval(input("请输入最大临界值 : "))
min=eval(input("请输入最小临界值 : "))
list.sort(key=takeSecond)
for i in range(0,10):
    if min<=takeSecond(list[i])<=max:
        print("{}号商品，价格为：{}".format(takeFirst(list[i]),takeSecond(list[i])))