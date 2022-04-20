words = set()
while 1:
	print("="*20)
	print("欢迎来到你的生词本！")
	print("1.查看生词列表")
	print("2.背单词")
	print("3.添加新单词")
	print("4.删除单词")
	print("5.清空生词本")
	print("6.退出程序")
	print("="*20)
	choice = eval(input("请输入你的选择："))
	if choice==1:
		print(words)
	if choice==2:
		wd=words.pop()
		print(wd)
		print("背会了吗？该单词删除还是保留？")
		print("1.删除")
		print("2.保留")
		c = eval(input("请选择："))
		if c==1:
			words.discard(wd)
	if choice==3:
		while choice==3:
			wd =str(input("请输入单词及意思（以-1为结束）："))
			if wd=="-1":
				break
			if not wd in words:
				words.add(wd)
				print("已存入生词本！")
	if choice==4:
		wd=str(input("请输入您要删除的单词及意思："))
		if not wd in words:
			print("单词未在生词本中！")
		else:
			words.discard(wd)
	if choice==5:
		words.clear()
	if choice==6:
		exit(0)