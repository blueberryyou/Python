from tkinter import*
import math
def run1():
    a = float(inp1.get())
    b = float(inp2.get())
    sin = b/a
    cos = math.sqrt(1-sin*sin)
    tan = sin/cos
    sin = ('%.2f' % sin)
    cos = ('%.2f' % cos)
    tan = ('%.2f' % tan)
    inp3.insert(END, sin)  # 追加显示运算结果
    inp4.insert(END, cos)  # 追加显示运算结果
    inp5.insert(END, tan)  # 追加显示运算结果
def run2():
    exit()
# 窗体
root=Tk()
root.title('Form1')
root.geometry('350x250')
# 斜边长度
lb1 = Label(root, text='斜边长度：')
lb1.place(relx=0.04, rely=0.1, relwidth=0.2, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.23, rely=0.1, relwidth=0.2, relheight=0.1)
# 直角边长度
lb2 = Label(root, text='直角边长度：')
lb2.place(relx=0.47, rely=0.1, relwidth=0.2, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.71, rely=0.1, relwidth=0.2, relheight=0.1)
# 正弦值
lb3 = Label(root, text='正弦值：')
lb3.place(relx=0.04, rely=0.3, relwidth=0.2, relheight=0.1)
inp3 = Entry(root)
inp3.place(relx=0.23, rely=0.3, relwidth=0.2, relheight=0.1)
# 余弦值
lb4 = Label(root, text='余弦值：')
lb4.place(relx=0.47, rely=0.3, relwidth=0.2, relheight=0.1)
inp4 = Entry(root)
inp4.place(relx=0.71, rely=0.3, relwidth=0.2, relheight=0.1)
# 正切值
lb5 = Label(root, text='正切值：')
lb5.place(relx=0.04, rely=0.5, relwidth=0.2, relheight=0.1)
inp5 = Entry(root)
inp5.place(relx=0.23, rely=0.5, relwidth=0.2, relheight=0.1)
# 按钮功能
btn1 = Button(root, text='计算', command=run1)
btn1.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.1)
btn1 = Button(root, text='退出', command=run2)
btn1.place(relx=0.6, rely=0.7, relwidth=0.3, relheight=0.1)
root.mainloop()