from tkinter import *
from tkinter.messagebox import *
def run1():
    a = str(enter1.get())
    b = str(enter2.get())
    if a=='user1' and b=='123':
        btn.config(text='登陆成功！')
    else :
        btn.config(text='账号密码错误！')
root=Tk()
root.title('Blue')
root.geometry('260x150')
l1=Label(root,text='用户名：')
l1.grid(row=0, padx='10', pady='10')
enter1 = Entry(root)
enter1.grid(row=0, column=1, padx='10', pady='10')
l2=Label(root,text='密码：')
l2.grid(row=1, padx='10', pady='10')
enter2 = Entry(root)
enter2.grid(row=1, column=1, padx='10', pady='10')
btn= Button(root, text="登 录", width='15',command=run1)
btn.grid(row=2, column=0, columnspan=2, pady='10')
root.mainloop()
