list = []
while 1:
    print("")
    print("欢迎使用好友管理系统")
    print("1:添加好友")
    print("2:删除好友")
    print("3:备注好友")
    print("4:展示好友")
    print("5:退出")
    choice = eval(input("请输入您的选择："))
    #添加好友
    if choice == 1:
        name = input("请输入要添加的好友：")
        list.append(name)
        print("好友添加成功")
    #删除好友
    elif choice == 2:
        name = input("请输入要删除的好友：")
        list.remove(name)
        print("好友删除成功")
    # 修改名字
    elif choice == 3:
        name = input("请输入要修改备注的好友：")
        x=list.index(name)
        nameupdate = input("请输入新的备注：")
        list[x]=nameupdate
    #输出好友列表
    elif choice == 4:
        if len(list):
            print(list)
        else:
            print("好友列表为空")
            print(list)
    #退出程序
    elif choice == 5:
        exit(0)

