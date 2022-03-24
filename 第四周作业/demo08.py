list = ['A01']
for i in range(2,10):
    list.append('A0'+str(i))
for i in range(10,31):
    list.append('A' + str(i))
print("方式一：")
print("座位编码")
print(list)
print("方式二：")
print("座位编码")
for i in range(0,30):
    print(list[i],end=' ')