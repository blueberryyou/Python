x = str(input("请输入您的银行卡号："))
for i in range(0, len(x)):
    if (i + 1) % 4 == 0:
        print(end=' ')
    print(x[i], end='')
