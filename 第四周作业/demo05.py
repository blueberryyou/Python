#单次测试10道题
import random
s=0
i=1
while i<=10:
    i=i+1
    x=random.randint(1, 11)
    y=random.randint(1,11)
    z=random.choice('+-*/')     #从序列中随机选取一个元素
    print("{}{}{}=".format(x,z,y),end="")
    n=eval(input())
    if z=='+':
        if n==x+y:
            s=s+1
    elif z=='-':
        if n==x-y:
            s=s+1
    elif z=='*':
        if n==x*y:
            s=s+1
    elif z=='/':
        if n==x/y:
            s=s+1
print("一共10道题！您做对{}道题".format(s))
print("您一共得{}分".format(s*10))

