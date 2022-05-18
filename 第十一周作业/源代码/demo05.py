from tkinter import*
import math
def run1():
    a = float(inp1.get())
    b = float(inp2.get())
    x = a+b
    inp3.insert(END, x)
root=Tk()
root.config(bg='gray')
root.title('Form1')
root.geometry('350x250')
#输入框1
inp1 = Entry(root,bg='pink')
inp1.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)
#‘+’号
lb1 = Label(root,text='+',bg='gray')
lb1.place(relx=0.35, rely=0.1, relwidth=0.02, relheight=0.1)
#输入框2
inp2 = Entry(root,bg='green')
inp2.place(relx=0.42, rely=0.1, relwidth=0.2, relheight=0.1)
#‘=’号
lb2 = Label(root,text='=',bg='gray')
lb2.place(relx=0.66, rely=0.1, relwidth=0.02, relheight=0.1)
#结果框
inp3 = Entry(root,bg='blue')
inp3.place(relx=0.72, rely=0.1, relwidth=0.2, relheight=0.1)
# 按钮
btn1 = Button(root, text='计算', command=run1,bg='yellow')
btn1.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.1)
root.mainloop()
