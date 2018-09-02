# pack几何布局管理器
# side 取值 top bottom left right
from tkinter import *
root = Tk()
f1 = Frame(); f1.pack()
f2 = Frame(); f2.pack()
f3 = Frame(); f3.pack()

bt1 = Button(f1, text="按钮1")
bt1.pack(side='right')
bt2 = Button(f1, text="按钮2")
bt2.pack()

l1 = Label(f2, text="请输入")
l1.pack(side=LEFT)
e1 = Entry(f2)
e1.pack()

bt3 = Button(f3, text='按钮三')
bt3.pack(side="left")
bt4 = Button(f3, text='按钮四')
bt4.pack(side="left")

root.mainloop()
