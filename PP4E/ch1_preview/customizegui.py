from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102OOP import MyGui

class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='Ouch!')

if __name__ == "__main__":
    CustomGui().pack()
    mainloop()