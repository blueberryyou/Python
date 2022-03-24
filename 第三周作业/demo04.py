x=float(input("请输入体重（kg为单位：）"))
y=float(input("请输入身高（m为单位：）"))
BMI=x/(y*y)
if BMI>=28 :
    print("非常肥胖")
elif 24<BMI<28 :
    print("肥胖")
elif 18.5<BMI<=24 :
    print("正常")
else :
    print("偏瘦")

