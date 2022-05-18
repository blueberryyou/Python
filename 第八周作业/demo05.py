x=eval(input("请输入第一个数字："))
y=eval(input("请输入第二个数字："))
def f(x,y):
    op=str(input("请输入算术符："))
    if op=="+":
        print("{}+{}={}".format(x,y,x+y))
    if op=="-":
        print("{}-{}={}".format(x,y,x-y))
    if op=="*":
        print("{}*{}={}".format(x, y, x*y))
    if op=="/":
        print("{}/{}={}".format(x,y,x/y))
f(x,y)