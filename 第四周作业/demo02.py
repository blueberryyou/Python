import math
s1=0
s2=0
s3=0
s4=0
s5=0
str=eval(input("请输入一个字符串："))
for i in range(0,len(str)):
		if str[i]>='A' and str[i]<='Z' :
			s1=s1+1
		elif str[i]>='a' and str[i]<='z':
			s2=s2+1
		elif str[i]>='0' and str[i]<='9':
			s3=s3+1
		elif str[i] == ' ':
		# elif ord(str[i])==32:   right
			s4=s4+1
		else:
			s5=s5+1
print("大写字母有{}个".format(s1))
print("小写字母有{}个".format(s2))
print("数字字符有{}个".format(s3))
print("空格有{}个".format(s4))
print("其他字符有{}个".format(s5))

