data=[{'name':"zsy",'tel':979,'email':2506573157,'adress':"河南"}]
while 1:
	print("="*20)
	print("欢迎使用通讯录！")
	print("1.添加联系人")
	print("2.查看通讯录")
	print("3.删除联系人")
	print("4.修改联系人信息")
	print("5查找联系人")
	print("6.退出程序")
	print("="*20)
	choice = eval(input("请输入你的选择："))
	if choice==1:
		name=str(input("请输入联系人姓名："))
		tel=eval(input("请输入联系人电话："))
		email=eval(input("请输入联系人邮箱："))
		adress=str(input("请输入联系人地址："))
		data.append({'name':name,'tel':tel,'email':email,'adress':adress})
		print("联系人信息添加成功！")
	if choice==2:
		print(data)
	if choice==3:
		name=str(input("请输入将要删除联系人的姓名："))
		for i in range(len(data)):
			if data[i]['name']==name:
				del data[i]
				break
		print("联系人删除成功！")
	if choice==4:
		name = str(input("请输入修改联系人的姓名："))
		for i in range(len(data)):
			if data[i]['name'] == name:
				del data[i]
				name = str(input("请输入联系人姓名："))
				tel = eval(input("请输入联系人电话："))
				email = eval(input("请输入联系人邮箱："))
				adress = str(input("请输入联系人地址："))
				data.append({'name': name, 'tel': tel, 'email': email, 'adress': adress})
				print("联系人信息修改成功！")
				break
	if choice==5:
		name = str(input("请输入查找联系人的姓名："))
		for i in range(len(data)):
			if data[i]['name'] == name:
				print(data[i])
				break
	if choice==6:
		exit(0)