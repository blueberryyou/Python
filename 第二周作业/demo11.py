import math
x=float(input("请输入三角形的x边："))
y=float(input("请输入三角形的y边："))
z=float(input("请输入三角形的z边："))
q=(x+y+z)/2
s=math.sqrt(q-x)*(q-y)*(q-z)
print("三角形的面积S为{}".format(s))
