list = []
list.append(399)
list.append(4369)
list.append(539)
list.append(288)
list.append(109)
list.append(749)
list.append(235)
list.append(190)
list.append(99)
list.append(1000)
max=eval(input("最高价格为："))
min=eval(input("最低价格为："))
print("请选择升序or降序")
print("1.升序     2.降序")
x=eval(input())
if x==1:
    list.sort(key=None, reverse=False)
    print("升序排序为：",list)
elif x==2:
    list.sort(key=None, reverse=True)
    print("降序排序为：",list)




