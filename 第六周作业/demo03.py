import random
list1=[]
list=[]

#plan 1
for i in range(0,8):
    list1.append(random.randint(1,3))
print("八位老师的办公室编号依次是：{}".format(list1))

#plan 2
list2=[2,3,3]
list3=[0,0,0]
for i in range(0,8):
    x = random.randint(0, 2)
    while list3[x]>=list2[x]:
        x = random.randint(0, 2)
    list.append(x+1)
    list3[x] = list3[x] + 1
print("八位老师的办公室编号依次是：{}".format(list))

