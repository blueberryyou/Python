str = eval(input("请输入字符串："))
print("解密后的字符串为：",end='')
for i in range(0,len(str)):
    if chr(ord(str[i]))>='v':
        print(chr(ord(str[i])-21),end='')
    else:
        print(chr(ord(str[i])+5),end='')