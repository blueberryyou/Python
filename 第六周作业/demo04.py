def takeSecond(elem):
    return elem[1]
def takeFirst(elem):
    return elem[0]
list = [(0,'零'),(1,'壹'),(2,'贰'),(3,'叁'),(4,'肆'),(5,'伍'),(6,'陆'),(7,'柒'),(8,'捌'),(9,'玖')]
str=input("请输入一串阿拉伯数字：")
print("转为中文大写数字为：",end='')
for i in range(len(str)):
    for j in range(0,10):
        if int(str[i])==int(takeFirst(list[j])):
            print(takeSecond(list[j]),end='')
