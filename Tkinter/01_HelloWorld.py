# 01_HelloWorld.py
from tkinter import *

# 窗口1
root_1 = Tk()
w = Label(root_1, text="Hello, world!")
w.pack()
root_1.mainloop()

# 窗口2
root_2 = Tk()
root_2.title("window created by Tkinter")     # 窗口标题
root_2['width'] = 400
root_2['height'] = 200
print(root_2.keys())                          # 显示窗口属性字典
root_2.geometry('600x200+200+100')
root_2.mainloop()

# ['bd', 'borderwidth', 'class', 'menu', 'relief',
# 'screen', 'use', 'background', 'bg', 'colormap',
# 'container', 'cursor', 'height', 'highlightbackground',
# 'highlightcolor', 'highlightthickness', 'padx', 'pady',
# 'takefocus', 'visual', 'width']
