# place 几何布局管理器
# 二维网格的单元格中
from tkinter import *
root = Tk()
pane = Frame(root, width=400, height=200)   # 设置框架大小
pane.pack()

Label(pane, text="Pane Title").place(x=10, y=10)    # 绝对位置
b = Button(pane, text="Enter", width=50, height=5)
b.place(relx=0.5, rely=0.5, anchor=CENTER)          # 相对位置 Button 中心再0.5,0.5处
root.mainloop()
