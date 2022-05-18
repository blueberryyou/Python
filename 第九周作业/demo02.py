# from turtle import * #将turtle中的所有方法导入
# forward(degree)  #向前移动距离degree代表距离
# backward(degree)  #向后移动距离degree代表距离
# right(degree)    #向右移动多少度
# left(degree)  #向左移动多少度
# goto(x,y)  #将画笔移动到坐标为x,y的位置
# stamp()     #复制当前图形
# speed(speed)  #画笔绘制的速度范围[0,10]整数
# down() #移动时绘制图形,缺省时也为绘制
# up() #移动时不绘制图形
# pensize(width) #绘制图形时的宽度
# color(colorstring) #绘制图形时的颜色
# fillcolor(colorstring) #绘制图形的填充颜色
# fill(Ture)
# fill(false)

from turtle import*
fillcolor("pink")
color("pink")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()
# done()界面停留
# pos()返回海龟的当前位置
# abs()返回当前位置与原点的距离