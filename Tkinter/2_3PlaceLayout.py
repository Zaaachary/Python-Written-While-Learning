# grid 几何布局管理器
# 二维网格的单元格中
from tkinter import *
root = Tk()

l1 = Label(text="计算器")
l1.grid(row=0, column=0, columnspan=2)

e1 = Entry()
e1.grid(row=1, column=0)
e2 = Entry()
e2.grid(row=2, column=0)
e3 = Entry()
e3.grid(row=3, column=0)

bt1 = Button(text="run", width=20, height=2)
bt1.grid(row=1, column=1, columnspan=1, rowspan=3, sticky='e')
root.mainloop()
