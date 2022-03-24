from tkinter import*
def run1():
    r = float(inp1.get())
    c = 2*3.14*r
    s = 3.14*r*r
    v = 4/3*3.14*r*r*r
    c = ('%.2f' % c)
    s = ('%.2f' % s)
    v = ('%.2f' % v)
    inp2.insert(END, c)  # 追加显示运算结果
    inp3.insert(END, s)  # 追加显示运算结果
    inp4.insert(END, v)  # 追加显示运算结果
def run2():
    exit()
# 窗体
root=Tk()
root.title('Form1')
root.geometry('350x280')
# 半径
lb1 = Label(root, text='请输入半径：')
lb1.place(relx=0.03, rely=0.1, relwidth=0.5, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.4, rely=0.1, relwidth=0.4, relheight=0.1)
# 周长
lb2 = Label(root, text='圆的周长：')
lb2.place(relx=0.03, rely=0.25, relwidth=0.5, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.4, rely=0.25, relwidth=0.4, relheight=0.1)
# 面积
lb3 = Label(root, text='圆的面积：')
lb3.place(relx=0.03, rely=0.4, relwidth=0.5, relheight=0.1)
inp3 = Entry(root)
inp3.place(relx=0.4, rely=0.4, relwidth=0.4, relheight=0.1)
# 体积
lb4 = Label(root, text='球的体积：')
lb4.place(relx=0.03, rely=0.55, relwidth=0.5, relheight=0.1)
inp4 = Entry(root)
inp4.place(relx=0.4, rely=0.55, relwidth=0.4, relheight=0.1)
# 按钮功能
btn1 = Button(root, text='计算', command=run1)
btn1.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.1)
btn1 = Button(root, text='退出', command=run2)
btn1.place(relx=0.6, rely=0.7, relwidth=0.3, relheight=0.1)
root.mainloop()